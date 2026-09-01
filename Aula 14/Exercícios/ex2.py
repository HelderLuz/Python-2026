# 2. Leia uma lista de 12 números e em seguida ler também dois valores X e Y quaisquer correspondentes a duas posições na lista. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista = []
for i in range(12):
    lista.append(int(input(f'Digite o número [{i}]: ')))
soma = 0

x = int(input('Digite o valor X: '))
y = int(input('Digite o valor Y: '))

if x >= 0 and x < len(lista) and y >= 0 and y < len(lista):
    soma = lista[x] + lista[y]

    print(f'Resultado da soma de {lista[x]} e {lista[y]} é {soma}')
else:
    print('Valores de X ou Y estão fora do limite da lista.')