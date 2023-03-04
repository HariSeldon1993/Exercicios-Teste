#HENRIQUE LUZ - 2023
#EX03

import json

arq = open('dados.json')
data = json.load(arq)

dia = []
val = []

filtro = []

somaval = 0
dam = 0

#VERIFICANDO DADOS
"""
print(data)
print(data[0])
print(data[0].get('dia'))
print(data[0].get('valor'))
"""
"""
for x in data:
    print(x.get('dia'))
    print(x.get('valor'))
"""

#EXCLUIR DIAS ZERADOS
for x in data:
    if x.get('valor') > 0:
        #print(x.get('valor'))
        #print(x)
        filtro.append(x)

        

print('Dias Com Vendas: ',len(filtro))

#SEPARAR DADOS EM LISTAS DIFERENTES
for x in filtro:
    dia.append(x.get('dia'))
    val.append(x.get('valor'))

#print(dia)
#print(val)

#TESTE MAX E MIN
print('Valor Máximo: ',max(val))
print('Valor Mínimo: ',min(val))

#SOMA VALORES E TESTE DA MÉDIA
for x in filtro:
    somaval = somaval + x.get('valor')
    #print(x.get('valor'))

media = round((somaval / len(filtro)), 4)

#DIAS ACIMA DA MÉDIA
for x in val:
    if x > media:
        #print(x)
        dam = dam + 1

#print(somaval)
print('Soma Total: ',round(somaval, 4)) 
print('Média das Vendas: ',media)
print('Dias com Vendas acima da Média: ',dam)
print('')

    
