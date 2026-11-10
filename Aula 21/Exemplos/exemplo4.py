import os
caminho = os.path.dirname(__file__) + '\\arquivo2.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrevendo no arquivo com Python\n')
