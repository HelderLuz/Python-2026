# 7. Use uma expressão condicional para verificar se um número é positivo e maior que 100 ou negativo.

numero = int(input('Digite um número: '))

maior100_negativo = numero > 100 or numero < 0

print(f'O número é maior que 100 ou negativo? {maior100_negativo}')