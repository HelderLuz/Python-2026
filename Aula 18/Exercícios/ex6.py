# 6. Crie um dicionário para armazenar os nomes e notas de 5 alunos.
# - Verifique se um aluno específico está no dicionário.
# - Caso esteja, exiba a nota dele.
# - Caso contrário, exiba uma mensagem que o aluno não foi encontrado.

alunos = {
    'ana': 9.0,
    'maria': 7.5,
    'josé': 8.0,
    'paulo': 8.5,
    'rafael': 5.0
}

nome = input('Digite o nome do aluno: ')

if nome.casefold() in alunos:
    print(f'A nota do aluno {nome.title()} é {alunos[nome.casefold()]}')
else:
    print('O aluno não foi encontrado!')