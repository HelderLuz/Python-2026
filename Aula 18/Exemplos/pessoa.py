dicionario = {
    "nome": "João", 
    "idade": 20, 
    "curso": "Engenharia"
}

# print(dicionario.values())

for chave in dicionario:
    print(chave, dicionario[chave])

for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(chave, valor)

# # Verificar se uma chave existe
# if "nome" in dicionario:
#     print("A chave 'nome' existe!")
# if "endereço" not in dicionario:
#     print("A chave 'endereço' não existe!")

# if "João" in dicionario.values():
#     print("O valor 'João' está no dicionário!")