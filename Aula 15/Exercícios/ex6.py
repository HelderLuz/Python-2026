# 6. Escreva uma função contar_vogais(texto) que receba uma string e retorne o número de vogais (a, e, i, o, u) presentes no texto.

def contar_vogais(texto: str):
    vogais = 'aeiou'
    contador = 0

    # for letra in texto.casefold():
    #     if letra in vogais:
    #         contador+=1

    # return contador

    for vogal in vogais:
        contador += texto.casefold().count(vogal)
    return contador

print(contar_vogais('Apos a sopauie'))