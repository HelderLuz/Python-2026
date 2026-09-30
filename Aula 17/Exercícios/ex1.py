# 1. Dado dois conjuntos de números, crie funções para retornar:
# A união dos conjuntos.
# A intersecção dos conjuntos.

def uniao(conjunto1: set, conjunto2: set) -> set:
    return conjunto1.union(conjunto2)

def interseccao(conjunto1: set, conjunto2: set) -> set:
    return conjunto1.intersection(conjunto2)

numeros1 = {1, 2, 3, 4, 5}
numeros2 = {2, 5, 6, 7, 8}

print(f'União: {uniao(numeros1, numeros2)}')
print(f'Intersecção: {interseccao(numeros1, numeros2)}')