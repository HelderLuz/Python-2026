import os
caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, 'a', encoding='utf-8') as arquivo:
    arquivo.write('Adicionando conteúdo no final do arquivo\n')
