# Implemente um programa que, dado um valor de lado informado pelo usuário, calcule a área do quadrado e formate a saída para que o valor seja apresentado com duas casas decimais.
lado = float(input('Digite o tamanho do lado do quadrado: '))
area = lado * lado
print(f'A área do quadrado é {area:.2f}')