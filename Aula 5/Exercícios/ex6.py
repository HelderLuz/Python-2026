# Considere qtd_alunos = 29 e capacidade_grupo = 4. Calcule quantos grupos completos podem ser formados e quantos alunos sobram.

qtd_alunos = 29
capacidade_grupo = 4

print(f'Qtd de grupos completos: {qtd_alunos // capacidade_grupo}')
print(f'Alunos restantes: {qtd_alunos % capacidade_grupo}')