def distancia_euclidiana(ponto1, ponto2):
    x1, y1, z1 = ponto1
    x2, y2, z2 = ponto2

    distancia = ( (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 ) ** 0.5

    return distancia

a = (4, -8, -9)
b = (2, -3, -5)

print(f'Distância dos pontos A {a} e B {b} é {distancia_euclidiana(a, b):.2f}')