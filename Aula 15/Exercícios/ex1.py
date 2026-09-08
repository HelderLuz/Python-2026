# 1. Escreva uma função formatar_nome(nome_completo) que receba uma string com um nome completo em letras minúsculas e retorne o nome com a primeira letra de cada nome em maiúscula.

def formatar_nome(nome_completo: str):
    return nome_completo.title()

print(formatar_nome('helder jefferson ferreira da luz'))