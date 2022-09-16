#Ejercicio 03 : INSERTAR ELEMENTOS Y ORDENARLOS
#Pedir números y meterlos en una lista, cuando el usuario
# Introduzca un número 0, nuestro programa dejaria de insertar.
# Por ultimo, mostrar los números ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input("Digite un número: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista esta ordenada con esta función
print(f"\n Lista ordenada : \n {lista}")

