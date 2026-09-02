# 4. Implementar um programa que verifique se um número está presente em uma lista de números informados pelo usuário. O programa deve solicitar inicialmente a lista de números e depois o número a ser buscado. Utilize alguma palavra para que o usuário possa terminar a lista de números (e.g. "parar").

lista = []

while True:
    entrada = input('Digite um número ("parar" para sair): ')

    if entrada.casefold() == 'parar':
        break

    lista.append(int(entrada))

numero = int(input('Digite um número para verificar se há na lista: '))

if numero in lista:
# if lista.count(numero) > 0:
    print(f'O número {numero} está presente na lista!')
else:
    print(f'O número {numero} não está presente na lista!')