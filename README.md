# Interview Assistant

Assistente de entrevista em tempo real com tradução simultânea e preparação de respostas via GPT-4o. Captura voz pelo navegador (Web Speech API), traduz a pergunta e gera resposta profissional em português e inglês.

## Funcionalidades

- Captura de voz por navegador (Web Speech API)
- Tradução simultânea da pergunta (qualquer idioma → PT + EN)
- Resposta profissional em 2-3 parágrafos (STAR para comportamentais)
- Streaming da resposta em tempo real
- Perfil contextualizado para dados/analytics

## Stack

Python · FastAPI · OpenAI GPT-4o · Uvicorn · Web Speech API

## Setup

```bash
git clone https://github.com/geovime1977/interview-assistant.git
cd interview-assistant
uv venv && uv pip install -r requirements.txt
export IA_PROVIDER=openai
export OPENAI_API_KEY=sk-...
```

## Como rodar

```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8001
```

Acesse http://localhost:8001.

## Licença

MIT
