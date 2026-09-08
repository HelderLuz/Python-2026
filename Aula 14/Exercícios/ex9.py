# 9. Implementar um programa que compare duas listas e retorne os elementos que são comuns a ambas.
lista1 = [1, 2, 3, 4, 5, 8]
lista2 = [2, 4, 5, 6, 7, 8, 9]

def comuns(lista1: list, lista2: list) -> list:
    comum = []

    for item in lista1:
        if item in lista2:
            comum.append(item)
    return comum

print(comuns(lista1, lista2))


