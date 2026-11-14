import pytest

from caso5_modelo import MM, REACOES, Dados, com, consumo, resolver

TOL = 1e-6


@pytest.fixture(scope="module")
def base():
    return Dados(), resolver()


# 1. Unidade: funções puras, sem solver
@pytest.mark.parametrize("produto", ["P", "Q"])
def test_reacao_conserva_massa(produto):
    reagentes = sum(coef * MM[s] for s, coef in REACOES[produto].items())
    assert reagentes == pytest.approx(MM[produto])


def test_rendimento_menor_exige_mais_insumo():
    estequiometrico = 1 * MM["A"] / MM["P"]
    assert consumo(Dados(), "P", "A") == pytest.approx(estequiometrico / 0.90)
    assert consumo(com(rendimento={"P": 0.5, "Q": 0.95}), "P", "A") > consumo(Dados(), "P", "A")


# 2. Propriedades do plano: valem para qualquer solução ótima
def test_balanco_de_massa_fecha(base):
    d, p = base
    for s in "ABC":
        usado = sum(consumo(d, k, s) * p.producao[k] for k in "PQ")
        assert p.compra[s] >= usado - TOL


def test_reator_respeita_horas_incluindo_limpeza(base):
    d, p = base
    horas = sum(d.horas_por_t[k] * p.producao[k] for k in "PQ")
    roda_as_duas = p.producao["P"] > TOL and p.producao["Q"] > TOL
    assert horas + (d.horas_limpeza if roda_as_duas else 0) <= d.horas_mes + TOL


def test_contrato_venda_e_disponibilidade(base):
    d, p = base
    assert p.producao["Q"] >= d.contrato_q - TOL
    assert p.producao["P"] <= d.venda_max_p + TOL
    assert all(p.compra[s] <= d.disponivel[s] + TOL for s in "ABC")


def test_so_produz_com_a_reacao_ligada(base):
    _, p = base
    assert all(p.roda[k] == 1 for k in "PQ" if p.producao[k] > TOL)


# 3. Oráculo: resultado calculado à mão
def test_sem_valor_para_p_so_produz_q_ate_acabar_a():
    p = resolver(com(preco_venda={"P": 0, "Q": 3000}))
    q_maximo = 500 / consumo(Dados(), "Q", "A")
    margem_q = 3000 - 1500 * consumo(Dados(), "Q", "A") - 1000 * consumo(Dados(), "Q", "C")
    assert p.producao["P"] == pytest.approx(0, abs=TOL)
    assert p.producao["Q"] == pytest.approx(q_maximo)
    assert p.margem == pytest.approx(q_maximo * margem_q)


# 4. Regressão: o ótimo conhecido do caso base
def test_regressao_caso_base(base):
    _, p = base
    assert p.producao["P"] == pytest.approx(250)
    assert p.producao["Q"] == pytest.approx(337)
    assert p.margem == pytest.approx(1_325_055, abs=1)


# 5. Metamórficos: mudar um dado num sentido conhecido muda o resultado no sentido esperado
def test_preco_de_p_maior_nao_reduz_a_margem(base):
    _, p = base
    assert resolver(com(preco_venda={"P": 6000, "Q": 3000})).margem >= p.margem - TOL


def test_limpeza_mais_longa_nao_aumenta_a_margem(base):
    _, p = base
    assert resolver(com(horas_limpeza=100)).margem <= p.margem + TOL


def test_mais_materia_prima_nao_reduz_a_margem(base):
    _, p = base
    assert resolver(com(disponivel={"A": 900, "B": 200, "C": 300})).margem >= p.margem - TOL


# 6. Erros: entrada impossível gera erro claro
def test_contrato_impossivel_gera_erro_claro():
    with pytest.raises(RuntimeError, match="sem solução"):
        resolver(com(contrato_q=5000))
