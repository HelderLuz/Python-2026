# 6. Implementar um programa que, dado um número inteiro n informado pelo usuário, calcule a média dos n primeiros números naturais. Considere que os números naturais começam em 0.

n = int(input('Digite um número: '))
soma = 0
print('Números naturais: ', end='')
for i in range(n):
    soma = soma + i
    print(i, end=' ')
print(f'\nSoma: {soma} \nMédia {soma / n}')