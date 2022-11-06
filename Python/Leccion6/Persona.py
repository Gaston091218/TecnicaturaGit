class Persona: # Creamos una Clase
    pass # No se procesa nada más (No tiene contenido)
print (type(Persona))


persona1= Persona("Gaston","Riveros",32) #NECESITAMOS ENVIAR ARGUMENTOS
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
#Print( persona1.apellido)
# print(persona1.edad)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")
persona2= Persona("Pepe","Juarez", 35)
print(f"Elobjeto2 de la clase persona: {persona2.nomre} {persona2.apellido} {persona2.edad}"

      #Los atributos son: caracteristicas
# los metodos son : el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()