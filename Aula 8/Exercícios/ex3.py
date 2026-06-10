# Qual é o valor da variável resultado ao final da execução do código? Encontre o valor sem executar o código.

a = 12
b = 5
c = 8
d = 3
resultado = ((a / b > 2) and (c % d == 2)) or (not(a - c < d) and (b * d <= a))
# resultado = ((12 / 5 > 2) and (8 % 3 == 2)) or (not(12 - 8 < 3) and (5 * 3 <= 12))
# resultado = ((2.4 > 2) and (2 == 2)) or (not(4 < 3) and (15 <= 12))
# resultado = (True and True) or (not False and False))
# resultado = True or (True and False)
# resultado = True or False
# resultado = True
print(resultado)