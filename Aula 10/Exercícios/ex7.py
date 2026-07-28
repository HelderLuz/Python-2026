# 7. Implementar um programa que, dado um número inteiro informado pelo usuário, calcule o fatorial desse número. O fatorial de um número (n!) é o produto de todos os inteiros positivos menores ou iguais a ele. Por exemplo, 4! = 4×3×2×1. Por definição, 0! = 1.

numero = int(input('Digite um número: '))
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i
    print(f'{i}! = {fatorial}')

print(f'Fatorial de {numero} é {fatorial}')