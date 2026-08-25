# 6. Implementar um programa que calcule o Índice de Massa Corpórea (IMC), dados o peso e a altura informados pelo usuário. A implementação deve usar funções.
# Fórmula do IMC: 
# 7. Crie uma função chamada classificar_imc que receba o IMC e retorne a classificação:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 <= IMC < 25
# Sobrepeso: 25 <= IMC < 30
# Obesidade: IMC >= 30

def calcular_IMC(peso: float, altura: float):
    return peso / (altura * altura)

def classificar_imc(imc: float):
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"


peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = calcular_IMC(peso, altura)

print(f'IMC: {imc:.2f}')
print("Classificação: ", classificar_imc(imc))