# 5. Escreva uma função que receba uma tupla de strings e uma string como parâmetros, e retorne o número de vezes que a string aparece na tupla.
# Exemplo: Dada a tupla ("a", "b", "a", "c", "a") e a string "a", a função deve retornar 3.

def contagem(tupla: tuple, string: str):
    return tupla.count(string)

tupla = ("a", "b", "a", "c", "a")
string = "a"
print(f'Número de vezes: {contagem(tupla, string)}')