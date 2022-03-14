import utils

def test_gerar_valores_minimo_e_maximo_para_eixo_y():
    input_test = [
        [2,5,7,23],
        [-1,3,-5, 15],
        [0.12, -0.15, -0.25],
        [8534583.42423, 2834.34, 191],
        [8534583.42423, -14834.34, 191],
        [0.023, -0.023],
        [0.0023, -0.0027]
    ]

    expected_results = [
        (0.0, 25.0),
        (-5.5, 20.0),
        (-0.30, 0.15),
        (0, 9000000.0),
        (-15000, 9000000.0),
        (-0.025, 0.025),
        (-0.0030, 0.0025)
    ]

    for (i, e) in zip(input_test, expected_results):
        assert utils.gerar_limites_eixo_y(i) == e


