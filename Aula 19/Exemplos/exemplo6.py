usuarios = {
    'joao': {
        'nome': 'João da Silva', 'idade': 25, 'sexo': 'M',
    },
    'maria': {
        'nome': 'Maria da Silva', 'idade': 30, 'sexo': 'F',
    },
    'pedro': {
        'nome': 'Pedro da Silva', 'idade': 28, 'sexo': 'M',
    },
}

for usuario, dados_usuario in usuarios.items():
    print(f'\nUsuário: {usuario} \nNome: {dados_usuario["nome"]}')
    print(f'Idade: {dados_usuario["idade"]} \nSexo: {dados_usuario["sexo"]}')
