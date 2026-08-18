def operacao(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao # retorna uma tupla, veremos mais detalhes depois

resultado1, resultado2 = operacao(3, 4)
print(f'Resultado da soma é {resultado1}')
print(f'Resultado da subtração é {resultado2}')
