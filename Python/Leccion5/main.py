# Comenzamos con Funciones
# Definimos una función
def mi_funcion(): # No se puede llamar antes de definir a una función
    print('Saludos a todos los alumnos de la Tecnicatura')
    print()
print()# Este print esta fuera de lo que es la funcion

mi_funcion()# Estamos llamando a la función

# Desemmpaquetado de listas olistas unpacking

def show(name,lastName):
    print(name+' '+lastName)
persona = ["Gaston", "Riveros"]
show(persona[0], persona[1]) #Pasamos un por uno los datos de la lista a la funcion
show(*persona) # Esto es lo mismo que lo anterior pero le estamos pasanto TODO JUNTO
persona2 = ("pepe", "sanchez") # desempacamos a traveés de una tupla
show(*persona2)
persona3 = {"lastName": "gallardo", "name": "marcelo"}
show(**persona3)

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se terminó")

# list comprehension , lista de compresión
names = ["paolo", "rodrigo", "lupe", "pepe"]
alongP = [p for p in names if p[0] == "p"] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "quilmes", "country": "Arg"},
           {"name":"Corona", "country": "Mx"},
           {"name": "Stella Artois", "country":"Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos ( funciones)
def mi_funcion2(name, lastname):
    print("Saludos a todos los que ven a través del canal de youtube")
    print(f"Nombre: {name}, Apellido: {lastname}")
    mi_funcion2("Jorge","Lucero")
    mi_funcion("Ariel", "Betancud")
    mi_funcion("Analia", "Pedrosa")

# La palabra return en funciones
# Creamos una función para sumar

def sumar(a,b):
    return a + b
resultado = sumar(78,22)
print(f'El resultado de la suma es: {resultado}')

def sumar2(a: int = 0,b: int = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma : {resultado}')
print(f'Resultado de la suma: {sumar2(22,66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas','José','Claudia','Rosa','Maria')
listarNombres('Matias','Soledad','Kratos','Romina', 'Messi')

def listarTerminos(**terminos): # LOS MÁS UTILIZAOD ES **KWARGS PARA RECIBIR LOS ARGUMENTOS
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')
listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE = 'Intergrated Develoment Enviroment' , PK = 'Primary Key')
listarTerminos(Nombre = 'Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 10) # No es un objeto iterable
desplegarNombres((10, 11))# La convertimos a una tupla. en un soo elemento no olvidar la coma
desplegarNombres([22, 55 ]) # La convertimos en una lista

# Funcion Recursivas

def factorial (numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero- 1) # Caso Recursivo
numeroFactorial = int(input("Digite el numero para calcular el factorial: "))
resultado = factorial(numeroFactorial) # Lo hacemos en código duro
print(f'Él factorial del número {numeroFactorial} es : {resultado}') # Tarea que el usuario ingrese el número para cálcular el factorial





