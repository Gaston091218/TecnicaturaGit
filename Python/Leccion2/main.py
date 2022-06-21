"""
#Esta clase veremos la sentencia if/else
condicion = 10
if condicion == True:
    print("Condición verdadera")
elif condicion == False:
    print("condicion falsa")
else:
    print("Condicion sin especificar")

num = int(input("Digite un numero en el rango entre  el 1 y el 3:"))
numTexto = ""
if num == 1:
    numTexto= "Numero uno"
elif num == 2:
    numTexto = "Numero 2"
elif num == 3 :
    numTexto = "Numero 3"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f"El número ingresado es : {num} , {numTexto}")
"""
condicion = False
#if condicion:
#   print ("Condicion Verdadera")
#else:
#   print("Condicion Falsa")
print("Condicion Verdadrera") if condicion else print("Condicion Falsa")
