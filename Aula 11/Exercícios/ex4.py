# 4. Escreva um programa que solicita ao usuário adivinhar um número secreto entre 1 e 10. O programa continua pedindo palpites até que o número correto seja adivinhado. Use if para verificar se o palpite está correto e while para manter o laço.

numero_secreto = 7

while True:
    palpite = int(input('Palpite (Entre 1 e 10): '))

    if palpite == numero_secreto:
        print('Você acertou!')
        break
    else:
        print('Você errou!!!')