# Ejercicio 3 : Función Recursiva
# Imprimir númerps de 5 a 1 de manera descente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# Valor de 5, debe imprimir:
#
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir :
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada
def imprimir_numeros_recursivos(numero):

    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero -1) # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorreto....')

imprimir_numeros_recursivos(5) # Tarea el numero lo debe ingresar el usuario
