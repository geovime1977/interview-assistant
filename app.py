"""
Interview Assistant — Tradução e preparação de respostas em tempo real.
Usa Web Speech API (browser) para captura de voz e GPT-4o para tradução + resposta.
"""

import json
import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """Você é um assistente de entrevista para Geovane, profissional de dados com experiência em analytics, machine learning e pesquisa operacional.

Quando receber uma pergunta de entrevista (em qualquer idioma), responda EXATAMENTE neste formato:

🇧🇷 PERGUNTA
[pergunta traduzida para português, ou original se já estiver em PT]

🇺🇸 QUESTION
[pergunta traduzida para inglês, ou original se já estiver em EN]

━━━━━━━━━━━━━━━━━━━━

🇧🇷 RESPOSTA
[resposta profissional em português, 2-3 parágrafos, primeira pessoa]

🇺🇸 ANSWER
[resposta profissional em inglês, 2-3 parágrafos, primeira pessoa]

Perfil de Geovane (use como contexto, não force em toda resposta):
- Data Scientist com experiência em analytics, ML e otimização
- Python, PySpark, SQL, scikit-learn, OR-Tools
- MBA em Pesquisa Operacional e Finanças Corporativas

Regras:
- Responda sobre o assunto exato da pergunta — não redirecione para OR ou logística a não ser que a pergunta seja sobre isso
- Perguntas de apresentação ("tell me about yourself"): fale sobre trajetória profissional em dados de forma geral
- Perguntas comportamentais: use o método STAR (Situação, Tarefa, Ação, Resultado) com exemplos de projetos de dados
- Perguntas técnicas: responda tecnicamente sobre o tema perguntado (SQL, Python, ML, estatística, etc.)
- Perguntas sobre motivação/cultura: responda de forma genuína e profissional
- Tom: confiante, direto, 2-3 parágrafos por resposta
- Nunca mencione nomes de empresas específicas"""


@app.get("/", response_class=HTMLResponse)
async def index():
    return Path("templates/index.html").read_text(encoding="utf-8")


@app.post("/stream")
async def stream(request: Request):
    data = await request.json()
    question = data.get("question", "").strip()
    if not question:
        return {"error": "pergunta vazia"}

    def generate():
        try:
            with client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question},
                ],
                stream=True,
                temperature=0.6,
                max_tokens=1200,
            ) as stream_response:
                for chunk in stream_response:
                    delta = chunk.choices[0].delta.content
                    if delta:
                        yield f"data: {json.dumps({'text': delta})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
