# 2. Crie um dicionário com nomes de 2 frutas e seus preços em reais. Adicione a fruta "Morango" com o preço de R$ 7,90.

frutas = {
    'uva': 9.90,
    'banana': 3.50
}

frutas['morango'] = 7.90

for fruta, valor in frutas.items():
    print(f'{fruta} - R$ {valor}')