# 11. Crie um programa que receba três lados de um triângulo e classifique-o como:
    # "Equilátero": todos os lados possuem a mesma medida
    # "Isósceles": dois lados iguais
    # "Escaleno": três lados diferentes

lado1 = int(input('Digite o tamanho do lado 1: '))
lado2 = int(input('Digite o tamanho do lado 2: '))
lado3 = int(input('Digite o tamanho do lado 3: '))

if lado1 == lado2 and lado2 == lado3:
    print('Equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Isósceles')
else:
    print('Escaleno')