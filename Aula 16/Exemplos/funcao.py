def listar_nomes(*nomes):
    print(type(nomes))
    for nome in nomes:
        print(nome)

listar_nomes('José', 'Maria', 'Marcos')
