# 4. Crie uma função iniciais(nome_completo) que receba uma string com um nome completo e retorne as iniciais de cada nome.

def iniciais(nome_completo: str):
    nomes = nome_completo.split()
    inicial = []

    for nome in nomes:
        inicial.append(nome[0])
        # inicial += nome[0]

    return inicial

print(iniciais('Helder Jefferson Ferreira da Luz'))