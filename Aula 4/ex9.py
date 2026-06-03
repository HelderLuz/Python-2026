# Dado o nome, sobrenome e idade de uma pessoa, usando concatenação de string, combine essas variáveis em uma única frase, que diga "Meu nome é [nome completo] e eu tenho [idade] anos."

nome = 'Ana'
sobrenome = 'Fezz'
idade = 40
frase = 'Meu nome é ' + nome + ' ' + sobrenome + ' e eu tenho ' + str(idade) + ' anos.'
ffrase = f'Meu nome é {nome} {sobrenome} e eu tenho {idade} anos.'
print(frase)
print(ffrase)
