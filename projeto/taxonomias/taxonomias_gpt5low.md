Objetivos:

- **Classificar sistematicamente** cada consulta.
- **Medir complexidade** (Jagged Frontier).
- **Comparar desempenho de agentes por tipo de tarefa**.

---

# 1. Dimensões principais da taxonomia

Em vez de uma lista única de classes, é sugerida uma **taxonomia multidimensional** (várias “etiquetas” por consulta). Isso é muito útil para analisar fronteira irregular.

## 1.1. Tipo de objetivo da consulta

- **[O1] Consulta factual local**
  Resposta sobre um evento/ponto específico em um poço/operação.
  Ex.: “Como foi o teste de pressão após a 2ª cimentação...”
- **[O2] Consulta factual intervalar**
  Pergunta sobre se algo ocorreu em um intervalo de operações/tempo.
  Ex.: “Houve condicionamento entre o fim da perfuração e a retirada?”
- **[O3] Análise comparativa/multi-poço**
  Varre múltiplos poços/intervenções e responde para cada um.
  Ex.: “Analise todas as perfurações de 2024 e responda se houve retorno de traçador...”
- **[O4] Crosscheck normativo/consistência**
  Confronta um item de conhecimento novo com normas, padrões, ICs etc., buscando alinhamentos/conflitos.
  Ex.: crosscheck de nova recomendação X com Normas/Padrões/ICs.
- **[O5] Pesquisa global/sumarização operacional**
  Varredura ampla (todas as sondas, período de tempo) com resumo estruturado.
  Ex.: “Pesquisa profunda sobre todas as operações em todas as sondas na semana X.”
- **[O6] Investigação de incidente/falha**
  Reconstrução de contexto de falha, linha do tempo, causas possíveis.
  Ex.: investigação da falha na cimentação.
- **[O7] Geração de recomendações/planejamento operacional**
  Toma insumo sobre próximas operações e gera recomendações baseadas em conhecimento histórico/normativo.
  Ex.: relatório com recomendações operacionais com base na NS-48 e KBs.

---

## 1.2. Escopo de dados

- **[D1] Um único poço / uma única sonda / evento pontual**
- **[D2] Múltiplos eventos do mesmo poço/sonda**
- **[D3] Múltiplos poços / múltiplas intervenções**
- **[D4] Todas as sondas / escopo corporativo**

---

## 1.3. Complexidade de recuperação de dados

- **[R1] Recuperação simples**
  Uma única base, filtro direto (ex.: por poço e data).
- **[R2] Recuperação sequencial com marcação de eventos**
  Precisa encontrar eventos específicos (ex.: “2ª cimentação”, “término da perfuração”).
- **[R3] Recuperação multi-base com junção temporal/operacional**
  Combina várias bases com janelas de tempo (D-3 a D+7) e/ou intervalos operacionais.
- **[R4] Recuperação ampla + agregação**
  Varredura de muitas instâncias (ex.: todas intervenções em 2024, todas sondas em uma semana).

---

## 1.4. Natureza do raciocínio

- **[C1] Descritivo (o que aconteceu?)**
  Resumo de eventos, testes, operações.
- **[C2] Presença/ausência/contagem (ocorreu ou não?)**
  Checar se algo aconteceu em um intervalo (circulação, retorno de traçador etc.).
- **[C3] Analítico causal/diagnóstico**
  Entender contexto de falha, relações de causa/efeito, fatores contribuintes.
- **[C4] Normativo-argumentativo**
  Avaliar se algo corrobora ou conflita com normas/padrões, identificar conflitos.
- **[C5] Prescritivo/planejamento**
  Gerar recomendações para ações futuras, com base em conhecimento histórico/normativo.

---

## 1.5. Integração de fontes

- **[S1] 1 base** (ex.: só DDR/T&O)
- **[S2] 2–3 bases**
- **[S3] 4+ bases** (sitops, T&O, Anormalidades, RTO-Live, Incidentes, Normas, Padrões, Lessons, ICs…)

---

## 1.6. Abstração temporal

- **[T1] Evento pontual relativo** (ex.: “após a 2ª cimentação”)
- **[T2] Intervalo operacional** (entre fases, entre início/fim de operação)
- **[T3] Janela temporal absoluta** (D-3 a D+7, semana específica, ano inteiro)

---

# 2. Classificação dos seus exemplos na taxonomia

Vou rotular cada exemplo com as categorias acima (entre colchetes).

---

### Exemplo 1

“Como foi o teste de pressão após a 2a operação de cimentação durante a perfuração do poço X?”

- **Objetivo**: [O1] Consulta factual local
- **Escopo**: [D1] Único poço / evento
- **Recuperação**: [R2] Recuperação sequencial com marcação de eventos
- **Raciocínio**: [C1] Descritivo
- **Fontes**: T&O (DDRs) → [S1] (ou [S2] se combinar outra)
- **Tempo**: [T1] Evento pontual relativo

---

### Exemplo 2

“Foram realizadas operações de circulação ou condicionamento do poço X entre o término da perfuração da fase de 16 1/2" e a retirada?”

- **Objetivo**: [O2] Consulta factual intervalar
- **Escopo**: [D1]/[D2] (um poço, vários eventos)
- **Recuperação**: [R2] (marcar término da perfuração e fim da retirada, buscar operações no intervalo)
- **Raciocínio**: [C2] Presença/ausência
- **Fontes**: T&O / DDRs → [S1]
- **Tempo**: [T2] Intervalo operacional

---

### Exemplo 3

“Analise todas as perfurações realizadas em 2024 e responda, para cada uma, se houve ou não retorno de traçador durante a cimentação do revestimento de superfície.”

- **Objetivo**: [O3] Análise comparativa/multi-poço
- **Escopo**: [D3] Múltiplos poços/intervenções (~30)
- **Recuperação**: [R4] Varredura ampla + agregação
- **Raciocínio**: [C2] Presença/ausência + pequena agregação (tabela por poço)
- **Fontes**: T&O/DDR + possivelmente outros → [S1]/[S2]
- **Tempo**: [T3] Janela anual

---

### Exemplo 4

“Para uma nova recomendação X (de um novo IC), faça um crosscheck com Normas Petrobras, Padrões e ICs indicando itens relacionados (similaridades, conflitos, etc). Determine se cada item encontrado corrobora ou conflita com a nova recomendação.”

- **Objetivo**: [O4] Crosscheck normativo
- **Escopo**: [D3]/[D4] (potencialmente global na KB)
- **Recuperação**: [R3] Multi-base com busca semântica
- **Raciocínio**: [C4] Normativo-argumentativo
- **Fontes**: Normas, Padrões, ICs → [S3]
- **Tempo**: n/a (não é temporal, é conceitual)

---

### Exemplo 5

“Faça uma pesquisa profunda sobre todas as operações ocorridas em todas as sondas marítimas na semana do dia 09/11/2025 a 15/11/2025.”

- **Objetivo**: [O5] Pesquisa global/sumarização operacional
- **Escopo**: [D4] Todas as sondas
- **Recuperação**: [R4] Varredura ampla + agregação
- **Raciocínio**: [C1] Descritivo + síntese de alto nível
- **Fontes**: sitops, T&O, Anormalidades, RTO-Live, Incidentes → [S3]
- **Tempo**: [T3] Janela temporal absoluta (semana)

---

### Exemplo 6

“Faça uma investigação da falha ocorrida na cimentação do revestimento de superfície do poço X.”

- **Objetivo**: [O6] Investigação de incidente/falha
- **Escopo**: [D1]/[D2] (um poço, múltiplos eventos)
- **Recuperação**: [R3] (identificar data da falha e buscar D-3 a D+7 em múltiplas bases)
- **Raciocínio**: [C3] Analítico causal/diagnóstico
- **Fontes**: T&O, Anormalidades, sitops, RTO-Live, Incidentes → [S3]
- **Tempo**: [T3] Janela relativa D-3 a D+7

---

### Exemplo 7

“Faça um relatório com recomendações operacionais levando em consideração as próximas operações previstas na NS-48.”

- **Objetivo**: [O7] Recomendações/planejamento operacional
- **Escopo**: [D1]/[D2] (uma sonda com sua fila de operações)
- **Recuperação**: [R3] (pegar próximas operações no SITOP e buscar recomendações em múltiplas KBs)
- **Raciocínio**: [C5] Prescritivo/planejamento
- **Fontes**: SITOP, Lessons, Padrões, Normas, Anormalidades → [S3]
- **Tempo**: futuro imediato, derivado da NS-48 (sem janela explícita, mas ligado à sequência operacional)

---

# 3. Como usar essa taxonomia na pesquisa (Jagged Frontier)

Algumas ideias de uso direto na sua tese:

- **Eixo de complexidade** pode ser composto por:

  - tipo de objetivo (de O1 até O7),
  - grau de integração de fontes (S1→S3),
  - tipo de raciocínio (C1→C5),
  - complexidade de recuperação (R1→R4).
- **Jagged frontier**:

  - Mapear quais combinações de rótulos os agentes resolvem bem (ex.: O1+D1+R2+C1+S1)
  - vs. quais começam a falhar (ex.: O6+D2+R3+C3+S3, O4+C4+S3, O7+C5+S3).
- **Desenho de experimentos**:

  - Gerar muitos prompts novos, mantendo algumas dimensões fixas e variando outras, para medir sensibilidade da performance.

---

Se você quiser, no próximo passo posso:

- **Refinar essa taxonomia em uma tabela formal**, pronta para virar esquema de anotação (por ex., uma planilha).
- Ou **propor um “índice de complexidade” numérico** combinando as dimensões, para você usar em métricas da tese.
