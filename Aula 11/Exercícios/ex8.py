# 8. Implementar um programa que some todos os números informados pelo usuário até que seja digitada a palavra “Fim”.

soma = 0
numero = ''

while numero.casefold() != 'fim':
    numero = input('Digite um número ("fim" para sair): ')

    if numero.casefold() != 'fim':
        soma += int(numero)

print(f'Resultado: {soma}')