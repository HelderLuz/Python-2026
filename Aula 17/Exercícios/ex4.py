# 4. Escreva uma função que receba dois conjuntos de palavras e retorne as palavras que estão em um dos conjuntos, mas não em ambos (diferença simétrica).

def ambos(conj1: set, conj2: set) -> set:
    return palavras.symmetric_difference(palavras2)

palavras = {'palavra', 'texto', 'número', 'vírgula'}
palavras2 = {'texto', 'número', 'acentuação'}

print(ambos(palavras, palavras2))