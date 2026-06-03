# Peça a idade do usuário e calcule em quantos anos ele poderá se aposentar, considerando a idade mínima de 65 anos.
idade_minima_aposentadoria = 65
idade = int(input('Digite a sua idade: '))
tempo_aposentadoria = idade_minima_aposentadoria - idade

print(f'Falta {tempo_aposentadoria} anos para você se aposentar 😢')