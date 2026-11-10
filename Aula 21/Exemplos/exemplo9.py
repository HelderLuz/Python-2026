import os
caminho = os.path.dirname(__file__) + '\\arquivo.txt'

if (os.path.exists(caminho)):
    os.remove(caminho)
