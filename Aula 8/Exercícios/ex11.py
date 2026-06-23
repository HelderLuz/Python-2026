# 11. Considerando idade e renda. Crie uma expressão booleana para verificar se a pessoa pode solicitar um empréstimo, considerando que ela deve ser maior de idade e ter renda de pelo menos R$ 2000,00.

idade = int(input('Digite a idade: '))
renda = float(input('Digite a renda: '))

emprestimo = idade >= 18 and renda >= 2000

print(f'Pode solicitar um empréstimo? {emprestimo}')