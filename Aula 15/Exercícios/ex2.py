# 2. Crie uma função substituir(frase, antiga, nova) que receba uma frase e substitua todas as ocorrências de uma substring específica por outra.

def substituir(frase: str, antiga: str, nova: str):
    return frase.replace(antiga, nova)

print(substituir('o esquilo está com pneumonia', 'o', 'Y'))
print(substituir('Crie uma função substituir(frase, antiga, nova) que receba uma frase e substitua todas as ocorrências de uma substring específica por outra.', 'frase', 'SUBSTITUIDO'))