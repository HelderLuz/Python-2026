# 2. Crie uma função que receba uma tupla com 3 números e retorne a soma e a média desses números. Descompacte a tupla retornada em variáveis separadas e exiba os resultados.

def soma_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media

# tupla = (10, 20, 30)
tupla = tuple()
for i in range(3):
    num = int(input('Digite o número: '))
    tupla += num,
soma, media = soma_media(tupla)
print(f'Soma: {soma} \nMédia: {media}')