# 3. Crie um dicionário com informações sobre um livro, incluindo título, autor, número de páginas e ano de publicação. Imprima cada informação separadamente.

livro = {
    'titulo': 'O nome do vento',
    'autor': 'Patrick Rothfuss',
    'paginas': 656,
    'ano_publicacao': 2009
}

for chave, valor in livro.items():
    print(f'{chave.title()}: {valor}')