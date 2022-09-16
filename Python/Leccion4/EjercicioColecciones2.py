# Ejercicio 2: OPERACIONES DE CONJUNTOS CON LISTAS
# Escriba un programa que tenga  2 listas y que acontinuacion
# cree las siguientes listas ( en las que no deben haber repetición)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

# Resolucion
lista1 =["pepe","juan","marcelo","ale","julian"]
lista2 = ["julian","marcelo","marina","lorena",]
print( f"lista 1:","\n",lista1,"\n","lista2:", "\n",lista2)
conjunto1= set(lista1)
conjunto2 = set(lista2)
pto1= list(conjunto1 | conjunto2)
print(pto1)
pto2= list(conjunto1 - conjunto2)
print(pto2)
pto3= list(conjunto2 - conjunto1)
print(pto3)
pto4= list(conjunto1 & conjunto2)
print(pto4)
