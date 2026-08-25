# 8. Escreva uma função chamada comparar_numeros que receba dois números, retorne True se eles forem iguais e a diferença entre eles se forem diferentes (n1 - n2).

def comparar_numeros(n1: float, n2: float):
    if n1 == n2:
        return True
    return n1 - n2

valor = comparar_numeros(11,10)
if valor == True and type(valor) == bool:
    print('Os valores são iguais')
else:
    print(f'Os valores são diferentes.\nA diferença é de {valor}')