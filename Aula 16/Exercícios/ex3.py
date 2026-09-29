# 3. Escreva uma função chamada remove_duplicatas que receba uma tupla e retorne uma nova tupla sem valores duplicados. A ordem dos elementos na tupla original deve ser mantida.
def remove_duplicatas(tupla):
    unicos = tuple()

    for elemento in tupla:
        if elemento not in unicos:
            unicos += elemento,
    return unicos

tupla = (1, 2, 3, 3, 4, 3, 4, 5, 5, 6, 1, 2, 7)
sem_repetidos = remove_duplicatas(tupla)
print(sem_repetidos)