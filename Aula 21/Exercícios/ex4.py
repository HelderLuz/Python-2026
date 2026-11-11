# 4. Escreva um programa que solicite ao usuário que digite uma frase e salve-a em um arquivo chamado "frase.txt".

import os

caminho = os.path.dirname(__file__) + '\\frase.txt'

with open(caminho, 'w', encoding='UTF-8') as arquivo:
    frase = input('Digite uma frase: ')
    arquivo.write(frase)