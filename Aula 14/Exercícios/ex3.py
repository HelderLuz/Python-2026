# 3. Declare uma lista e preencha-a somente com números ímpares que o usuário informar, preenchendo 10 elementos. Ao final, apresente a lista.

lista = []

while len(lista) < 10:
    numero = int(input('Digite um número: '))

    if numero % 2 == 1:
        lista.append(numero)

print(f'Lista: {lista}')