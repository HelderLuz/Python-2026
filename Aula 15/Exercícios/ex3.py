# 3. Escreva uma função contar_palavras(frase) que receba uma string e retorne o número de palavras.

def contar_palavras(frase: str):
    return len(frase.split())

print(f'Número de palavras: {contar_palavras('Escreva uma função contar_palavras(frase) que receba uma string e retorne o número de palavras.')}')