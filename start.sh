#!/bin/bash
# IA: opção 1 OpenAI (se OPENAI_API_KEY no .env ou no ambiente), opção 2 Claude CLI (login do Claude Code, sem chave).
# Forçar só Claude: IA_PROVIDER=claude-cli ./start.sh
cd "$(dirname "$0")"
[ -f .env ] && { set -a; . ./.env; set +a; }
exec .venv/bin/uvicorn app:app --host 127.0.0.1 --port 8001
