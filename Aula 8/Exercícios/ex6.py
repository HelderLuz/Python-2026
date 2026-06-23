# 6. Dada uma nota de 0 a 10, verifique se o aluno foi aprovado usando uma expressão condicional. A aprovação requer uma nota maior ou igual a 6.

nota = int(input('Digite a nota (0 a 10): '))

aprovado = nota >= 6

print(f'Aluno aprovado? {aprovado}')