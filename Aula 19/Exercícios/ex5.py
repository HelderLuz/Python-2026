# 5. Crie uma lista de dicionários com informações de livros. Cada dicionário contém título, autor, ano de publicação e gênero. Permita ao usuário pesquisar por um livro pelo título e exiba todas as informações dele, ou uma mensagem caso o livro não seja encontrado.

livros = [
    {
        'titulo': 'Mistborn: O Império Final',
        'autor': 'Brandon Sanderson',
        'ano_publicacao': 2025,
        'genero': 'Fantasia'
    },
    {
        'titulo': 'A Morte de Ivan Ilitch',
        'autor': 'Liev Tolstói',
        'ano_publicacao': 2023,
        'genero': 'Ficção'
    },
    {
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
        'ano_publicacao': 2015,
        'genero': 'Fantasia'
    },
]

entrada_usuario = input('Digite o título do livro: ')

encontrado = False
for livro in livros:
    titulo, autor, ano_publicacao, genero = livro.values()
    if entrada_usuario.casefold() in titulo.casefold():
        print(f'Título: {titulo} \nAutor: {autor} \nAno publicação: {ano_publicacao} \nGênero: {genero}')
        encontrado = True

        
if not encontrado:
    print('O livro não foi encontrado!')