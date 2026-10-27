def compra(estoque, produto, qtd):
    produto = produto.casefold()
    if produto not in estoque:
        print('Produto não encontrado')
        return
    
    if estoque[produto] < qtd:
        print('Quantidade insuficiente')
        return
    
    estoque[produto] -= qtd
    print(f'Preço da compra: {qtd * 2.5}')

estoque = {
    'mouse': 4,
    'teclado': 3,
    'monitor': 5,
    'fonte': 3
}

produto = input('Digite o produto: ')
qtd = int(input('Quantidade: '))

compra(estoque, produto, qtd)

print(estoque)