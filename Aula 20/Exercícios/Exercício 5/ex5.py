# Crie um módulo chamado conversor que contenha funções para converter entre diferentes unidades de medida, como pé para metros, milhas para quilômetros, Celsius para Fahrenheit, e os seus inversos. Importe esse módulo e use-o para fazer algumas conversões.

from conversor import pes_metros, metros_pes, milhas_km, km_milhas, celsius_fahrenheit, fahrenheit_celsius

print(f'1 pé em metros é {pes_metros(1)}')
print(f'1 metro em pés é {metros_pes(1)}')
print(f'1 milha em km é {milhas_km(1)}')
print(f'1 km em milha é {km_milhas(1)}')
print(f'30 Celsius em Fahrenheit é {celsius_fahrenheit(30)}')
print(f'90ºF é {fahrenheit_celsius(90)}ºC')
