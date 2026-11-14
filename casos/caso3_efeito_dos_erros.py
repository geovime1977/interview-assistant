import pyomo.environ as pyo

import caso3_codigo_com_erros as e

ERROS = ["sentido", "rendimento", "bigM", "troca"]


def montar(com_erros):
    rend = (lambda k: e.RENDIMENTO[k]) if "rendimento" in com_erros else (lambda k: 1 / e.RENDIMENTO[k])
    cons = lambda k, s: e.REACOES[k].get(s, 0) * e.MM[s] / e.MM[k] * rend(k)
    m = pyo.ConcreteModel()
    m.x = pyo.Var(["P", "Q"], domain=pyo.NonNegativeReals)
    m.c = pyo.Var(["A", "B", "C"], domain=pyo.NonNegativeReals)
    m.y = pyo.Var(["P", "Q"], domain=pyo.Binary)
    m.w = pyo.Var(domain=pyo.Binary)
    sentido = pyo.minimize if "sentido" in com_erros else pyo.maximize
    m.margem = pyo.Objective(expr=sum(e.PRECO_VENDA[k] * m.x[k] for k in "PQ") - sum(e.PRECO_COMPRA[s] * m.c[s] for s in "ABC"), sense=sentido)
    m.balanco = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] >= sum(cons(k, s) * m.x[k] for k in "PQ"))
    m.estoque = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] <= e.DISPONIVEL[s])
    m.contrato = pyo.Constraint(expr=m.x["Q"] >= 200)
    m.venda_P = pyo.Constraint(expr=m.x["P"] <= 250)
    m.reator = pyo.Constraint(expr=sum(e.HORAS_POR_T[k] * m.x[k] for k in "PQ") + 8 * m.w <= 720)
    M = (lambda k: 100) if "bigM" in com_erros else (lambda k: 720 / e.HORAS_POR_T[k])
    m.liga = pyo.Constraint(["P", "Q"], rule=lambda m, k: m.x[k] <= M(k) * m.y[k])
    if "troca" in com_erros:
        m.troca = pyo.Constraint(expr=m.w <= m.y["P"] + m.y["Q"] - 1)
    else:
        m.troca = pyo.Constraint(expr=m.w >= m.y["P"] + m.y["Q"] - 1)
    r = pyo.SolverFactory("appsi_highs").solve(m, load_solutions=False)
    st = str(r.solver.termination_condition)
    if len(r.solution) == 0:
        return st, None
    m.solutions.load_from(r)
    v = pyo.value
    # margem verdadeira: recalculada com o consumo correto, para medir o estrago real
    real = sum(e.PRECO_VENDA[k] * v(m.x[k]) for k in "PQ") - sum(
        e.PRECO_COMPRA[s] * sum(e.REACOES[k].get(s, 0) * e.MM[s] / e.MM[k] / e.RENDIMENTO[k] * v(m.x[k]) for k in "PQ") for s in "ABC")
    horas = sum(e.HORAS_POR_T[k] * v(m.x[k]) for k in "PQ") + (8 if v(m.y["P"]) > .5 and v(m.y["Q"]) > .5 else 0)
    return st, dict(P=round(v(m.x["P"]), 1), Q=round(v(m.x["Q"]), 1), w=round(v(m.w)), declarada=round(v(m.margem)), verdadeira=round(real), horas_reais=round(horas, 1))


print("corrigido   ", montar(set()))
for erro in ERROS:
    print(f"{erro:12s}", montar({erro}))
print("todos       ", montar(set(ERROS)))
