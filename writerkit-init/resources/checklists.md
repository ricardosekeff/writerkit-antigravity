# Padrão de Checklist para Produção de Capítulos

Durante as etapas de **Review** e **Validation**, o agente deve percorrer rigorosamente o checklist abaixo e registrar o resultado na memória.

## 1. Technical Accuracy (Precisão Técnica)
- [ ] Os exemplos de código foram validados externamente e estão corretos?
- [ ] As explicações conceituais estão em conformidade com o estado da arte e o rigor matemático exigido?
- [ ] O uso de APIs/Bibliotecas nos exemplos condiz com a versão mais recente/estável suportada pelo projeto?

## 2. Consistency (Consistência)
- [ ] A terminologia técnica é uniforme ao longo de todo o capítulo e consistente com os capítulos anteriores?
- [ ] O estilo de formatação do código (identação, convenção de nomes) segue o `code_style` definido na memória?
- [ ] O mapeamento de acentuação (literate) no LaTeX está implementado corretamente nos blocos de código?

## 3. Readability (Legibilidade e Fluidez)
- [ ] O texto possui cadência lógica (introdução, desenvolvimento, conclusão parcial) sem saltos bruscos?
- [ ] A linguagem está adequada ao tom estabelecido na memória?
- [ ] Os parágrafos são coesos e evitam jargões desnecessários quando não explicados previamente?

## 4. Completeness (Completude)
- [ ] Os pré-requisitos lógicos para a compreensão do capítulo foram declarados?
- [ ] Os objetivos de aprendizagem traçados na fase de *Planning* foram integralmente alcançados?
- [ ] Há uma seção de fechamento/resumo que consolida o conhecimento adquirido?

## 5. Cross-references (Referências e Navegação)
- [ ] Todos os *labels* e *refs* internos (imagens, tabelas, algoritmos) foram validados e não apontam para locais nulos?
- [ ] Todas as citações bibliográficas (\cite) correspondem a uma entrada válida no arquivo BibTeX?
- [ ] **Validação Externa:** Todas as referências bibliográficas foram verificadas com sucesso em bases acadêmicas (Google Scholar, ScienceDirect, IEEE, etc.)?
