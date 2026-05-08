import unittest

from calculador_desconto import (
    CalculadoraDesconto,
    SemDesconto,
    DescontoPercentual,
    DescontoCupom
)


class TestCalculadoraDesconto(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraDesconto()

    def test_sem_desconto_retorna_valor_original(self):
        politica = SemDesconto()

        resultado = self.calculadora.calcular(100.0, politica)

        self.assertEqual(resultado, 100.0)

    def test_desconto_percentual_aplica_percentual_fixo(self):
        politica = DescontoPercentual(10)

        resultado = self.calculadora.calcular(200.0, politica)

        self.assertEqual(resultado, 180.0)

    def test_desconto_por_cupom_subtrai_valor_fixo(self):
        politica = DescontoCupom(20.0)

        resultado = self.calculadora.calcular(100.0, politica)

        self.assertEqual(resultado, 80.0)

    def test_desconto_por_cupom_nao_retorna_valor_negativo(self):
        politica = DescontoCupom(20.0)

        resultado = self.calculadora.calcular(10.0, politica)

        self.assertEqual(resultado, 0.0)


if __name__ == "__main__":
    unittest.main()