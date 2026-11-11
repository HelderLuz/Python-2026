#  2. Escreva um programa que abra o arquivo "arquivo.txt" e exiba o seu conteúdo na tela.

import os

caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo:
        print(linha)