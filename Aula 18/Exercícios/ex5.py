# 5. Crie um programa que simule um tradutor simples usando um dicionário. O dicionário deve conter algumas palavras em português como chave e suas traduções para inglês como valores.
# - Peça ao usuário para digitar uma palavra em português.
# - Verifique se a palavra está no dicionário e exiba a tradução.
# - Caso contrário, informe que a palavra não foi encontrada.

dicionario = {
    'fogo': 'fire',
    'água': 'water',
    'terra': 'earth',
    'vento': 'wind'
}

palavra = input('Digite a palavra em português: ')

if palavra.casefold() in dicionario:
    print(f'A palavra "{palavra}" está no dicionário. Tradução: {dicionario[palavra.casefold()]}')
else:
    print(f'A palavra "{palavra}" não foi encontrada no dicionário.')
