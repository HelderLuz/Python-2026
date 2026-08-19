# 3. Escreva uma função chamada eh_primo que receba um número inteiro positivo e retorne True se for um número primo, e False caso contrário.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.

def eh_primo(numero: int):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

# Verificando apenas o número 12
if eh_primo(12):
    print(f'12 é primo!')
else:
    print(f'12 não é primo!')

# Verificando entre os número 1 e 48
for i in range(1, 48):
    if eh_primo(i):
        print(f'{i} é primo!')
    else:
        print(f'{i} não é primo!')

# Verificando entre os números 1 e 48, mas apresentando apenas os números primos
print('Números primos: ', end='')
for i in range(1, 48000):
    if eh_primo(i):
        print(f'{i} ', end='')