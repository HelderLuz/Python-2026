# Implemente um programa que, dados dois valores de entrada informados pelo usuário, troque os valores entre as variáveis iniciais, ou seja, a variável 1 deverá receber o valor da variável 2, e a variável 2 deverá receber o valor da variável 1.
caixa1 = input('Digite: ')
caixa2 = input('Digite: ')

caixa3 = caixa1
caixa1 = caixa2
caixa2 = caixa3

print(f'Caixa1 {caixa1} | caixa2: {caixa2}')