# 3. Escreva uma função que receba uma string e retorne todas as palavras únicas (ignorando maiúsculas e minúsculas, e removendo pontuação) do texto.

def palavras_unicas(texto: str) -> set:
    palavras = texto.casefold().replace('!','').replace('.','').split()
    return set(palavras)

frase = 'uma frase qualquer. Junto de outra frase qualquer!'

print(palavras_unicas(frase))