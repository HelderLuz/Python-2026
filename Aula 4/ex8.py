# Dada uma variável idade com um número inteiro, crie uma variável idade_str que converta esse número para uma string. Em seguida, crie uma frase que diga "Eu tenho [idade] anos."

idade = 30
idade_str = str(idade)

# print(idade, type(idade), idade_str, type(idade_str))
frase = f'Eu tenho {idade_str} anos.'
print(frase)