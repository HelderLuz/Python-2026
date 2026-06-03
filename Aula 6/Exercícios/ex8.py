# 8. Implemente um programa que, dada uma quantidade de litros de abastecimento e o preço em reais do combustível informados pelo usuário, calcule e apresente o valor total do abastecimento com duas casas decimais.

litros = float(input('Digite a quantidade em litros: '))
preco = float(input('Digite o preço (R$): '))

valor_total = litros * preco
print(f'Valor total: R${valor_total:.2f}')