def frequencia_palavras(frase):
    frequencia = {}
    palavras = frase.casefold().split()

    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

frase = 'Python é incrível e Python é poderoso'

frequencia = frequencia_palavras(frase)
print(frequencia)

for palavra, contagem in frequencia.items():
    print(f'Palavra: "{palavra}", Frequência: {contagem}')