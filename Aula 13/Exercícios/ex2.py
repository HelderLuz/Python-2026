# 2. Escreva uma função em Python que verifique se um número é par ou ímpar.

def par_impar(numero: int):
    if numero % 2 == 0:
        return "Par"
    
    return "Ímpar"

numero = int(input("Digite um número: "))
print(f"O número {numero} é {par_impar(numero)}")