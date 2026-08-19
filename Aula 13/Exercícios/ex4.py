# 5. Escreva uma função chamada soma_impares que receba um número inteiro positivo n e retorne a soma de todos os números ímpares de 0 até n.

def soma_impares(numero: int):
    soma = 0

    for i in range(1, numero + 1):
        if i % 2 == 1:
            soma = soma + i
    return soma

numero = int(input('Digite um número: '))
somatoria = soma_impares(numero)
print(f'A soma dos ímpares de 1 até {numero} é {somatoria}')