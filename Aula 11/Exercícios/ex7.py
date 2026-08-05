# 7. Escreva um programa que calcula a média de uma série de números positivos, parando quando o número zero for encontrado. Exiba a média no final.

soma = 0
qtd = 0
numero = 1

while numero != 0:
    numero = int(input('Digite um número (0 para sair): '))

    if numero > 0:
        soma += numero
        qtd += 1

print(f'Média: {soma / qtd}')