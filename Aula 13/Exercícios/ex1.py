# 1. Escreva uma função em Python que calcule a área de um triângulo.
def area_triangulo(base: float, altura: float):
    """
    Calcula a área do triangulo.

    Parâmetros:
    - base: Comprimento da base do triângulo
    - altura: Altura do triângulo

    Retorno:
    - A área do triângulo
    """
    return (base * altura) / 2

def base_altura():
    base = float(input('Digite a base do trângulo: '))
    altura = float(input('Digite a altura do trângulo: '))
    return base, altura

base, altura = base_altura()
print(f"A área do triângulo base {base} altura {altura} é {area_triangulo(base, altura)}")
base, altura = base_altura()
print(f"A área do triângulo base {base} altura {altura} é {area_triangulo(base, altura)}")