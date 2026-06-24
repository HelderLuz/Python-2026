# 4. Crie um programa que leia a temperatura em graus Celsius e informe se está "Frio" (abaixo de 18°C), "Agradável" (entre 18°C e 26°C) ou "Quente" (acima de 26°C).

celsius = float(input('Digite a temperatura (ºC): '))

if celsius < 18:
    print('Frio 🥶')
elif celsius <= 26:
    print('Agradável 😊')
else:
    print('Quente 🥵')

