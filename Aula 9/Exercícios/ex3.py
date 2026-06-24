# 3. Escreva um programa que categorize a idade de uma pessoa da seguinte forma:
# "Criança" se tiver menos de 12 anos
# "Adolescente" se tiver entre 12 e 17 anos
# "Adulto" se tiver entre 18 e 59 anos
# "Idoso" se tiver 60 anos ou mais

idade = int(input('Digite a idade: '))

if idade < 12: # 0~11
    print('Criança')
elif idade <= 17: # 12~17
    print('Adolescente')
elif idade <= 59: # 18~59
    print('Adulto')
else: # 60~Inf
    print('Idoso')