# 4. Implementar um programa que imprima a tabuada de um número informado pelo usuário. O programa deve exibir os resultados das multiplicações desse número por valores de 0 até 10.

numero = int(input('Digite o número: '))

for i in range(11):
    print(f'{numero} * {i:2d} = {i * numero}')