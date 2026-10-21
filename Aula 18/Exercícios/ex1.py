# 1. Crie um dicionário com 3 nomes de países e suas respectivas capitais. Imprima a capital de cada país.

capitais = {
    'brasil': 'brasília',
    'inglaterra': 'londres',
    'frança': 'paris'
}

for pais, capital in capitais.items():
    print(f'País: {pais.title()} | Capital: {capital.title()}')