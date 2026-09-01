# 1. Implementar um programa que permita ao usuário adicionar elementos em uma lista até que ele decida parar. Em seguida, o programa deve exibir a lista resultante e a quantidade de elementos.

lista = []

while True:
    elemento = input('Digite o elemento (digite "sair" para terminar): ')

    if elemento.casefold() == "sair":
        break

    lista.append(elemento)

print(f"Quantidade de elementos na lista: {len(lista)}")
print(f"Conteúdo da lista: {lista}")
for elemento in lista:
    print(elemento)