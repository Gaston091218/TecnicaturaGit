# Ejercicio 8 : Menú Interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con
# un saldo inicial de 1000$ y tendrá el siguiente enú de opciones:
#       1.INGRESAR DINERO EN LA CUENTA
#       2. Retirar dinero de la cuenta
#       3. Mostrar dinero disponible
#       4. Salir

saldo = 1000
while True :
    print("\t.:MENÚ:.")
    print("1. INGRESAR DINERO EN LA CUENTA")
    print("2. RETIRAR DINERO DE LA CUENTA")
    print("3. MOSTRAR DINERO DISPONIBLE")
    print("4. SALIR")
    opcion = int(input("Digite una opcion de menú:"))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar ->  "))
        saldo += extra
        print(f"Dinero en la cuenta al momento : $ {saldo}")
    elif opcion == 2:
        retirar = float(input("cuanto dinero desea retirar -->  "))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print (f"Dinero en la cuenta al momento: $ {saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automatico, hasta pronto")
        break
    else :
        print("Error, se equivoco de opción de menú")
        print()







