"""
Interview Assistant — Tradução e preparação de respostas em tempo real.
Usa Web Speech API (browser) para captura de voz e GPT-4o para tradução + resposta.
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from openai import OpenAI

app = FastAPI()
# claude-cli: usa o login do Claude Code (sem chave de API). openai: exige OPENAI_API_KEY com créditos.
PROVEDOR = os.getenv("IA_PROVIDER", "claude-cli")
MODELO_CLAUDE = os.getenv("IA_CLAUDE_MODEL", "haiku")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if PROVEDOR == "openai" else None

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


def claude_stream(sistema: str, texto: str):
    """Chama `claude -p` sem ferramentas, hooks, MCP nem sessão salva e repassa o texto em eventos SSE."""
    cmd = ["claude", "-p", "--tools", "", "--disable-slash-commands", "--no-session-persistence",
           "--setting-sources", "", "--strict-mcp-config", "--system-prompt", sistema,
           "--model", MODELO_CLAUDE, "--output-format", "stream-json", "--include-partial-messages", "--verbose"]
    try:
        with tempfile.TemporaryDirectory() as cwd:
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True, cwd=cwd)
            proc.stdin.write(texto)
            proc.stdin.close()
            for linha in proc.stdout:
                try:
                    ev = json.loads(linha)
                except json.JSONDecodeError:
                    continue
                if ev.get("type") == "stream_event":
                    delta = ev.get("event", {}).get("delta", {})
                    if delta.get("type") == "text_delta":
                        yield f"data: {json.dumps({'text': delta['text']})}\n\n"
                elif ev.get("type") == "result" and ev.get("is_error"):
                    yield f"data: {json.dumps({'error': str(ev.get('result'))})}\n\n"
            proc.wait(timeout=120)
            if proc.returncode:
                yield f"data: {json.dumps({'error': proc.stderr.read()[:300]})}\n\n"
        yield "data: [DONE]\n\n"
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        yield f"data: {json.dumps({'error': f'claude CLI: {e}'})}\n\n"


TRADUTOR = """Você é um intérprete. Traduza o texto recebido de {de} para {para}, com fidelidade ao sentido.
Regras:
- Devolva somente a tradução, sem aspas, sem comentários, sem notas.
- Não responda perguntas contidas no texto e não acrescente informação: só traduza.
- O texto veio de reconhecimento de voz e pode ter palavras erradas; corrija pelo contexto, sem inventar conteúdo.
{extra}"""

EXTRA_EN = ("- O resultado será lido em voz alta numa videochamada por um falante de português com inglês intermediário: "
            "use frases curtas, vocabulário comum e ordem direta, mantendo o tom profissional.")


@app.get("/tradutor", response_class=HTMLResponse)
async def tradutor():
    return Path("templates/tradutor.html").read_text(encoding="utf-8")


@app.post("/traduzir")
async def traduzir(request: Request):
    data = await request.json()
    texto = data.get("texto", "").strip()
    para = data.get("para", "pt")
    if not texto:
        return {"error": "texto vazio"}
    sistema = TRADUTOR.format(de="inglês" if para == "pt" else "português", para="português do Brasil" if para == "pt" else "inglês",
                              extra="" if para == "pt" else EXTRA_EN)
    return StreamingResponse(claude_stream(sistema, texto), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


@app.get("/", response_class=HTMLResponse)
async def index():
    return Path("templates/index.html").read_text(encoding="utf-8")


@app.post("/stream")
async def stream(request: Request):
    data = await request.json()
    question = data.get("question", "").strip()
    if not question:
        return {"error": "pergunta vazia"}

    def generate_claude():
        yield from claude_stream(SYSTEM_PROMPT, question)

    def generate():
        if PROVEDOR != "openai":
            yield from generate_claude()
            return
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
