#Input dos elementos, onde o usuário deve colocar os respectivos números
n1 = int(input("Primeiro numero "))
n2 = int(input("Segundo numero "))
n3 = int(input("Terceiro numero "))
n4 = int(input("Quarto numero "))
n5 = int(input("Quinto numero "))
n6 = int(input("Sexto numero "))
n7 = int(input("Sétimo numero "))
n8 = int(input("Oitavo numero "))
n9 = int(input("Nono numero "))
n10 = int(input("Décimo numero "))

#lista com os elementos
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

#lista auxiliar para que o programa não se perca
listaAux = []

#realizacao da media
media = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10/10

#printando a lista completamente
print(lista)

#printando o maior número, o menor numero e a media aritmetica
print(f"O maior número é {max(lista)}")
print(f"O menor número é {min(lista)}")
print(f"A média aritmética desses números é {media}")

#percorrendo a lista para encotrar os numeros acima de 10
for elem in lista:
    if elem > 10:
        listaAux.append(elem)

#printando os numeros acima de 10
print(f"Elementos acima de 10{listaAux}")

#percorrendo a lista para encontrar os numeros acima de 50
for elemA in lista:
    if elemA > 50:
        listaAux.append(elemA)

#printando os elementos acima de 50
print(f"Elementos acima de 50 {listaAux}")

