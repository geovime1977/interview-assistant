#!/bin/bash
# Padrão: Claude CLI (login do Claude Code, sem chave). Para usar OpenAI: IA_PROVIDER=openai OPENAI_API_KEY=... ./start.sh
cd "$(dirname "$0")"
.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8001
