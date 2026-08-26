frutas = ['🍎', '🍌', '🍊', '🍉', '🍉']
tamanho = len(frutas)

frutas.insert(1, '🍉')

indice = frutas.index('🍌')
frutas[indice] = '🍍'

print(f'A 🍉 aparece {frutas.count('🍉')} vezes.')

# for i in range(0, 3):
#     fruta = input('Digite uma fruta: ')
#     frutas.append(fruta)

frutas.reverse()
print(frutas)

