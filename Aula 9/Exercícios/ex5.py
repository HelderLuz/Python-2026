# 5. Escreva um programa que receba a quantidade de faltas de um aluno e sua nota. Se a nota for maior ou igual a 60 e as faltas forem menores ou iguais a 5, imprima "Aprovado". Caso contrário, imprima "Reprovado".

faltas = int(input('Digite o número de faltas: '))
nota = int(input('Digite a nota: '))

if faltas <= 5 and nota >= 60:
    print('Aprovado!')
else:
    print('Reprovado!')