# 5. Implementar um programa que encontre o menor valor de uma sequência de números informados pelo usuário. O programa deve solicitar, inicialmente, a quantidade de números a serem fornecidos. Em seguida, o usuário deve informar os números um a um. O programa deve encontrar e exibir o menor valor da sequência.

qtd = int(input('Digite o tamanho do sequência: '))
menor = int(input(f'{1}: '))

print('Digite os números: ')
for i in range(1, qtd):
    numero = int(input(f'{i + 1}: '))

    if numero < menor:
        menor = numero

print(f'O menor número da sequência é {menor}.')