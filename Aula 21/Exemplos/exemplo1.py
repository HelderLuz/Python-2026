import os # importação de módulo

print(__file__) # variável com o caminho do arquivo atual

caminho = os.path.dirname(__file__) # retorna o caminho do diretório do arquivo atual

print(caminho) # imprime o caminho do diretório

# concatenação do caminho com o nome do arquivo (padrão Windows)
arquivo = open(caminho + '\\arquivo.txt') 
arquivo.close()