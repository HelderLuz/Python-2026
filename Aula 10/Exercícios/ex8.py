# 8. Implementar um programa que calcule a potência de um número utilizando uma estrutura de repetição. O programa deve solicitar ao usuário que informe a base e o expoente, ambos considerados comos inteiros.

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: ')) 
potencia = 1

for i in range(expoente):
    potencia = potencia * base

print(f'A potência é {potencia}')