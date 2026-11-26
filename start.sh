#!/bin/bash
# Padrão: OpenAI. Claude Code CLI é usado como fallback quando a API da OpenAI falha.
cd "$(dirname "$0")"
.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8001
