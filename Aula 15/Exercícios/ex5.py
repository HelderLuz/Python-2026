# 5. Escreva uma função eh_palindromo(texto) que verifique se uma string é um palíndromo, ou seja, se ela é igual quando lida de trás para frente. Ignore os espaços e a diferença entre maiúscula e minúscula.

def eh_palindromo(texto: str):
    texto = texto.casefold().replace(' ', '')

    for i in range(len(texto) // 2):
        if texto[i] != texto[-i-1]:
            return False
    return True

print(eh_palindromo("Apos a sopa"))  # Saída: True
print(eh_palindromo("Python"))       # Saída: False

def eh_palindromo_fatiado(texto: str):
    texto = texto.casefold().replace(' ', '')
    return texto == texto[::-1]

print(eh_palindromo_fatiado("Apos a sopa"))  # Saída: True
print(eh_palindromo_fatiado("Python"))       # Saída: False    