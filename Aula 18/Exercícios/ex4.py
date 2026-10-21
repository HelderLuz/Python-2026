# 4. Implementar um programa que faça o cadastro de uma pessoa. Os dados pessoais informados são: nome, idade, telefone e e-mail. O programa deve mostrar os dados cadastrados.

pessoa = {
    'nome':'',
    'idade': 0,
    'telefone': '',
    'email': ''
}

for chave in pessoa:
    pessoa[chave] = input(f'Digite o {chave}: ')

# pessoa['nome'] = input('Digite o nome: ')
# pessoa['idade'] = input('Digite o idade: ')
# pessoa['telefone'] = input('Digite o telefone: ')
# pessoa['email'] = input('Digite o email: ')

for chave, valor in pessoa.items():
    print(f'{chave.title()}: {valor}')