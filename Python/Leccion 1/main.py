
''' #se utiliza 3 comillas para crear comentarios extensos 
hola= "Hola mundo"
print(hola)
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)
# literales
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escribem x y los tres ultimos numeros de la dirreccion de memoria#
print(id(y))
print(id(z))

# Clase 3 Tipos de datos en python

a = "Hola alumnos"
print(type(a))
# str = tipo cadena , float= tipo flotante, int = tipo entero , Type indica clase de variable
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola almunos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))

# Manejo de cadenas (string)
migrupofavorito = "AC/DC"
caracteristicas = "The best rock band"
print("Mi grupo favorito es:", migrupofavorito, ",", caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))  # se puede sumar 2 cadenas siempre que sea un numero

# Tipos Booleanos (bool)
miBooleano = True
print(miBooleano)
miBooleano2 = 3 < 2
print(miBooleano2)
if miBooleano2:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
# Procesar la entrada del usuario
nombre = str(input("Cual es su nombre:")  # regresa un dato tipo string
print("Tu nombre es:", nombre)

# Conversion de la entrada de datos
numero3 = int(input("Escribe el primer numero:"))
numero4 = int(input("Escribe el segundo numero:"))
resultado2 = numero3 + numero4
print("El resultado de la suma es:", resultado2)

#Ejercicio1
pregunta = int(input("Como estuvo tu dia del 1 al 10:"))
print("Mi dia estuvo de:",pregunta)

#Ejercicio 2
titulo =input("Proporciona el titulo del libro:")
autor = input("Prpoporciona el autor del libro:")
print(titulo, "fue escrito por", autor)
'''
"""
# Clase 4 Operadores
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("El resultado de la suma es:", suma)
resta = operandoA - operandoB
print(f"El resultado de la resta es:{resta}") #interpolacion
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")
division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB # la doble barra me genera un resultado entero en la division
print(f"El resultado de la división (int) es : {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo ( modulo) es {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es : {exponente}")
# Ejercicio rectangulo
alto = int(input("ingrese alto del rectangulo:"))
ancho = int(input("ingrese ancho del rectangulo"))
area = alto * ancho
perimetro = (area + alto) *2
print("El area del rectangulo es:", area)
print("El perimetro del rectangulo es : ", perimetro)

# Operadores de reasignacion
miVariable3 = 10
print(miVariable3)
miVariable3= miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)
#miVariable3 = miVariable3 -2
miVariable3 -= 2
print(miVariable3)
#miVariable3 *= 2
miVariable3 *= 2
print(miVariable3)

# Operadores de comparacion

d = 4
c = 2
resultado= d==c # comparamos si son iguales
print(resultado)
# Menor igual
resultado2 = d=<c
print(resultado2)
# Mayor igual
resultado3 = d >= c
print(resultado3)
# Distinto que
resultado4 = d != c
print(resultado4)

# Ejercicio Numero par o impar
num = int(input("Ingrese un numero:"))
if num%2 == 0:
    print("Es par")
else:
    print("Es impar")
#Ejercicio determinar si es mayor de edad
edad = int(input("Ingrese su edad:"))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
# And, or y Not
a = True
b = True
c = False
resultado  = a and b
print(resultado)
resultado2 = a or c
print(resultado2)
resultado3 =a and c
print(resultado3)
resultado4 = not c
print(resultado4)

# Ejercicio: Valor dentro de un rango
valor = float(input("Digite un numero dentro del rango  0 a 5:"))
valorminimo = 0
valormaximo = 5
dentrorango = valor >= valorminimo and valor <= valormaximo
if dentrorango:
    print(f" El varlor {valor} esta dentro del rango")
else:
    print (f"El valor {valor} No esta dentro del rango")

# Ejercicio edad dentro de un rango
edad= int(input(" introduzca su edad : "))
veinte= edad>= 20 and edad <=30
treinta= edad= 30 and edad <= 40
if veinte or treinta:
    print ("Su edad esta dentro del rango de los veinte y/o treinta")
else:
    print (" Edad fuera del rango")

# Ejercicio El mayor de dos numeros
num1 = int(input("ingrese el valor del numero 1:"))
num2 = int(input("Ingrese el valor del numero 2:"))
if num1 > num2:
    print("El numero 1 es mayor")
else:
    print("EL numero 2 es mayor")
# Ejercicio : Tienda de libros
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro:")
id = int(input("Digite el ID del libro:"))
precio = float(input("digite el precio del libre: "))
envioGratuito = input("Indicar si el envio es Gratuito, SI/ NO:")
if envioGratuito == "SI":
    envioGratuito = "SI"
elif envioGratuito == "NO":
    envioGratuito = "NO"
else: envioGratuito = "El valor ingresado es incorrecto debe ingresar si/ no"
print(f'''
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envio gratuito? : {envioGratuito}
''')
"""
