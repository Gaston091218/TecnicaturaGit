# Ejercicio 5 : Convertidor de temperaturas
# Realizar dos funciones apra convertir de grados celsius
# a fahrenheit y viceversa
# Investigar las formulas

# Función que convierte celcius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia : multiplicacion, division y suma

# Función que converte fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respetar la presedencia utilizando parentesis

celsius = float(input("Digite el valor de celsius : "))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado}')

fahrenheit = float(input("Digite el valor de fahrenheit : "))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')
