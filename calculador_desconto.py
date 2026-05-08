class SemDesconto:
    pass


class DescontoPercentual:
    def __init__(self, percentual):
        self.percentual = percentual


class DescontoCupom:
    def __init__(self, valor):
        self.valor = valor


class CalculadoraDesconto:
    def calcular(self, valor_original, politica):
        if isinstance(politica, SemDesconto):
            return valor_original

        if isinstance(politica, DescontoPercentual):
            desconto = valor_original * (politica.percentual / 100)
            return valor_original - desconto

        if isinstance(politica, DescontoCupom):
            valor_final = valor_original - politica.valor
            return max(valor_final, 0.0)

        raise ValueError("Política de desconto inválida.")