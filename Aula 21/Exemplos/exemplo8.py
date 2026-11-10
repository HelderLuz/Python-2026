import os
caminho = os.path.dirname(__file__) + '\\arquivo.txt'

with open(caminho, "r+", encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo original:", conteudo)

    novo_conteudo = conteudo.replace("arquivo", "file")
    
    arquivo.seek(0)# Retorna o ponteiro para o início do arquivo
    arquivo.write(novo_conteudo) # Escreve o novo conteúdo no arquivo
    arquivo.truncate() # Trunca o arquivo para o tamanho do novo conteúdo

    arquivo.seek(0)
    novo_conteudo = arquivo.read()
    print("Conteúdo modificado:", novo_conteudo)
