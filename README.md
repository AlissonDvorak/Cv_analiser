# 🤖 Currículo IA — Análise Inteligente de Currículos com LLMs

  

Este projeto realiza a **análise automatizada de currículos em PDF**, utilizando **Large Language Models (LLMs)** para extrair informações, gerar resumos, atribuir pontuações e emitir pareceres críticos sobre a aderência de candidatos a vagas específicas.

  

## ✨ Funcionalidades

  

- 📄 Leitura e extração de conteúdo de currículos em PDF

- 🧠 Resumo inteligente do currículo em Markdown com LLM (Groq + LLaMA)

- 📝 Análise crítica sobre a compatibilidade com a vaga

- 📊 Geração de pontuação baseada em critérios objetivos (experiência, educação, idiomas, etc)

- 📁 Armazenamento de dados estruturados em MongoDB

- 💬 Opinião profissional simulando um recrutador sênior

  

---

  

## 🛠️ Tecnologias Utilizadas

  

- 🐍 **Python 3.11+**

- 🤖 **[Groq API](https://console.groq.com)** com `meta-llama/llama-4-scout-17b-16e-instruct`

- 🧠 **LangChain**

- 📦 **MongoDB** para persistência dos dados

- 📄 **PyMuPDF (fitz)** para leitura de PDFs

- 🧬 **Pydantic** para schemas e validação de dados

- 🛜 **dotenv** para gerenciamento de variáveis de ambiente

  

---

  

## 📂 Estrutura do Projeto

  

📁 models/

│ ├── resum.py # Schema do resumo do currículo

│ ├── analysis.py # Schema da análise

│ └── file.py # Metadata do arquivo PDF

📁 helpers/

│ └── helper.py # Funções de extração e leitura de PDF

📁 ai/

│ └── groq_client.py # Cliente de comunicação com o LLM da Groq

📄 analise.py # Script principal de execução

📄 .env # Variáveis de ambiente (Groq API Key etc)

  
  
  

## 🚀 Como Executar

  

1.  **Clone o repositório**:

```bash

git  clone  https://github.com/seu-usuario/curriculo-ia.git

cd  curriculo-ia

```

  

2.  **Crie e ative um ambiente virtual:**

  

```bash

python  -m  venv  venv

source  venv/bin/activate  # Linux/macOS

venv\Scripts\activate  # Windows

Instale  as  dependências:

```

  

3.  **Configure o .env:**

```bash

pip  install  -r  requirements.txt

Configure  o  .env:

```

  

4.  **adicione sua key groq**

```bash

GROQ_API_KEY=your_api_key_here

Adicione  currículos  em  PDF  na  pasta  curriculos/.

```

5.  **Execute os scripts**

  

```bash

 1.  preencha  os  dados  da  vaga  em  create_job.py

	- execute  o  script  python  create_job.py

 1.  execute  o  script  analise.py

 2.  streamlit  run  app.py

```

  

🧠 Exemplo de Output

Resumo em Markdown (gerado automaticamente):

  

```bash

markdown

## Nome Completo

João  da  Silva


## Experiência

Desenvolvedor  Python  na  Empresa  X


## Habilidades

Python,  Git,  SQL


## Educação

Ciência  da  Computação  -  UFPR

  
## Idiomas

Inglês  Avançado

Opinião  Crítica:

  

O  candidato  demonstra  sólida  base  em  Python,  mas  não  possui  experiência  prévia  com  frameworks  web,  o  que  pode  limitar  sua  performance  inicial...

  

Pontuação  Final:  7.9

```

  

```bash

Pontuação  Final:  8.5

```