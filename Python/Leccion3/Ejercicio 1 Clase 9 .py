#Clase 9
opcion= 1
print ("Comprobamos que año es Bisiesto")
while opcion == 1:
    num = int (input ("Digite un año:"))
    if (num % 4 == 0) and (num% 100 != 0) or (num % 400 == 0):
        print (f"¡El año {num} es Bisiesto!")
        opcion = int(input ("Para seguirr adelante digite la opcion1:"))
    else:
        print (f"¡El año {num} no es Bisiesto!")
        opcion = int(input("Para seguir adelante digite la opcion 1:"))
