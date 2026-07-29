# 3. Crie um programa que imprime os números de 1 a 20, mas interrompe o laço quando o número for 13.

numero = 1

while numero <= 20:
    if numero == 13:
        break
    print(numero, end = ' ')
    numero += 1