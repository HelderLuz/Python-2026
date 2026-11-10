import os
caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    # linha = arquivo.readline()

    # while(linha):
    #     print(linha, end='')
    #     linha = arquivo.readline()
    for linha in arquivo:
        print(linha, end='')