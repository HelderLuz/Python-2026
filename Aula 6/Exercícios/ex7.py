# 7. Solicite uma distância em quilômetros e converta para metros e centímetros.

quilometros  = float(input('Digite a distância em quilômetros: '))
metro = quilometros * 1000
centimetros = metro * 100

print(f'Quilômetros: {quilometros:.2f}km')
print(f'Metro: {metro:.2f}m')
print(f'Centímetros: {centimetros:.2f}cm')