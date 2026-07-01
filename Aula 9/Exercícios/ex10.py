# Escreva um programa que leia o salário de um funcionário e calcule o valor do imposto de renda a ser pago, considerando:
    # Faixa salarial até R$ 2.000,00: isento
    # R$ 2.000,01 até R$ 3.500,00: 10%
    # Acima de R$ 3.500,00: 20%.

salario = float(input('Digite o salário: '))

if salario <= 2000:
    print('Isento')
elif salario <= 3500:
    print(f'O imposto de renda é de {salario * 0.1}')
else:
    print(f'O imposto de renda é de {salario * 0.2}')