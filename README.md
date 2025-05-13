# 🧠 Flask API com DeepSeek-R1 via Ollama

Esta é uma API desenvolvida com Flask em Python, conectando-se ao modelo LLM **DeepSeek-R1** utilizando a plataforma [Ollama](https://ollama.com/).  
Ela permite realizar inferências com LLMs de forma simples, eficiente e local com uma UI básica e retorno stream de resposta.

## ⚙️ Pré-requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes itens instalados:

- [Python 3.8+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/)
- `deepseek-r1` baixado no Ollama

## 🚀 Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/jocimarlopes/ollama-llm-deepseek-server.git
cd ollama-llm-deepseek-server
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Instale e inicie o Ollama**
Se ainda não tiver o Ollama:
```bash
# No Linux via curl
curl -fsSL https://ollama.com/install.sh | sh
```

4. **Baixe o modelo DeepSeek-R1**
Se ainda não tiver o Ollama:
```bash
ollama pull deepseek-r1:latest
```

## 🧪 Executando a API

Basta rodar o script app.py:

```bash
python app.py
```

## 📁 Estrutura básica

Basta rodar o script app.py:

```bash
├── app.py
├── requirements.txt
└── README.md
```

## 👤 Créditos
Projeto desenvolvido por Jocimar Lopes.
Sinta-se à vontade para contribuir ou utilizar em seus próprios projetos.

## 📄 Licença
Este projeto está licenciado sob os termos da MIT License.
