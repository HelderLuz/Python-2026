# 3. Escreva um programa que permita ao usuário criar um arquivo. Apresente o caminho completo do arquivo após sua criação.

import os 

nome_arquivo = input('Digite o nome do arquivo: ')

caminho = os.path.dirname(__file__) + '\\' + nome_arquivo + '.txt'
print(caminho)

arquivo = open(caminho, 'w')
arquivo.close()