#Ejercicio 11 : Agenda Telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuarios y el valor
#sea el telefono, el prograa tendrá el siguiente menú de opciones:
#             1. Nuevo contacto
#             2. Borrar contacto
#             3. Ver contactos existentes
#             4. Salir

agenda = {}
while True:
    print('\t.:Menu:.')
    print('1. Nuevo contacto ')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opcion de menú'))
    if opcion == 1:
        nombre =input('Digite el nobre del contacto: ')
        telefono = input('Digite el numero del teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente! ')
        else:
            print('Este nombre d econtacto existe')
    elif opcion ==2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for  clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else:
        print('Se equivoco de opción de menú')
        print()




