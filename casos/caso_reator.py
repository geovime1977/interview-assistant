import pyomo.environ as pyo

MM = {"A": 40, "B": 10, "C": 20, "P": 60, "Q": 60}
rend = {"P": 0.90, "Q": 0.95}
cons = {
    "P": {"A": 1 * MM["A"] / MM["P"] / rend["P"], "B": 2 * MM["B"] / MM["P"] / rend["P"]},
    "Q": {"A": 1 * MM["A"] / MM["Q"] / rend["Q"], "C": 1 * MM["C"] / MM["Q"] / rend["Q"]},
}
preco_venda = {"P": 5000, "Q": 3000}
preco_compra = {"A": 1500, "B": 2000, "C": 1000}
disp = {"A": 500, "B": 200, "C": 300}
horas = {"P": 1.5, "Q": 1.0}
venda_max_P = 250


def resolver_horas(horas_mes=720, troca=8):
    return resolver(troca=troca, horas_mes=horas_mes)


def resolver(troca=8, minimo_Q=200, pv_P=5000, horas_mes=720):
    m = pyo.ConcreteModel()
    m.x = pyo.Var(["P", "Q"], domain=pyo.NonNegativeReals)
    m.c = pyo.Var(["A", "B", "C"], domain=pyo.NonNegativeReals)
    m.y = pyo.Var(["P", "Q"], domain=pyo.Binary)
    m.w = pyo.Var(domain=pyo.Binary)
    pv = {**preco_venda, "P": pv_P}
    m.obj = pyo.Objective(expr=sum(pv[k] * m.x[k] for k in "PQ") - sum(preco_compra[s] * m.c[s] for s in "ABC"), sense=pyo.maximize)
    m.bal = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] >= sum(cons[k].get(s, 0) * m.x[k] for k in "PQ"))
    m.disp = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] <= disp[s])
    m.contrato = pyo.Constraint(expr=m.x["Q"] >= minimo_Q)
    m.demP = pyo.Constraint(expr=m.x["P"] <= venda_max_P)
    m.reator = pyo.Constraint(expr=sum(horas[k] * m.x[k] for k in "PQ") + troca * m.w <= horas_mes)
    m.liga = pyo.Constraint(["P", "Q"], rule=lambda m, k: m.x[k] <= (horas_mes / horas[k]) * m.y[k])
    m.troca = pyo.Constraint(expr=m.w >= m.y["P"] + m.y["Q"] - 1)
    pyo.SolverFactory("appsi_highs").solve(m)
    v = pyo.value
    return {k: round(v(m.x[k]), 1) for k in "PQ"} | {s: round(v(m.c[s]), 1) for s in "ABC"} | {
        "rodaP": round(v(m.y["P"])), "troca": round(v(m.w)), "margem": round(v(m.obj)),
        "horas_usadas": round(sum(horas[k] * v(m.x[k]) for k in "PQ") + troca * v(m.w), 1)}


if __name__ == "__main__":
    print("consumo por t:", {k: {s: round(q, 3) for s, q in d.items()} for k, d in cons.items()})
    print("margem unitária P:", round(5000 - sum(preco_compra[s] * q for s, q in cons["P"].items())), "Q:", round(3000 - sum(preco_compra[s] * q for s, q in cons["Q"].items())))
    print("base         ", resolver())
    print("P a 2600/t   ", resolver(pv_P=2600))
    print("troca 200 h  ", resolver(troca=200))
