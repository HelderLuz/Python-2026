# 7. Escreva um programa que leia um número e informe se ele é:
    # múltiplo de 2 e de 3 ao mesmo tempo
    # apenas múltiplo de 2
    # apenas múltiplo de 3
    # não é múltiplo de nenhum dos dois

num = int(input('Digite um número: '))

if num % 2 == 0 and num % 3 == 0:
    print('O número é múltiplo de 2 e 3!')
elif num % 2 == 0:
    print('O número é múltiplo de 2!')
elif num % 3 == 0:
    print('O número é múltiplo de 3!')
else:
    print('O número não é múltiplo de nenhum dos dois!')