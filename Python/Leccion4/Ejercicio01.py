##  Ejercicio 01 : Llenar una lista
## LLENAR UNA LISTA CON LOS NUMEROS DEL 1 AL 50, LUEGO MOSTRAR LA LISTA CON EL BUCLE FOR,
## los elementos deben mostrarse de la siguiente forma:
# 1,2,3,4,5....50

lista =[]
i = 1
while i <=50 :
    lista.append(i)
    i += 1
for i in lista:
    print(i, end='-')

#Algoritmo eficaz, en vez de 5 lineas tenemos una que cumple la misma funcion
##lista =list(range(1,51))
##for i in lista:
 ##   print(i, end='-')

