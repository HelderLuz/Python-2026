# 3. Crie um dicionário onde as chaves são os nomes de alunos e os valores são listas de suas notas. Em seguida:
# - Calcule e imprima a média das notas de cada aluno.
# - Exiba o nome dos alunos com média acima de 7.

def media(notas):
    return sum(notas) / len(notas)

alunos = {
    'Ana': [8, 9, 7],
    'Maria': [6, 9.5, 3, 9],
    'José': [10, 8.5],
    'Pedro': [6.5, 9, 7],
    'Josias': [5.5, 6.5, 7.5]
}

for nome, notas in alunos.items():
    print(nome, notas)

for nome, notas in alunos.items():
    print(f'Aluno: {nome} | Média: {media(notas):2.2}')

print('\n\nAlunos com média acima de 7:')
for nome, notas in alunos.items():
    if media(notas) > 7:
        print(nome)