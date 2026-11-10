import os
nome_arquivo = input('Digite o nome do arquivo: ')
caminho = os.path.dirname(__file__) + '\\' + nome_arquivo

with open(caminho, 'w', encoding='utf-8') as arquivo:
    while True:
        texto = input('Digite o texto para ser escrito no arquivo: ')
        if texto.casefold() == 'sair':
            break

        arquivo.write(texto + '\n')
