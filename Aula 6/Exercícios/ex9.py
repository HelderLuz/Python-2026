# Solicite ao usuário que insira uma temperatura em graus Celsius e converta para Fahrenheit usando a fórmula .

celsius = float(input('Digite a temperatura (Celsius): '))
fahrenheit = 9 / 5 * celsius + 32

print(f'{celsius}°C é equivalente a {fahrenheit}°F')