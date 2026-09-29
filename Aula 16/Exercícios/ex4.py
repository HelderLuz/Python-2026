# 4. Escreva uma função chamada esta_ordenada que receba uma tupla de números e retorne True se os elementos estiverem em ordem crescente, e False caso contrário.
def esta_ordenada(numeros):
    for i in range(1, len(numeros)):
        if numeros[i] < numeros[i-1]:
            return False
    return True

tupla1 = (1, 2, 3, 4, 5, 6, 7)
tupla2 = (1, 2, 3, 4, 5, 7, 6)
print(f'Tupla1 está ordenada? {esta_ordenada(tupla1)}')
print(f'Tupla2 está ordenada? {esta_ordenada(tupla2)}')