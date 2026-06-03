# Peça ao usuário para inserir o ano de seu nascimento e calcule sua idade, considerando o ano atual igual a 2026.
ano_atual = 2026

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'A sua idade é {idade} anos')