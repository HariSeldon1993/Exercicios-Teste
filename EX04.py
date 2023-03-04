#HENRIQUE LUZ - 2023
#EX 04

#TENTATIVA 1
"""
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma = 0
pct = 0

soma = sp + mg + rj + es + outros

print(soma)

pct = (sp * 100) / soma
print(round(pct, 2))

#A partir daqui teria que fazer um p/ cada estado...
"""

#TENTATIVA 2
total = 0
pct = 0

#Primeiro modelo de lista
lista = [{'SP': 67836.43},
         {'MG': 29229.88},
         {'RJ': 36678.66},
         {'ES': 27165.48},
         {'Outros': 19849.53}]

#Segundo modelo de lista
listab = [{'Estado': 'SP', 'FM': 67836.43},
          {'Estado': 'RJ', 'FM': 36678.66},
          {'Estado': 'MG', 'FM': 29229.88},
          {'Estado': 'ES', 'FM': 27165.48},
          {'Estado': 'Outros', 'FM': 19849.53}]

#print(listab)
#print('')

for x in listab:
    print(x)
    total = total + x.get('FM')

print('')
print('Faturamento Total: ',round(total,2))
print('')

for x in listab:
    pct = (x.get('FM') * 100) / (round(total,2))
    print('Participação de: ',x.get('Estado'),' = ',round(pct,2), '%')
