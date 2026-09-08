# Implementar um programa que simule uma lista de compras. O usuário deve poder adicionar e remover itens, além de visualizar a lista a qualquer momento.

# INICIAR PRÓXIMA AULA CORRIGINDO O EXERCÍCIO 8

lista = []

def menu():
    print('\nMENU')
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Apresentar lista de compras')
    print('4. Sair')

def adicionar(lista: list):
    item = input('Digite o item: ')
    lista.append(item)

def remover(lista: list):
    item = input('Digite o item para remover: ')
    lista.remove(item)

def listar(lista: list):
    print('\n\nLista de Compras')

    for item in lista:
        print(f'- {item}')

while True:
    menu()
    opcao = int(input('Opção: '))

    if opcao == 1:
        adicionar(lista)
    if opcao == 2:
        remover(lista)
    if opcao == 3:
        listar(lista)
    if opcao == 4:
        break