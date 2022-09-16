"""#Listas(Arreglos o vectores)
#Colecciones en Python

nombres = ["Matias", "julian","Marcelo","Enzo"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])# Con numeros negativos nos muestra el ultimo elemento empezando desde el final con -1,-2..
print(nombres[-2])
print(nombres[0:2]) # Nos muestra el indice 0 y  1 pero no el 2
#Ir del inicio de la lista al indice, pero sin incluirlo.
print(nombres[:3])#INDICES A MOSTRAR 0,1,2
#Desde el indice mostrado hasta el final
print(nombres[1:])

#Modificamos un Valor dentro de nuestra lista
nombres[2] = "Nicolas"
nombres[1] = "Simon"
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular, la lista el plural
    print (nombre)
else:
    print( "No hay más elementos en la lista")

# Preguntamos cuantos elementos tiene nuestra lista
print(len(nombres))# len es la funcion que nos regresa la cantidad elementos que contiene una lista

#Agregamos un elemento a nuestra lista
nombres.append("Juanfer")# utilizamos la funcion .append para agregar un elemento a la lista
#en este caso el elemento se agrega a la cola de la lista
print(nombres)
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico (.insert)
nombres.insert(1,"Milton")
print(nombres)
nombres.insert(3,"lucas")
print(nombres)

#Agregar más de un elemento a la lista
nombres.extend(["Marcelo ","Franco","Enzo"]) # utilizamos la funcion .extend
print(nombres)

#Eliminamos un elemento
nombres.remove ("Simon")
print (nombres)

#Eliminamos el ultimo elemento
nombres.pop()# Se elimina el ultimo elemento en cola.
print(nombres)

#Eliminamos un indice especifico
del nombres[1] # tambien se utiliza la funcion del para borrar una lista.
print (nombres)

#Eliminar todos los elementos de la lista
nombres.clear()
print (nombres)

#Definimos una Tupla
cocina= ("cuchara", "Cuchillo", "Tenedor")
print (len(cocina))
#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print((cocina)[0])
# Mostrar de manera inversa
print((cocina)[-1])
#Acceder a un rango
print((cocina)[0:2])
#Ejemplo
verduras= ("papa,") # Una tupla necesita auqne sea de un elemento: la coma
#de lo contrario seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=" ")# Usamos end= para eliminar los saltos de lineas

#NO ES UNA BUENA PRACTICA, pero lo siguiente es la conversion de una lista a una tupla
cocinalista=list(cocina)
cocinalista [0]= "plato"
cocina=tuple(cocinalista)
print("\n",cocina)
#
# del cocina
#print(cocina)

#Dada la siguiente tupla
#tupla = (13,1,8,3,2,5,8) # DEFINAMOS LA TUPLA
# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [ 1,3,2]
tupla = (13,1,8,3,2,5,8)
lista=[]
for elemento in tupla:
    if elemento < 5:
         lista.append(elemento)
print(lista)

#Tipo Set
planetas = {'Marte', 'Júpiter','Venus'}
print(planetas)
print(len(planetas)) #Usamos la funcion len (length significa largo)

# Revisar si un elemento existe dentro de set
print('Júpiter' in planetas)

#No se puede agregar un elemento duplicado o repetido en los tipo Set
planetas.add('Tierra') #add es la función utilizada para agregar un elemento
planetas.add('Tierra')
planetas.add('Tierra') # Por más que intente agregarlo varias veces si esta duplicado o ya existe no es posible.
print(planetas)

#Eliminar elementos, puede arrojar un eror si el elemento no existe, hay que observar bien el tipeo
planetas.remove('Júpiter') # La funcion remove  ante un mal ingreso ortografico del elemento presenta error
print(planetas)
planetas.discard('tierra')# Esta funcion no presenta error
print(planetas)

#Limpiar Set
planetas.clear()
print(planetas)

#Eliminar Set
del planetas # luego de eliminarlo si intentamos imprimirlo nos largara un errror

#Diccionarios
#'Messi' : 10 Un diccionario esta compuesto por dos elementos
#Una llave y un valor ( key, value)
diccionario ={
    'IDE': 'Integrated Development Environmet',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificiamos los elementos
diccionario['IDE'] ='Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos de un diccionario
for termino in diccionario:
    print(termino)
for termino, valor in diccionario.items():
    print(termino,valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de un elemento
print('IDE' in diccionario)# devuelve un booleano

# Agregar un elemento a diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento de diccionario
diccionario.pop('SABD')
print(diccionario)

#Vaciar o limpiar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
#del diccionario """

# Concatenar listas
lista1 = [1,2,3,1,2,1]
lista2 =[4,5,6]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7,8,9]) # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función que nos muestra donde se ubica un indice buscado
#print(lista3.index(0)) en este caso al no estar el elemento 0 nos daria un error

# Como ver cuantos elementos o valores repetidos hay en una lista
print("En la lista el número 1 se repite,",lista3.count(1),"veces")
# Cuenta cuantos valores iguales hay dentro de la lista

# Para poner una lista al reves
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = ["a","b","c"] *2
print(lista)

# Métodos de ordenamiento
lista3.sort() # Ordena los elementos de la lista de manera ascendente
print(lista3)

#Para ordenarla de manera descendente
lista3.sort(reverse=True)
print(lista3)

#Repaso de tupla
 #Se pueden ingresar distintos tipos de elementos
tupla=(4,"hola",6.78, [1,2,78],4,"adios")
print(tupla)

print( 4 in tupla)# Accion booleana, su respuesta es tipo booleana
# Lo que podemos usar dentro de tuplas : index, count , len.
# Tambien en tuplas se pueden convertir tuplas a listas y listas a tuplas

#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye" ,}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el numero 3 NO esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve una respuesta tipo booleana

#Operaciones  en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2
print(conjunto3)
conjunto3= conjunto2 - conjunto1
print(conjunto3)

conjunto3= conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre si
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))# acá preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2))#No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 =frozenset # Esto hace que el conjunto  sea totalmente inmutable # No se puede modificar el conjunto


#Repaso Diccionarios
diccionarioNuevo = { "Azul": "Blue","Rojo": "Red", "Verde": "Green","Amarillo": "Yellow"}
print(diccionarioNuevo)

#Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

#Los diccionarios pueden alamacenar diferente tipos de datos
diccionario2 = {"Gaston":{"Edad ": 31, "Altura": 1.84}}
print(diccionario2)

seleccionArgentina = {
    10:{"Nombre": "Lionel Messi"," Edad": 35,"Altura":1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho",},
    11:{"Nombre": "Angel Di Maria"," Edad": 34,"Altura":1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    21:{"Nombre": "Paulo Dybala"," Edad": 28,"Altura":1.77, "Precio": "35 Millones", "Posicion": "Media punta"},
    19:{"Nombre": "Nicolas Otamendi"," Edad": 34,"Altura":1.83, "Precio": "3.5 Millones", "Posicion": "Defensor Central"},
    1:{"Nombre": "Franco Armani"," Edad": 35,"Altura":1.89, "Precio": "3.5 Millones", "Posicion": "Arquero"},
    22:{"Nombre": "Julian Alvarez"," Edad": 22,"Altura":1.70, "Precio": "23 Millones", "Posicion": "Delantero"},
    4: {"Nombre": "Gonzalo Montiel"," Edad": 25,"Altura":1.76, "Precio": "14 Millones", "Posicion": "Lateral Derecho"},
    6:{"Nombre": "Germán Pezzela"," Edad": 31,"Altura":1.87, "Precio": "5 Millones", "Posicion": "Defensor Central"},
    13:{"Nombre": "Cristian Romero"," Edad": 24,"Altura":1.85, "Precio": "48 Millones", "Posicion": "Defensor Central"},
    14: {"Nombre": "Exequiel Palacios"," Edad": 23,"Altura":1.77, "Precio": "15 Millones", "Posicion": "Volante Central"},
}
for llave in seleccionArgentina:
    print(llave)
for valor in seleccionArgentina:
    print(valor)
for llave, valor in seleccionArgentina.items():
    print(llave,valor)
#Como tarea agregar 4 jugadores más al diccionario: seleccionArgentina
print("Tenemos cargados en el diccionario la cantidad de jugadores:", end=" ")
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1,2,3]

#Agregar elemetnos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop( )#Quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento: {elementoBorrado}")
print(f"La pia ahora quedo así: {pila}")

#Colas con listas
#Estrucutra de datos tipo fifo( first input / first output)
cola = ["Gaston","Diego", "Fer","Maxi"]

#Agregamos elementos al final de la cola
cola.append("Marina")
cola.append("lorena")
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(cola)
seRetira = cola.pop(0)
print(cola)
seRetira = cola.pop(0)
print(cola)
seRetira = cola.pop(0)
print(cola)
seRetira = cola.pop(0)
print(f"No quedan mas clientes ")

#############################################
# Recorremos el Diccionario seleccionArgentina(otra forma)

for i in seleccionArgentina:
    print(f"\n {i} ---> {seleccionArgentina[i]}")






