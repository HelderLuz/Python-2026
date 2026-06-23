# 5. Implemente uma expressão condicional para verificar se um número é par ou ímpar.

numero = int(input('Digite um número: '))

eh_par = numero % 2 == 0

print(f'O número é par? {eh_par}')