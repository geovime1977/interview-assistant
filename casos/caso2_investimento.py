import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import caso_reator as c
from otimizacao_prescritiva.viabilidade import Premissas, fluxos_reais, payback_descontado, taxa_real, tir, vpl

CAPEX, OPEX_FIXO, VIDA = 30e6, 1.5e6, 10
p = Premissas(horizonte=VIDA, taxa_real=taxa_real(0.1232, 0.04), inflacao=0.04, aliquota_ir=0.34, anos_depreciacao=VIDA)


def margem(horas=720, troca=8, disp_A=None):
    original = dict(c.disp)
    if disp_A:
        c.disp["A"] = disp_A
    m = c.resolver_horas(horas, troca)
    c.disp.update(original)
    return m


def avaliar(nome, ebitda_inc):
    f = fluxos_reais(CAPEX, ebitda_inc, p)
    print(f"{nome:42s} EBITDA inc R$ {ebitda_inc/1e6:6.2f} mi/ano | VPL R$ {vpl(f, p.taxa_real)/1e6:7.2f} mi | "
          f"TIR {('%.1f%%' % (100*tir(f))) if tir(f) is not None else '—':>6} | payback {payback_descontado(f, p.taxa_real)}")
    return f


print(f"taxa real = {p.taxa_real:.4%}")
base = margem()
dois = margem(horas=1440, troca=0)
dois_A = margem(horas=1440, troca=0, disp_A=1000)
um_A = margem(disp_A=1000)
for nome, r in [("1 reator", base), ("2 reatores", dois), ("2 reatores + A=1000", dois_A), ("1 reator + A=1000", um_A)]:
    print(nome, r)
inc = lambda r: (r["margem"] - base["margem"]) * 12 - OPEX_FIXO
print()
avaliar("Premissa do diretor (margem dobra)", base["margem"] * 12 - OPEX_FIXO)
avaliar("Modelo: 2 reatores, A limitado a 500 t", inc(dois))
avaliar("Modelo: 2 reatores + contrato de A=1000 t", inc(dois_A))
print(f"Só ampliar o contrato de A (sem reator): +R$ {(um_A['margem']-base['margem'])*12/1e6:.2f} mi/ano, sem capex")
f = fluxos_reais(CAPEX, inc(dois_A), p)
errado = [-CAPEX] + [inc(dois_A) - 0.34 * (inc(dois_A) - CAPEX / VIDA)] * VIDA
print(f"Armadilha depreciação tratada como real: VPL R$ {vpl(errado, p.taxa_real)/1e6:.2f} mi (certo {vpl(f, p.taxa_real)/1e6:.2f})")
print(f"Armadilha fluxo real descontado à taxa nominal 12,32%: VPL R$ {vpl(f, 0.1232)/1e6:.2f} mi")
ebitda_eq = next(e for e in range(0, 20_000_000, 10_000) if vpl(fluxos_reais(CAPEX, e, p), p.taxa_real) >= 0)
print(f"EBITDA incremental de equilíbrio (VPL=0): R$ {ebitda_eq/1e6:.2f} mi/ano")
