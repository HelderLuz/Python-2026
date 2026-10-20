alien = {
    'cor': 'verde', 
    'pontos': 5
}

print(alien['cor']) # acessa o valor da chave cor
print(alien.get('tamanho'))
alien['posicao_x'] = 0
alien['posicao_y'] = 25
alien['cor'] = 'vermelho'
print(alien)

del alien['cor']
valor_removido = alien.pop('pontos') # retorna o valor removido
print(alien)
