# 7. Dada a seguinte lista de dicionários:
carros = [
    {"marca": "Toyota", "modelo": "Corolla", "ano": 2020},
    {"marca": "Honda", "modelo": "Civic", "ano": 2018},
    {"marca": "Ford", "modelo": "Focus", "ano": 2019}
]
# Realize as seguintes tarefas:
# - Adicione um novo carro à lista.
# - Exiba os carros fabricados após 2018.

carros.append({'marca': 'Fiat', 'modelo': 'Fastback', 'ano': 2025})

for carro in carros:
    if carro['ano'] > 2018:
        marca, modelo, ano = carro.values()
        print(f'Marca: {marca} | Modelo: {modelo} | Ano: {ano}')