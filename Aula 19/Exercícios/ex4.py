# 4. Crie uma lista de dicionários, onde cada dicionário representa um produto com as chaves: "nome", "preço", e "estoque".
# - Adicione ao menos 3 produtos diferentes.
# - Calcule o valor total do estoque (preço * quantidade para cada produto).
# - Exiba os produtos cujo estoque é maior que 10 unidades.

def valor_total_produto(produto):
    return produto['preco'] * produto['estoque']

produtos = [
    {
        'nome': 'mouse',
        'preco': 250.90,
        'estoque': 25
    },
    {
        'nome': 'teclado',
        'preco': 399.90,
        'estoque': 22
    },
    {
        'nome': 'monitor',
        'preco': 1341.90,
        'estoque': 7
    }
]

for produto in produtos:
    print(f'Produto: {produto['nome']} \nValor total do estoque: R$ {valor_total_produto(produto):8.2f}\n')

print('Produtos com estoque superior a 10:')
for produto in produtos:
    if produto['estoque'] > 10:
        print(f'{produto['nome'].title()} -> Estoque: {produto['estoque']}')