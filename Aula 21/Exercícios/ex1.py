# 1. Escreva um programa que crie um novo arquivo chamado "arquivo.txt" e escreva nele a frase "Olá, mundo!".

import os

caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Olá, mundo!')