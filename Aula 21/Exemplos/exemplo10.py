pessoas = []

import os
caminho = os.path.dirname(__file__) + '\\dicionario.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, idade, salario = linha.rstrip('\n').split(';')
        idade = (int(idade))
        salario = float(salario)
        pessoa = {'nome': nome, 'idade': idade, 'salario': salario}
        pessoas.append(pessoa)

print(pessoas)
