def preferidos(pessoa1, pessoa2):
    ambas = pessoa1 & pessoa2
    unicos_pessoa1 = pessoa1 - pessoa2
    unicos_pessoa2 = pessoa2 - pessoa1

    return ambas, unicos_pessoa1, unicos_pessoa2

pessoa1 = {'caneta', 'estojo', 'teclado', 'mouse', 'monitor'}
pessoa2 = {'teclado', 'mouse', 'microfone', 'sintetizador'}

ambos, p1, p2 = preferidos(pessoa1, pessoa2)

print(f'Ambos: {ambos} \nPessoa 1: {p1} \nPessoa 2: {p2}')