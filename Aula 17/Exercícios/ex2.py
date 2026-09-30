# 2. Dado um conjunto de números, verifique se ele é um subconjunto de outro conjunto maior. Se for, imprima uma mensagem dizendo que o conjunto menor está contido no conjunto maior.

def ehSubconjunto(maior_conj: set, menor_conj: set) -> str:
    if menor_conj.issubset(maior_conj):
        return "É um subconjunto!"
    return "Não é um subconjunto!"

numeros1 = {1, 2, 3, 4, 5, 6, 7}
numeros2 = {2, 3, 4}
numeros3 = {6, 7, 8, 9}

print(f'{numeros2} é subconjunto {numeros1}? -> {ehSubconjunto(numeros1, numeros2)}')
print(f'{numeros3} é subconjunto {numeros1}? -> {ehSubconjunto(numeros1, numeros3)}')