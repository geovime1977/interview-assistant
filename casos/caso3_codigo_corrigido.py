import pyomo.environ as pyo

MM = {"A": 40, "B": 10, "C": 20, "P": 60, "Q": 60}
REACOES = {"P": {"A": 1, "B": 2}, "Q": {"A": 1, "C": 1}}
RENDIMENTO = {"P": 0.90, "Q": 0.95}
PRECO_VENDA = {"P": 5000, "Q": 3000}
PRECO_COMPRA = {"A": 1500, "B": 2000, "C": 1000}
DISPONIVEL = {"A": 500, "B": 200, "C": 300}
HORAS_POR_T = {"P": 1.5, "Q": 1.0}
HORAS_MES = 720
HORAS_LIMPEZA = 8
CONTRATO_Q = 200
VENDA_MAX_P = 250


def consumo(produto, insumo):
    """t de insumo por t de produto: razão mássica da estequiometria dividida pelo rendimento."""
    coef = REACOES[produto].get(insumo, 0)
    return coef * MM[insumo] / MM[produto] / RENDIMENTO[produto]


def montar():
    m = pyo.ConcreteModel()
    m.x = pyo.Var(["P", "Q"], domain=pyo.NonNegativeReals)
    m.c = pyo.Var(["A", "B", "C"], domain=pyo.NonNegativeReals)
    m.y = pyo.Var(["P", "Q"], domain=pyo.Binary)
    m.w = pyo.Var(domain=pyo.Binary)

    m.margem = pyo.Objective(
        expr=sum(PRECO_VENDA[k] * m.x[k] for k in "PQ") - sum(PRECO_COMPRA[s] * m.c[s] for s in "ABC"),
        sense=pyo.maximize,
    )
    m.balanco = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] >= sum(consumo(k, s) * m.x[k] for k in "PQ"))
    m.disponibilidade = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] <= DISPONIVEL[s])
    m.contrato = pyo.Constraint(expr=m.x["Q"] >= CONTRATO_Q)
    m.venda_P = pyo.Constraint(expr=m.x["P"] <= VENDA_MAX_P)
    m.reator = pyo.Constraint(expr=sum(HORAS_POR_T[k] * m.x[k] for k in "PQ") + HORAS_LIMPEZA * m.w <= HORAS_MES)
    m.liga = pyo.Constraint(["P", "Q"], rule=lambda m, k: m.x[k] <= (HORAS_MES / HORAS_POR_T[k]) * m.y[k])
    m.troca = pyo.Constraint(expr=m.w >= m.y["P"] + m.y["Q"] - 1)
    return m


def resolver():
    m = montar()
    resultado = pyo.SolverFactory("appsi_highs").solve(m, load_solutions=False)
    status = resultado.solver.termination_condition
    if status != pyo.TerminationCondition.optimal:
        raise RuntimeError(f"modelo sem solução ótima: {status}")
    m.solutions.load_from(resultado)
    return m


if __name__ == "__main__":
    m = resolver()
    print("P =", round(pyo.value(m.x["P"]), 1), "| Q =", round(pyo.value(m.x["Q"]), 1),
          "| troca =", round(pyo.value(m.w)), "| margem =", round(pyo.value(m.margem)))
