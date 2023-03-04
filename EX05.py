#HENRIQUE LUZ - 2023
#EX 05

#palavra = 'roma'
palavra =(input('Digite uma palavra para invertê-la: '))
tam = 0
y = 0
z = 0
lista = []
listab = []

#QUEBRA DA PALAVRA EM LISTA
for x in palavra:
    #print(x)
    lista.append(x)

"""
#print(lista)
#print(len(lista))
#tam = len(lista)
#print(tam)


for y in lista:
    print(y[tam])
    tam = tam - 1
"""

#VARIÁVEL COMO TAMANHO DA LISTA
z = len(lista) - 1
"""
while y < z:
    #print(lista[y])
    print(lista[y])
    y = y + 1
"""

#INVERSÃO DA PALAVRA DIGITADA
while z >= y:
    #print(lista[z])
    listab.append(lista[z])
    z = z - 1

print('Resultado: ',''.join(listab))
