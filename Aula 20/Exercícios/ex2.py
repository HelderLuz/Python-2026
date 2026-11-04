# 2. Crie um programa que use o módulo math para calcular o seno, cosseno e tangente de um ângulo em graus informado pelo usuário. Use a função math.radians() e math.degrees() para converter entre graus e radianos.
from math import cos, sin, tan, radians

graus = int(input('Digite o ângulo em graus: '))

radianos = radians(graus)

print(f'Seno: {sin(radianos):.3f}')
print(f'Cosseno: {cos(radianos):.3f}')
print(f'Tangente: {tan(radianos):.3f}')