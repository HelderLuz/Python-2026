# 10. Escreva uma função chamada calcular_preco_final que receba o valor de uma compra e retorne o preço descontado com:
# 10% de desconto se valor >= 1000
# 5% de desconto se valor >= 500
# Sem desconto se valor < 500

def calcular_preco_final(valor: float):
    if valor >= 1000:
        return valor - (valor * 0.1)
    if valor >= 500:
        return valor - (valor * 0.05)
    return valor

print(f'Valor da compra R$ 1500.00. \nValor com desconto: R$ {calcular_preco_final(1500):.2f}')
print(f'Valor da compra R$ 500.00. \nValor com desconto: R$ {calcular_preco_final(500):.2f}')
print(f'Valor da compra R$ 499.00. \nValor com desconto: R$ {calcular_preco_final(499):.2f}')