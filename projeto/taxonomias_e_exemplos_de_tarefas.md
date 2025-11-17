## Taxonomia de Tarefas

### Análise Temporal

* Como foi o teste de pressão após a 2a operação de cimentação durante a perfuração do poço X
  * Raciocínio: é necessário encontrar as operações de cimentação, localizar a 2a, ler os respectivos DDRs e indicar como foi o teste de pressão.
* Foram realizadas operações de circulação ou condicionamento do poço X entre o término da perfuração da fase de 16 1/2" e a retirada?
  * Raciocínio: é necessário localizar o término da perfuração da fase de 16 1/2", localizar o fim da retirada e aferir se houve condicionamento no período.

### Análise Comparativa

* Analise todas as perfurações realizadas em 2024 e responda, para cada uma, se houve ou não retorno de traçador durante a cimentação do revestimento de superfície. [exemplo peralta]
  * Raciocínio: é necessário, para cada uma das ~30 intervenções, encontrar a operação em questão, ler os respectivos DDRs e indicar se houve ou não retorno do traçador.
* Para uma nova recomendação X (de um novo Item de Conhecimento - IC), faça um crosscheck com Normas Petrobras, Padrões e ICs indicando itens relacionados (similaridades, conflitos, etc). Determine se cada item encontrado corrobora ou conflita com a nova recomendação.
  * Raciocínio: necessário realizar busca semântica em 3 KBs distintas. Acumular todos os itens encontrados e solicitar análise (LLM) com corroborações e conflitos.

### Pesquisa Profunda

* Faça uma ***pesquisa profunda*** sobre todas as operações ocorridas em todas as sondas marítimas na semana do dia 09/11/2025 a 15/11/2025.
  * Raciocínio sugerido: agente deve consultar e concatenar: sitops, T&O, Anormalidades, RTO-Live (gráficos), Incidentes. Em seguida, gerar relatório por sonda. Por fim, gerar relatório geral.
* Faça uma ***investigação*** da falha ocorrida na cimentação do revestimento de superfície do poço X.
  * O agente deve encontrar em T&O ou Anormalidades a data da falha, em seguida busca relatórios de D-3 a D+7 em: sitops, T&O, Anormalidades, RTO-Live (gráficos), Incidentes. Por fim, gerar um relatório com os achados.
* Faça um relatório com ***recomendações operacionais*** levando em consideração as próximas operações previstas na NS-48.
  * O agente deve consultar o último SITOP da sonda em questão, extrair a lista de próximas operações. Em seguida, deve consultar os diversos sistemas em busca de recomendações para as operações listadas: Lessons, Padrões, Normas e Anormalidades. Por fim, gerar um relatório com todas as recomendações operacionais relevantes para cada operação.
