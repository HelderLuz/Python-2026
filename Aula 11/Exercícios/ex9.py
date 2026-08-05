# 9. Implementar um programa que simule um sistema de caixa de supermercado. O programa deve solicitar a quantidade e o valor unitário de cada produto. Esse processo deve ser repetido até que o usuário informe a palavra “fim”. Após a entrada da palavra “fim”, o programa deve exibir o valor total da compra.

total = 0
qtd = ''
valor = ''

while qtd.casefold() != 'fim' and valor.casefold() != 'fim':
    qtd = input('Digite a quantidade: ')

    if qtd.casefold() != 'fim':
        valor = input('Digite o valor: ')

        if valor.casefold() != 'fim':
            total += int(qtd) * float(valor)

print(f'Total: R$ {total:.2f}')