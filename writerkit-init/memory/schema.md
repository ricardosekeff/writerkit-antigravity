# Módulo de Memória e Estado

O arquivo de memória (ex: `memory.json`) deve ser mantido e atualizado constantemente pelas *skills*.

## Estrutura de Metadados do Projeto
* **`title`**: Título da obra.
* **`theme`**: Tema central e escopo.
* **`language`**: Idioma da obra (ex: pt-BR).
* **`depth`**: Nível de profundidade (Graduação, Mestrado, Técnico).
* **`rigor`**: Nível de formalismo matemático/teórico.
* **`tone`**: Personalidade do texto (Formal, Professoral, Crítico).
* **`code_style`**: Linguagem e guia de estilo de código.
* **`visual_style`**: Padrão para imagens e diagramas (ex: TikZ, preto e branco).
* **`latex_template`**: Referências aos arquivos `.tex`, `.cls` e `.sty` utilizados.

## Logs e Controle
* **`chapters`**: Status e metadados de cada capítulo.
* **`decision_log`**: Histórico temporal (timestamps) de todas as decisões tomadas.
