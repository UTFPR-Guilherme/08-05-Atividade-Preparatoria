from abc import ABC, abstractmethod


class PoliticaDesconto(ABC):
    @abstractmethod
    def aplicar(self, valor_original):
        pass


class SemDesconto(PoliticaDesconto):
    def aplicar(self, valor_original):
        return valor_original


class DescontoPercentual(PoliticaDesconto):
    def __init__(self, percentual):
        self.percentual = percentual

    def aplicar(self, valor_original):
        desconto = valor_original * (self.percentual / 100)
        return valor_original - desconto


class DescontoCupom(PoliticaDesconto):
    def __init__(self, valor):
        self.valor = valor

    def aplicar(self, valor_original):
        valor_final = valor_original - self.valor
        return max(valor_final, 0.0)


class CalculadoraDesconto:
    def calcular(self, valor_original, politica):
        return politica.aplicar(valor_original)