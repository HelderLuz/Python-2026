# 9. Crie um programa que gere a sequência de Fibonacci até o n-ésimo termo, onde n é informado pelo usuário.
# É uma sequência de números inteiros, começando por 0 e 1. Os números subsequentes corresponde a soma dos dois números anteriores.
# Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

tamanho = int(input('Digite o tamanho da sequência: '))
n1 = 0
n2 = 1

for i in range(tamanho):
    print(n1, end=', ')
    aux = n2
    n2 = n2 + n1
    n1 = aux