# 🚀 WriterKit: Engenharia Editorial para Livros Técnicos em LaTeX

**WriterKit** é um framework avançado de orquestração editorial projetado para o **Gemini CLI** e ecossistemas **Antigravity**. Ele transforma agentes de IA em engenheiros editoriais capazes de produzir livros científicos e técnicos com rigor acadêmico, fidelidade visual e compatibilidade total com LaTeX (TexPage/Overleaf).

Diferente de geradores de texto genéricos, o WriterKit é governado por um sistema de **Aderência Estrita**, garantindo que a IA nunca invente comandos, cores ou ambientes que não pertençam ao seu template original.

---

## 🌟 Diferenciais Críticos

### 🎯 Zero Hallucination (Strict Template Adherence)
O agente realiza um mapeamento exaustivo dos seus arquivos `.cls` e `.sty`. Ele utiliza **exclusivamente** os comandos e ambientes (`environments`) mapeados, impedindo a criação de macros inexistentes que quebrariam a compilação.

### 🎨 Strict Color Adherence
Fidelidade total à identidade visual. O WriterKit mapeia o esquema de cores oficial do projeto e proíbe o uso de cores extrínsecas. Qualquer exceção exige aprovação manual do usuário e, se negada, o sistema nunca mais sugerirá tal alteração.

### 📊 TikZ Intelligent Design
Regras nativas de geometria para diagramas:
- **Text Containment:** Ajuste automático de texto em formas para evitar extrapolação de bordas.
- **Overlap Prevention:** Rótulos e conexões são posicionados dinamicamente para nunca sobrepor elementos do diagrama.
- **Visual Balance:** Centralização horizontal obrigatória e grids inteligentes para múltiplas imagens.

---

## 📂 Estrutura do Projeto (Scaffolding)

Ao inicializar um projeto, o WriterKit organiza o ambiente seguindo este padrão:

```text
.
├── main.tex           # Arquivo mestre (orquestrador)
├── chapters/          # Conteúdo textual (.tex) por capítulo
├── codes/             # Algoritmos e snippets organizados por capítulo
├── images/            # Diagramas TikZ e figuras (.png, .svg, .tikz)
├── configs/           # Seus arquivos de estilo (.cls, .sty)
├── memory/            # memory.json (O "Cérebro" persistente do projeto)
└── output/            # Pacote final consolidado para publicação
```

---

## 🛠 O Pipeline de Produção

1.  **`writerkit-init`**: Prepara a infraestrutura física e pastas.
2.  **`writerkit-setup`**: Mapeia o "DNA" (comandos e cores) do template.
3.  **`writerkit-planning`**: Estrutura a pedagogia e o blueprint do capítulo.
4.  **`drafting-content`**: Redige a prosa técnica (Tom Professoral).
5.  **`developing-code`**: Implementa algoritmos com mapeamento `literate` (acentuação).
6.  **`integrating-assets`**: Gera os TikZ e consolida os inputs no capítulo.
7.  **`validating-references`**: Valida citações e bibliografia.
8.  **`revising-clarity`**: Refina o rigor científico e fluidez.
9.  **`publishing-book`**: Gera o pacote final pronto para o prelo.

---

## 📥 Instalação

Para utilizar o WriterKit no seu ambiente **Gemini CLI** ou **Antigravity**:

1.  Navegue até o diretório de skills do seu agente:
    ```bash
    cd ~/.gemini/antigravity/skills/
    ```
2.  Clone este repositório:
    ```bash
    git clone https://github.com/ricardosekeff/writerkit.git
    ```
3.  Reinicie sua sessão do Gemini CLI para que as novas skills sejam carregadas.

---

## 🚀 Como Iniciar seu Primeiro Livro

Siga esta sequência de comandos para garantir que o framework opere com máxima eficiência:

### Passo 1: Inicialização do Canteiro de Obras
No diretório onde deseja criar o livro, execute:
> *"Ative a skill **writerkit-init** para preparar a estrutura deste novo livro."*

### Passo 2: Configuração Editorial
Coloque seus arquivos de template (`.cls`, `.sty`) na pasta `/configs` e diga:
> *"Ative a skill **writerkit-setup** para mapear meu template, cores e definir o tom de escrita."*

### Passo 3: Planejamento do Capítulo
Com a infraestrutura pronta, inicie a criação:
> *"Ative a skill **writerkit-planning** para estruturarmos o primeiro capítulo."*

---

## ⚖️ Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes. Em suma: você é livre para usar, modificar e distribuir, desde que mantenha os créditos originais.

---

## ✍️ Autor

Desenvolvido por **Ricardo Sekeff**.

---

# 🚀 WriterKit: Editorial Engineering for Technical Books in LaTeX

**WriterKit** is an advanced editorial orchestration framework designed for the **Gemini CLI** and **Antigravity** ecosystems. It transforms AI agents into editorial engineers capable of producing scientific and technical books with academic rigor, visual fidelity, and full compatibility with LaTeX (TexPage/Overleaf).

Unlike generic text generators, WriterKit is governed by a **Strict Adherence** system, ensuring that the AI never invents commands, colors, or environments that do not belong to its original template.

---

## 🌟 Key Differentials

### 🎯 Zero Hallucination (Strict Template Adherence)
The agent performs an exhaustive mapping of your `.cls` and `.sty` files. It uses **exclusively** the mapped commands and environments, preventing the creation of non-existent macros that would break compilation.

### 🎨 Strict Color Adherence
Full fidelity to the visual identity. WriterKit maps the project's official color scheme and forbids the use of extraneous colors. Any exception requires manual user approval, and if denied, the system will never suggest such changes again.

### 📊 TikZ Intelligent Design
Native geometry rules for diagrams:
- **Text Containment:** Automatic adjustment of text within shapes to prevent overflow.
- **Overlap Prevention:** Labels and connections are dynamically positioned to avoid overlapping diagram elements.
- **Visual Balance:** Mandatory horizontal centering and intelligent grids for multiple images.

---

## 📂 Project Structure (Scaffolding)

When initializing a project, WriterKit organizes the environment as follows:

```text
.
├── main.tex           # Master file (orchestrator)
├── chapters/          # Textual content (.tex) per chapter
├── codes/             # Algorithms and snippets organized by chapter
├── images/            # TikZ diagrams and figures (.png, .svg, .tikz)
├── configs/           # Style files (.cls, .sty)
├── memory/            # memory.json (project's persistent "brain")
└── output/            # Final consolidated package for publishing
```

---

## 🛠 Production Pipeline

1.  **`writerkit-init`**: Prepares the physical infrastructure and folders.
2.  **`writerkit-setup`**: Maps the template “DNA” (commands and colors).
3.  **`writerkit-planning`**: Structures pedagogy and chapter blueprint.
4.  **`drafting-content`**: Writes technical prose (professorial tone).
5.  **`developing-code`**: Implements algorithms with `literate` mapping (accent support).
6.  **`integrating-assets`**: Generates TikZ and consolidates chapter inputs.
7.  **`validating-references`**: Validates citations and bibliography.
8.  **`revising-clarity`**: Refines scientific rigor and fluency.
9.  **`publishing-book`**: Generates the final publication-ready package.

---

## 📥 Installation

To use WriterKit in your **Gemini CLI** or **Antigravity** environment:

1. Navigate to your agent’s skills directory:
    ```bash
    cd ~/.gemini/antigravity/skills/
    ```
2. Clone this repository:
    ```bash
    git clone https://github.com/ricardosekeff/writerkit.git
    ```
3. Restart your Gemini CLI session to load the new skills.

---

## 🚀 Getting Started with Your First Book

Follow this sequence to ensure optimal framework operation:

### Step 1: Initialize the Workspace
In your desired project directory, run:
> *"Activate the **writerkit-init** skill to prepare the structure of this new book."*

### Step 2: Editorial Setup
Place your template files (`.cls`, `.sty`) in `/configs` and run:
> *"Activate the **writerkit-setup** skill to map my template, colors, and define the writing tone."*

### Step 3: Chapter Planning
With the infrastructure ready:
> *"Activate the **writerkit-planning** skill to structure the first chapter."*

---

## ⚖️ License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details. In short: you are free to use, modify, and distribute it, provided that you retain the original credits.

---

## ✍️ Author

Developed by **Ricardo Sekeff**.

