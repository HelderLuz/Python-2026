# 3. Crie um programa que use o módulo random para gerar um número aleatório entre 1 e 100 e peça ao usuário para adivinhar o número. Forneça dicas se o palpite for muito alto ou muito baixo.
import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

while True:
    palpite = int(input('Digite o palpite: '))

    if palpite == numero_aleatorio:
        break