import os
caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)  # O arquivo é fechado automaticamente

