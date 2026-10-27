pizzas = [
    {
        'massa': 'fina',
        'coberturas': ['queijo', 'tomate', 'azeitona'],
        'preco': 50,
        'tamanho': 'média'
    },
    {
        'massa': 'pan',
        'coberturas': ['molho de tomate', 'queijo mussarela', 'tomate', 'catupiry', 'cebola roxa', 'azeitona sem caroço'],
        'preco': 110,
        'tamanho': 'grande'
    }
]

for pizza in pizzas:
    print(f'Pizza de massa {pizza['massa']} com as coberturas: ', end='')
    coberturas = pizza['coberturas']

    # for cobertura in coberturas:
    #     print(f'{cobertura}', end=', ')

    for i in range(len(coberturas)):
        if i < len(coberturas)-1:
            print(f'{coberturas[i]}', end=', ')
        else:
            print(f'{coberturas[i]}', end='.')
            
    print(f'\nTamanho: {pizza['tamanho']}. \nPreço: R${pizza['preco']:6.2f}\n')