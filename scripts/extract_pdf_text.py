import argparse
from pathlib import Path
import re
import fitz
try:
    import pymupdf4llm as _pymd
    _HAS_PYMUPDF4LLM = True
except Exception:
    _HAS_PYMUPDF4LLM = False
try:
    from pdfminer.high_level import extract_text as _pdfminer_extract_text
    from pdfminer.layout import LAParams as _PDFLAParams
    _HAS_PDFMINER = True
except Exception:
    _HAS_PDFMINER = False


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def _is_page_number(s: str) -> bool:
    return bool(re.fullmatch(r"\d{1,4}", s.strip()))


def _find_repeated_headers(doc: fitz.Document) -> set[str]:
    """Collect header/footer lines that repeat on many pages.

    Heuristic: any line near top/bottom margin that appears on >= 40% of pages.
    """
    from collections import Counter

    counts = Counter()
    n_pages = doc.page_count
    for i in range(n_pages):
        p = doc.load_page(i)
        h = float(p.rect.height)
        margin = max(36.0, 0.08 * h)
        for _, y0, _, y1, txt, *_ in (p.get_text("blocks") or []):
            if not isinstance(txt, str) or not txt.strip():
                continue
            for line in txt.splitlines():
                s = line.strip()
                if not s:
                    continue
                if y0 < margin or y1 > (h - margin):
                    counts[_norm(s[:160])] += 1
    threshold = max(3, int(0.4 * n_pages))
    return {k for k, c in counts.items() if c >= threshold}


def _reflow_page_text(page, header_footer_norms: set[str] | None = None) -> str:
    """Reconstruct paragraphs from lines using geometry and remove headers/footers.

    Works even when each line is a separate block.
    """
    header_footer_norms = header_footer_norms or set()
    d = page.get_text("dict") or {}
    h = float(page.rect.height)
    margin = max(36.0, 0.08 * h)

    lines = []  # (y0, y1, x0, text)
    for b in d.get("blocks", []):
        if b.get("type", 0) != 0:
            continue
        for ln in b.get("lines", []):
            text = "".join(s.get("text", "") for s in ln.get("spans", []))
            text = text.strip()
            if not text:
                continue
            y0, x0 = float(ln["bbox"][1]), float(ln["bbox"][0])
            y1 = float(ln["bbox"][3])
            # Skip common header/footer lines
            if (y0 < margin or y1 > (h - margin)) and (
                _norm(text[:160]) in header_footer_norms
                or _is_page_number(text)
                or "electronic copy available at:" in _norm(text)
            ):
                continue
            lines.append((y0, y1, x0, text))

    if not lines:
        return ""

    lines.sort(key=lambda t: (round(t[0], 2), round(t[2], 2)))
    heights = [y1 - y0 for (y0, y1, _, _) in lines]
    avg_h = (sum(heights) / len(heights)) or 10.0

    paras: list[str] = []
    cur = ""
    prev = None  # (y0,y1,x0,text)
    for y0, y1, x0, text in lines:
        # Normalize internal line breaks / spaces (some PDFs inject soft breaks)
        t = text.replace("\r", "").strip()

        join = False
        if prev is not None:
            vgap = y0 - prev[1]
            indent = x0 - prev[2]
            starts_lower = bool(t) and t[:1].islower()
            if cur.endswith("-"):
                # hyphenation join
                cur = cur[:-1] + t
                join = True
            elif vgap < avg_h * 0.6 and abs(indent) < 14:
                join = True
            elif (
                not cur.endswith((".", "?", "!", ":"))
                and vgap < avg_h * 1.4
                and abs(indent) < 18
            ):
                join = True
            elif cur.endswith((",", ";")) and vgap < avg_h * 1.6 and abs(indent) < 20:
                join = True
            elif starts_lower and vgap < avg_h * 1.8 and abs(indent) < 20:
                join = True

        if join:
            cur += " " + t
        else:
            if cur:
                paras.append(cur)
            cur = t
        prev = (y0, y1, x0, text)

    if cur:
        paras.append(cur)

    # Post-merge: join tiny leading fragments with following paragraph when they
    # clearly continue the sentence (e.g., "In this" + "paper, ...").
    merged: list[str] = []
    i = 0
    join_starters = {
        "and", "or", "but", "so", "because", "while", "whereas", "as",
        "if", "when", "which", "that", "then", "thus", "therefore", "however",
        "moreover", "furthermore", "additionally", "also", "for"
    }
    while i < len(paras):
        curp = paras[i].strip()
        while i + 1 < len(paras):
            nxt = paras[i + 1].strip()
            if not nxt:
                i += 1
                continue
            nxt_first = nxt.split(" ", 1)[0].lower()
            should_join = (
                len(curp) < 120 and  # small fragment
                not curp.endswith((".", "?", "!", ":")) and
                (nxt[:1].islower() or nxt_first in join_starters or curp.endswith("-"))
            )
            if should_join:
                if curp.endswith("-"):
                    curp = curp[:-1] + nxt
                else:
                    curp = curp + " " + nxt
                i += 1
            else:
                break
        merged.append(curp)
        i += 1

    return "\n\n".join(p.strip() for p in merged if p.strip())


def _extract_pdfminer_text(pdf_path: Path) -> str:
    """Use pdfminer.six to extract text and reflow paragraphs with heuristics.

    Also removes page numbers and the SSRN boilerplate lines at page edges.
    """
    if not _HAS_PDFMINER:
        return ""
    laparams = _PDFLAParams(
        line_overlap=0.5,
        char_margin=2.0,
        line_margin=0.3,
        word_margin=0.1,
        boxes_flow=0.5,
        all_texts=True,
        detect_vertical=False,
    )
    raw = _pdfminer_extract_text(str(pdf_path), laparams=laparams) or ""
    # Split by form-feed (page breaks)
    pages = raw.split("\x0c")
    cleaned_pages = []
    for page in pages:
        lines = page.splitlines()
        if not lines:
            continue
        # Strip headers / footers in first / last 3 lines if they look like page # or boilerplate
        start = 0
        end = len(lines)
        for i in range(min(3, len(lines))):
            if _is_page_number(lines[i]) or "electronic copy available at:" in _norm(lines[i]):
                start = i + 1
        for i in range(1, min(3, len(lines)) + 1):
            if _is_page_number(lines[-i]) or "electronic copy available at:" in _norm(lines[-i]):
                end = max(start, len(lines) - i)
        seg = "\n".join(lines[start:end])
        cleaned_pages.append(seg)
    text = "\n\n".join(seg for seg in cleaned_pages if seg.strip())
    # Reflow: fix hyphenation, preserve paragraph breaks, collapse single wraps
    text = text.replace("\r", "")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    return text.strip()


def extract(pdf_path: Path, out_path: Path, fmt: str, keep_lines: bool) -> None:
    doc = fitz.open(pdf_path)
    header_footer = _find_repeated_headers(doc)
    parts = []
    for i in range(doc.page_count):
        page = doc.load_page(i)
        if fmt == "md":
            text = _reflow_page_text(page, header_footer)
            parts.append(text)
        else:
            text = page.get_text("text") if keep_lines else _reflow_page_text(page, header_footer)
            parts.append(text.strip())
    content = "\n\n".join(p for p in parts if p)
    out_path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--out", dest="out", default=None)
    parser.add_argument("--format", dest="fmt", choices=["txt", "md"], default="md")
    parser.add_argument("--keep-lines", dest="keep_lines", action="store_true", help="Preserve original PDF line breaks in TXT output")
    parser.add_argument("--md-engine", choices=["reflow", "llm"], default="reflow", help="Markdown engine: 'reflow' uses line-joining; 'llm' uses pymupdf4llm if available")
    parser.add_argument("--engine", choices=["mupdf", "pdfminer"], default="mupdf", help="Extraction backend. 'pdfminer' can yield smoother paragraphs.")
    args = parser.parse_args()

    in_path = Path(args.pdf)
    out_path = Path(args.out) if args.out else in_path.with_suffix(".md" if args.fmt == "md" else ".txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if args.engine == "pdfminer" and _HAS_PDFMINER:
        txt = _extract_pdfminer_text(in_path)
        out_path.write_text(txt, encoding="utf-8")
    elif args.fmt == "md" and args.md_engine == "llm" and _HAS_PYMUPDF4LLM:
        # Use pymupdf4llm directly for markdown
        doc = fitz.open(in_path)
        md = _pymd.to_markdown(doc)
        out_path.write_text(md, encoding="utf-8")
    else:
        extract(in_path, out_path, args.fmt, args.keep_lines)


if __name__ == "__main__":
    main()
