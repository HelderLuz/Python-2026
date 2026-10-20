# 5. Imagine que você tem dois conjuntos:
# - O primeiro contém o nome de todos os alunos de uma turma.
# - O segundo contém os alunos presentes em uma aula.
# Escreva uma função para mostrar quais alunos estavam ausentes.

def alunos_ausentes(alunos: set, presentes: set) -> set:
    return alunos - presentes

alunos = {'Ana', 'Maria', 'João', 'Pedro', 'Paula', 'Benedita'}
alunos_presentes = {'Maria', 'Pedro', 'Paula'}

print(alunos_ausentes(alunos, alunos_presentes))