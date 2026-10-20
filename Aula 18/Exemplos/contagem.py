texto = "Python é incrível e Python é poderoso"
palavras = texto.split()
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)


