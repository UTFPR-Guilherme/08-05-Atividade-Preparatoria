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
        raise NotImplementedError("Lógica ainda não implementada.")