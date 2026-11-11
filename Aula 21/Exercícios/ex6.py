# 6. Escreva um programa que leia o conteúdo de um arquivo de texto e apresente:
# - o número de linhas no arquivo
# - o número de palavras no arquivo
# - o número de caracteres no arquivo.

import os

caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, 'r', encoding='UTF-8') as arquivo:
    conteudo = arquivo.read()
    print(f'Número de caracteres: {len(conteudo)}')
    print(f'Número de palavras: {len(conteudo.split())}')
    print(f'Número de linhas: {len(conteudo.split('\n'))}')