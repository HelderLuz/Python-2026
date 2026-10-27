def calcula_estatisticas(numeros):
    media = sum(numeros) / len(numeros)
    somatoria = 0

    for numero in numeros:
        somatoria += (numero - media) ** 2

    dp = (somatoria / len(numeros)) ** 0.5

    return media, dp

# numeros = (6, 7, 7, 8, 8, 8, 8, 9, 9, 10)
numeros = (1, 2, 3, 4, 5, 6)
media, dp = calcula_estatisticas(numeros)
print(f'Média: {media}')
print(f'Desvio padrão: {dp:.3f}')