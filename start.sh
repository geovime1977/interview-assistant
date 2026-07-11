#!/bin/bash
cd "$(dirname "$0")"
OPENAI_API_KEY="$OPENAI_API_KEY" venv/bin/uvicorn app:app --host 127.0.0.1 --port 7860 --reload
