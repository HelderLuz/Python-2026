# 5. Escreva uma função chamada converter_celsius_fahrenheit que converta temperatura de Celsius para Fahrenheit. Fórmula: 

def converter_celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input('Digite a temperatura em ºC: '))
fahrenheit = converter_celsius_fahrenheit(celsius)

print(f'{celsius}ºC equivale a {fahrenheit}ºF')