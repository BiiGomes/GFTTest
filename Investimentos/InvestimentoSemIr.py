from Investimentos import Investimentos
valorInicial = int(input("Valor Inicial: "))
jurosMensais = int(input("Juros mensais: "))
calcularLucro = int(input("calcularLucro: "))
meses = int(input("Informe os meses: "))
retorno = 0

if valorInicial <= 1000:
    print("O valor inicial não pode ser menor que 1000")
else:
    retorno =(valorInicial(1+jurosMensais)**meses)-valorInicial

#printando os valores
print(valorInicial)
print(jurosMensais)
print(meses)
print(retorno)