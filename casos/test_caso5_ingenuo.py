from caso5_modelo import resolver


def test_roda_e_da_margem_positiva():
    plano = resolver()
    assert plano.margem > 0
