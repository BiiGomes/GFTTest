#classe pai
class Investimentos:

    def __init__(self, valorInicial, jurosMensais, calcularLucro):
        self.valorInicial = valorInicial
        self.jurosMensais = jurosMensais
        self.calcularLucro = calcularLucro

    def calcularLucro(self):
        meses = int(input("Informe os meses "))
        retorno = (self.valorInicial(1+self.jurosMensais)**meses)-self.valorInicial