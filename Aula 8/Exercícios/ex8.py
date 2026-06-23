# 8. Verifique se dois números são iguais e se ambos são maiores que 10 usando expressão condicional.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

igual_maior_10 = numero1 == numero2 and numero1 > 10

print(f'Os números são iguais e maiores que 10? {igual_maior_10}')