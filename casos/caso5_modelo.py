"""Modelo do reator (caso 1) com dados parametrizáveis, para ser testado."""
from dataclasses import dataclass, field, replace

import pyomo.environ as pyo

MM = {"A": 40, "B": 10, "C": 20, "P": 60, "Q": 60}
REACOES = {"P": {"A": 1, "B": 2}, "Q": {"A": 1, "C": 1}}


@dataclass(frozen=True)
class Dados:
    rendimento: dict = field(default_factory=lambda: {"P": 0.90, "Q": 0.95})
    preco_venda: dict = field(default_factory=lambda: {"P": 5000, "Q": 3000})
    preco_compra: dict = field(default_factory=lambda: {"A": 1500, "B": 2000, "C": 1000})
    disponivel: dict = field(default_factory=lambda: {"A": 500, "B": 200, "C": 300})
    horas_por_t: dict = field(default_factory=lambda: {"P": 1.5, "Q": 1.0})
    horas_mes: float = 720
    horas_limpeza: float = 8
    contrato_q: float = 200
    venda_max_p: float = 250


@dataclass
class Plano:
    producao: dict
    compra: dict
    roda: dict
    troca: int
    margem: float


def consumo(d: Dados, produto: str, insumo: str) -> float:
    """t de insumo por t de produto: razão mássica da estequiometria dividida pelo rendimento."""
    return REACOES[produto].get(insumo, 0) * MM[insumo] / MM[produto] / d.rendimento[produto]


def resolver(d: Dados = Dados()) -> Plano:
    m = pyo.ConcreteModel()
    m.x = pyo.Var(["P", "Q"], domain=pyo.NonNegativeReals)
    m.c = pyo.Var(["A", "B", "C"], domain=pyo.NonNegativeReals)
    m.y = pyo.Var(["P", "Q"], domain=pyo.Binary)
    m.w = pyo.Var(domain=pyo.Binary)
    m.margem = pyo.Objective(
        expr=sum(d.preco_venda[k] * m.x[k] for k in "PQ") - sum(d.preco_compra[s] * m.c[s] for s in "ABC"),
        sense=pyo.maximize,
    )
    m.balanco = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] >= sum(consumo(d, k, s) * m.x[k] for k in "PQ"))
    m.disponibilidade = pyo.Constraint(["A", "B", "C"], rule=lambda m, s: m.c[s] <= d.disponivel[s])
    m.contrato = pyo.Constraint(expr=m.x["Q"] >= d.contrato_q)
    m.venda_p = pyo.Constraint(expr=m.x["P"] <= d.venda_max_p)
    m.reator = pyo.Constraint(expr=sum(d.horas_por_t[k] * m.x[k] for k in "PQ") + d.horas_limpeza * m.w <= d.horas_mes)
    m.liga = pyo.Constraint(["P", "Q"], rule=lambda m, k: m.x[k] <= (d.horas_mes / d.horas_por_t[k]) * m.y[k])
    m.troca = pyo.Constraint(expr=m.w >= m.y["P"] + m.y["Q"] - 1)

    resultado = pyo.SolverFactory("appsi_highs").solve(m, load_solutions=False)
    status = resultado.solver.termination_condition
    if status != pyo.TerminationCondition.optimal:
        raise RuntimeError(f"modelo sem solução ótima: {status}")
    m.solutions.load_from(resultado)
    v = pyo.value
    return Plano(
        producao={k: v(m.x[k]) for k in "PQ"},
        compra={s: v(m.c[s]) for s in "ABC"},
        roda={k: round(v(m.y[k])) for k in "PQ"},
        troca=round(v(m.w)),
        margem=v(m.margem),
    )


def com(**ajustes) -> Dados:
    return replace(Dados(), **ajustes)
