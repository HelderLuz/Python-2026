matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# imprimir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f'{valor:4}', end='')
        print()

imprimir_matriz(matriz)
print()
matriz[1][1] = 10  # modificando um valor
imprimir_matriz(matriz)
# print(matriz)
