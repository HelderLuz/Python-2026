# 5. Escreva um programa que crie um novo arquivo de texto e permita que o usuário escreva nele. O programa deve pedir ao usuário para digitar cada linha e salvar o conteúdo no arquivo. Defina uma forma para que o usuário finalize a escrita no arquivo.

import os

caminho = os.path.dirname(__file__) + '\\novo.txt'

with open(caminho, 'w', encoding='UTF-8') as arquivo:
    while True:
        texto = input('Digite o texto ou "sair": ')
        if (texto.casefold() == "sair"):
            break
        arquivo.write(texto + '\n')