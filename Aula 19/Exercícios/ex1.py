# 1. Crie uma matriz 3x3 representada por uma lista de listas e:
# - Imprima todos os elementos da matriz.
# - Calcule a soma dos elementos da diagonal principal.

def imprimir_matriz(matriz):
    print('Matriz')

    for linha in matriz:
        for valor in linha:
            print(f'{valor:3}', end='')
        print()
    print()

def somar_diagonal_principal(matriz):
    total = 0

    for i in range(len(matriz)):
        total += matriz[i][i]
    print(f'A soma da diagonal principal é {total}')

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

imprimir_matriz(matriz)
somar_diagonal_principal(matriz)