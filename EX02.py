#HENRIQUE LUZ - 2023
#EX 02

#VARIÁVEIS
a = 0
b = 1
c = 0
memo = 0

fibolist = []
w = 0

#INÍCIO
print("A Sequência de Fibonacci!")
print('')
num = int(input("Digite um número a ser verificado na Sequência: "))
print('')
print("B", b, "+", "C", c, "=", "A", a)

#SEQUÊNCIA DE FIBONACCI
while a <= num:
    #print("B", b, "+", "C", c, "=", "A", a)

    a = b + c
    print("B", b, "+", "C", c, "=", "A", a)

    memo = b
    b = c
    c = a

    fibolist.append(a)

#print(fibolist)
#print(len(fibolist))
print('')

#VERIFICAÇÃO DO NÚMERO NA SEQUÊNCIA
while w <= (len(fibolist)):
    try:
        if num == fibolist[w]:
            #print('YESSS!')
            print('>>> FAZ parte da Sequência! <<<')
            break

    except:
        #print('OH NOO!')
        print('>>> NÃO FAZ parte da Sequência! <<<')
        
    #print(fibolist[w])
    w = w + 1

#FIM

#TENTATIVAS ANTERIORES        

"""
for x in fibolist:
    if num == x:
        print('Este número FAZ parte da Sequência de Fibonacci!')
        break
    
print('Este número NÃO FAZ parte da Sequência de Fibonacci!')
"""
"""
    if num == a:
        print('Este número faz parte da Sequência de Fibonacci!')
    
    elif num != a:
        print('Este número não faz parte da Sequência de Fibonacci!')
"""

    
