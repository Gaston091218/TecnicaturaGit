import math
# "importamos la clase math para hacer uso de la funcionsqrt(raiz cuadrada)
# Dada la siguiente Tupla
tupla =(13,1,8,3,2,5,8) # Deninimos la tupla
#Crear una lista dque solo incluya los numeros menors a 5
#e imprimimos por consola [lista
lista=[] # Definimos la lista
# Filtramos los elementos menores de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
        print(lista)

# Ejercicio de matemáticas
# PARA SACAR LA RAIZ CUADRADAD DE UN NÚMERO POSITIVO

numero = int(input("Digite un número positivo: "))
while numero < 0:
    print("Error -> Deberia ser un número positivo")
    numero = int(input("Digite un número positivo:"))
print(f"\n Su raiz cuadrada es {math.sqrt(numero): 2f}")




