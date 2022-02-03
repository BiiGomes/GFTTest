from Investimentos import *
#input do valor com IR
valorInicial = int(input("Valor Inicial: "))
jurosMensais = int(input("Juros mensais: "))
calcularLucro = int(input("calcularLucro: "))
meses = int(input("Informe os meses "))
desconto = 0.0
retorno = 0

#meses contando o desconto
if meses > 6:
    desconto = 22,5
    retorno = (valorInicial(1 + jurosMensais) ** meses) - valorInicial

elif meses >= 6 & meses <= 12:
    desconto = 20
    retorno = (valorInicial(1 + jurosMensais) ** meses) - valorInicial

elif meses >= 12 & meses <= 24:
    desconto = 17,5
    retorno = (valorInicial(1 + jurosMensais) ** meses) - valorInicial

elif meses >= 24:
    desconto = 15
    retorno = (valorInicial(1 + jurosMensais) ** meses) - valorInicial

#printando as informações
print(valorInicial)
print(jurosMensais)
print(meses)
print(retorno)