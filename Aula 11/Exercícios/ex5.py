# 5. Escreva um programa que solicite ao usuário números inteiros positivos até que ele digite um número negativo. O programa deve somar todos os números positivos e, ao final, exibir a soma.

soma = 0
numero = 0

while numero >= 0:
    soma += numero
    numero = float(input('Digite um número (negativo para sair): '))

print(f'Resultado: {soma}')