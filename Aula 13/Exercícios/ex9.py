# 9. Escreva uma função chamada menor_e_maior que receba três números e retorne o menor e o maior valor entre eles.

def menor_e_maior(n1: float, n2: float, n3: float):
    menor = n1
    maior = n1

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return menor, maior

menor, maior = menor_e_maior(2,1,3)
print(f'Menor: {menor} \nMaior: {maior}')