aliens = [
    {'cor': 'verde', 'pontos': 5},
    {'cor': 'amarelo', 'pontos': 10},
    {'cor': 'vermelho', 'pontos': 15}
]

for alien in aliens:
    # print(f'Cor: {alien['cor']} \nPontos: {alien['pontos']}\n')
    for cor, pontos in alien.items():
        print(f'Cor: {cor} \nPontos: {pontos}\n')
        
