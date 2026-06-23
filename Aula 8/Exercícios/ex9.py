# 9. Receba dois números e verifique se pelo menos um deles é negativo com expressão condicional.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

eh_negativo = numero1 < 0 or numero2 < 0

print(f'Um dos números é negativo? {eh_negativo}')