"""Teste de mutação manual: planta cada erro da pergunta 3 e verifica se a suíte de testes falha."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).parent
MUTACOES = {
    "1. big-M fixo em 100": ("(d.horas_mes / d.horas_por_t[k]) * m.y[k]", "100 * m.y[k]"),
    "2. não confere o status": ("    if status != pyo.TerminationCondition.optimal:\n        raise RuntimeError(f\"modelo sem solução ótima: {status}\")\n", ""),
    "3. sem sense=maximize": ("        sense=pyo.maximize,\n", ""),
    "4. rendimento multiplica": ("/ d.rendimento[produto]", "* d.rendimento[produto]"),
    "5. troca com <=": ("m.w >= m.y[\"P\"] + m.y[\"Q\"] - 1", "m.w <= m.y[\"P\"] + m.y[\"Q\"] - 1"),
}

original = (AQUI / "caso5_modelo.py").read_text()
for nome, (antes, depois) in MUTACOES.items():
    assert antes in original, nome
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "caso5_modelo.py").write_text(original.replace(antes, depois))
        resultado = {}
        for suite in ("test_caso5_modelo.py", "test_caso5_ingenuo.py"):
            shutil.copy(AQUI / suite, tmp)
            r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", suite],
                               capture_output=True, text=True, cwd=tmp)
            quebrados = [linha.split("::")[1].split(" ")[0] for linha in r.stdout.splitlines()
                         if linha.startswith(("FAILED", "ERROR"))]
            resultado[suite] = ("PEGO" if r.returncode != 0 else "ESCAPOU", quebrados)
        completo, ingenuo = resultado["test_caso5_modelo.py"], resultado["test_caso5_ingenuo.py"]
        print(f"{nome:26s} | suíte completa: {completo[0]:7s} ({len(completo[1]):2d} testes) | suíte ingênua: {ingenuo[0]}")
