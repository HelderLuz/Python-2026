# 7. Leia uma lista de 10 números e em seguida um valor X qualquer. Seu programa deverá fazer uma busca do valor de X na lista e informar a posição em que foi encontrado ou se não foi encontrado.

lista = []
for i in range(10):
    lista.append(int(input(f'Digite um número [{i}]: ')))

x = int(input('Digite o valor de X: '))

if x in lista:
    print('O número foi encontrado')
    posicao = lista.index(x)
    print(f'Posição: {posicao}')
else:
    print('O número não foi encontrado')