# 3. Implementar um programa que imprima todos os números ímpares entre 1 e 50.

for i in range(1, 51):
    if i % 2 == 1:
        print(i)

# Sem verificar se é impar, passar de impar em impar usando o step
for i in range(1, 51, 2):
    print(i)