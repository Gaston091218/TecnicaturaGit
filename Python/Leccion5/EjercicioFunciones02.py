#Ejercicio 2 : Funcion con * args para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo númerico, utilizando argumentos variables *args
# como parámetro de la funcion y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos

# Definimos la funcióin para multiplicar
def multiplicar_valores(*args):
    resultado = 1 # Elcero no nos ayuda a multiplicar
    for numero in  args:
        resultado *= numero
    return resultado

# Llamamos a la función
print(multiplicar_valores(3, 5, 15, 3))# Le pasamos los argumentos