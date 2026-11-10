import os
caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, "r", encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo original:", conteudo)

# Abre o arquivo no modo de escrita
with open(caminho, "w", encoding='utf-8') as arquivo:
    novo_conteudo = conteudo.replace("arquivo", "file") # Modifica o conteúdo
    arquivo.write(novo_conteudo)

with open(caminho, "r", encoding='utf-8') as arquivo:
    novo_conteudo = arquivo.read()
    print("Conteúdo modificado:", novo_conteudo)
