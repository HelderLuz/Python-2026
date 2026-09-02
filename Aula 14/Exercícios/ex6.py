# 6. Escreva uma função em Python que encontre o maior e menor valor em uma lista de números.

def maior_menor(lista: list[int]):
    # maior = lista[0]
    # menor = lista[0]

    # for numero in lista:
    #     if numero > maior:
    #         maior = numero
    #     if numero < menor:
    #         menor = numero

    # return maior, menor
    
    return max(lista), min(lista)

    # Organiza a lista em ordem crescente
    # lista.sort()
    # return lista[len(lista) - 1], lista[0]

maior, menor = maior_menor([7,4,8,3,9,5,2,6])

print(f'Maior: {maior} \nMenor: {menor}')