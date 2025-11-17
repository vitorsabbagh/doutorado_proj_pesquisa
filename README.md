## Projeto de Pesquisa para Doutorado

**Autor:** Vitor Brandão Sabbagh

### 1. Título

**Mapeando a Fronteira Irregular: Uma Análise Experimental da Capacidade de Agentes Baseados em LLM em Tarefas de Engenharia de Poços**

*(Mapping the Jagged Frontier: An Experimental Analysis of LLM-Based Agent Capabilities in Complex Offshore Well Engineering Tasks)*

### 2. Introdução e Contextualização

A ascensão dos Grandes Modelos de Linguagem (LLMs) marca uma transição da IA como ferramenta de consultas simples (Q&A) para a IA como agente autônomo. Sistemas de agentes agora podem decompor problemas, planejar e executar tarefas de múltiplos passos.

Contudo, a rápida adoção dessa tecnologia na indústria, especialmente em setores de alto risco como Óleo e Gás (O&G), supera nossa compreensão de seus reais limites. O entusiasmo com as capacidades de "pico" (sucesso) muitas vezes ofusca a existência de "vales" (falhas) em suas capacidades.

O influente estudo de Mollick et al. (2023) com o BCG introduziu o conceito de "Fronteira Tecnológica Irregular" (Jagged Frontier) para descrever como o desempenho da IA é irregular, alternando entre picos de competência super-humana e vales de falha. No entanto, este estudo focou na produtividade de *humanos usando IA* em tarefas de consultoria. [DETALHAR TAREFAS]

**A lacuna que este projeto aborda é:** a fronteira irregular para *agentes autônomos* em domínios de *engenharia de alta complexidade* permanece desconhecida. Não sabemos quais tarefas na construção de poços de petróleo (um domínio em que falhas podem custar vidas e/ou centenas de milhões de dólares) estão nos "picos" e quais estão nos "vales".

### 3. Problema de Pesquisa e Objetivos

#### Problema Central

A implantação de agentes de LLM em atividades diversas de O&G é dificultada pela falta de um mapa de risco-capacidade. As métricas de *benchmarks* genéricos (ex: MMLU, AgentBench) [LER, DETALHAR E CITAR] não capturam as nuances de tarefas de engenharia do mundo real, que envolvem dados ruidosos, raciocínio físico e adesão estrita a normas de segurança.

#### Pergunta Principal de Pesquisa (P1)

Onde se localiza, e qual é a topografia, da "fronteira irregular" de capacidade para agentes de LLM no domínio de planejamento e execução de tarefas da construção de poços offshore?

#### Perguntas Secundárias (P2-P4)

* **(P2)** Quais características de uma tarefa (ex: necessidade de raciocínio causal, dependência de dados físicos, conformidade regulatória, planejamento temporal) definem um "pico" (sucesso do agente) ou um "vale" (falha do agente)?
* **(P3)** Como diferentes arquiteturas de agentes (ex: LLM "puro" vs. RAG vs. Agentes de Planejamento) navegam por essa fronteira?
* **(P4)** É possível desenvolver um *framework* para identificar "vales" *a priori*, permitindo a implantação segura de agentes em tarefas de "pico"?

#### Objetivo Geral

Mapear e caracterizar a fronteira irregular de capacidade de agentes de LLM no domínio de engenharia de poços, identificando os fatores que determinam o sucesso e a falha em tarefas complexas.

#### Objetivos Específicos

1. **OE1:** Desenvolver uma taxonomia de tarefas representativas da construção de poços offshore, classificadas por tipo de cognição e complexidade.
2. **OE2:** Projetar e implementar um *benchmark* experimental baseado nesta taxonomia, com métricas de avaliação e *ground truth* definidos por especialistas.
3. **OE3:** Avaliar sistematicamente diferentes arquiteturas de agentes de LLM (ex: GPT-5, Claude 4, Llama 4 com diferentes *frameworks* de agentes) neste *benchmark*.
4. **OE4:** Analisar os resultados para construir o "mapa" da fronteira irregular, correlacionando tipos de tarefa com o desempenho dos agentes.
5. **OE5:** Propor um *framework* de decisão para a implantação segura de agentes na indústria de O&G, baseado nas descobertas.

### 4. Justificativa e Relevância

Este projeto possui relevância em três eixos:

1. **Contribuição para a Ciência da Computação (Teórica):** Estende a teoria da "Fronteira Irregular" do campo de Interação Humano-Computador (HCI) para o campo de Agentes Autônomos. Além disso, critica e avança o estado da arte em *benchmarking* de agentes, saindo de tarefas genéricas para domínios industriais complexos.
2. **Contribuição para a Indústria de O&G (Prática):** Fornece o primeiro estudo rigoroso sobre o que agentes de IA podem (e, crucialmente, *não podem*) fazer com segurança na engenharia de poços. Isso desbloqueia ganhos de eficiência (em "picos") e previne falhas catastróficas (em "vales").
3. **Originalidade:** A intersecção de Agentes LLM, a teoria da "Jagged Frontier" e o domínio de O&G *onshore/offshore* é inteiramente nova na literatura.

### 5. Fundamentação Teórica

A tese será fundamentada em quatro pilares:

1. **Agentes Baseados em LLM:** Arquiteturas e paradigmas (RAG, ReAct, CoT, Multi-Agentes). Como eles funcionam, planejam e usam ferramentas.
2. **Avaliação de Agentes (Benchmarking):** Estado da arte (ex: AgentBench, GAIA, MT-Bench). Análise de suas limitações para tarefas industriais/engenharia.
3. **Produtividade e Limites da IA:** O *paper* seminal de Brynjolfsson, Mollick, et al. (2023) sobre a "Fronteira Irregular".
4. **Engenharia de Poços e IA:** Aplicações atuais de machine learning em O&G e a lacuna existente na aplicação de *agentes generativos* para atividades diversas do setor.

### 6. Metodologia Proposta

Este projeto empregará uma **metodologia de pesquisa experimental quantitativa e qualitativa**, dividida em quatro fases:

**Fase 1: Definição do Domínio e Taxonomia de Tarefas (OE1)**

* **Fonte de Dados:** Análise documental de Normas Técnicas, Padrões Operacionais, Relatórios de Situação Operacional, Lições Aprendidas, Alertas Técnicos e Relatórios Diários de Perfuração (DDRs/Boletins Diários de Operação - BDOs).
* **Amostragem:** Criação de um *dataset* de 50-100 tarefas representativas.
* **Classificação (Taxonomia):** As tarefas serão classificadas por eixos:
  * [EXEMPLOS HIPOTETICOS] *Tipo de Ação:* Extração de Informação, Síntese, Diagnóstico, Planejamento, Verificação de Conformidade.
  * [EXEMPLOS HIPOTETICOS] *Domínio de Conhecimento:* Geologia, Fluidos, Mecânica, Regulação.
  * [EXEMPLOS HIPOTETICOS] *Complexidade:* Nível de raciocínio causal, temporal e espacial exigido.

**Fase 2: Design do Benchmark Experimental (OE2)**

* **Plataforma:** Desenvolvimento de um ambiente de teste (sandbox) onde os agentes podem atuar.
* **Ferramentas (Tools):** Disponibilização de "ferramentas" simuladas para os agentes (ex: `buscar_norma_api(id)`, `calcular_volume_anular(diametros)`, `ler_ultimo_ddr()`).
* **Ground Truth:** Definição de critérios de sucesso (o "gabarito") para cada tarefa, validado por Especialistas no Domínio (SMEs - *Subject Matter Experts*).

**Fase 3: Execução Experimental (OE3)**

* **Variáveis Independentes:** Arquitetura do Agente (Ex: Baseline GPT-4o, RAG c/ base de POPs, Agente ReAct).
* **Variáveis Dependentes (Métricas):**
  1. *Taxa de Sucesso Binário:* Completou a tarefa com sucesso?
  2. *Qualidade da Resposta:* Avaliação cega (1-5) por SMEs.
  3. *Eficiência:* Custo (tokens), passos de raciocínio.
  4. *Robustez:* O agente "alucina" ou falha graciosamente?

**Fase 4: Análise e Mapeamento da Fronteira (OE4, OE5)**

* **Análise Quantitativa:** Correlação estatística entre as *características da tarefa* (da Fase 1) e as *métricas de desempenho* (da Fase 3).
* **Análise Qualitativa:** Análise de causa-raiz das falhas ("vales"). O agente falhou por falta de conhecimento (RAG falho), raciocínio (LLM falho) ou planejamento (arquitetura falha)?
* **Resultado:** O "mapa" da fronteira e o *framework* de decisão.

### 7. Cronograma Preliminar (48 meses)

* **Ano 1 (Meses 1-12):**
  * Revisão de Literatura aprofundada.
  * Disciplinas obrigatórias.
  * Execução da Fase 1 (Taxonomia de Tarefas).
  * Definição do projeto de tese (Exame de Qualificação).
* **Ano 2 (Meses 13-24):**
  * Execução da Fase 2 (Desenvolvimento do Benchmark).
  * Testes-piloto.
  * Artigo de revisão ou *position paper* sobre o *benchmark*.
* **Ano 3 (Meses 25-36):**
  * Execução da Fase 3 (Bateria principal de testes e avaliação).
  * Coleta de dados (avaliação pelos SMEs).
  * Início da Fase 4 (Análise).
  * Submissão de artigo para conferência principal (ex: NeurIPS, ICML, ou conferência de O&G como a OTC).
* **Ano 4 (Meses 37-48):**
  * Conclusão da Fase 4 (Desenvolvimento do Framework).
  * Redação da Tese.
  * Submissão de artigo em periódico.
  * Defesa.

### 8. Referências Bibliográficas Preliminares

* Mollick, E., & Brynjolfsson, E., et al. (2023). *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*. HBS Working Paper.
* Yao, S., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*.
* Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
* Zeng, Y., et al. (2024). *AgentBench: Evaluating LLMs as Agents*.
* ... (Outros sobre IA em O&G e metodologias de avaliação de LLMs)
