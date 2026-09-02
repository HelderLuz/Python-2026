# 5. Escreva uma função em Python que calcule a média de uma lista de números.

def media_lista(lista: list[float]):
    # soma = 0
    # for numero in lista:
    #     soma += numero

    # return soma / len(lista)
    return sum(lista) / len(lista)

print(f'Média: {media_lista([1,2,3,4,5,6,7,8,9,10])}')