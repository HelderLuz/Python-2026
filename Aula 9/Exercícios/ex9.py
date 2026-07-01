# 9. Escreva um programa que simule uma calculadora simples. O programa deve receber dois números e uma operação (+, -, *, /). O resultado da operação deve ser exibido.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, -, *, /): ')

if operacao == '+':
    print(f'Soma: {num1 + num2}')
elif operacao == '-':
    print(f'Subtração: {num1 - num2}')
elif operacao == '*':
    print(f'Multiplicação: {num1 * num2}')
elif operacao == '/':
    print(f'Divisão: {num1 / num2}')
else:
    print("Operação inválida.")