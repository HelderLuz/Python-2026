frutas = ['🍎', '🍌', '🍊', '🍉', '🍉']

def modificar_fruta(frutas):
    indice = int(input('Digite o indice: '))
    fruta = input('Digite a fruta: ')

    frutas[indice] = fruta

modificar_fruta(frutas)
print(frutas)