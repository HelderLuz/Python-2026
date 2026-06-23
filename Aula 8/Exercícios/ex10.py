# 10. Dado um número, use expressão condicional para averiguar se o número é múltiplo de 3 e 5 ao mesmo tempo.

numero = int(input('Digite um número: '))

multiplo3_5 = numero % 3 == 0 and numero % 5 == 0

print(f'O número é múltiplo de 3 e 5? {multiplo3_5}')
