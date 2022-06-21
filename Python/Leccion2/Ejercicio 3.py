# Ejercicio calcular la estacion del año
mes = int(input("Digite eun mes del año ( 1 -12 ):"))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = "Verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "Otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "Invierno"
elif mes == 10 or mes == 11 or mes == 12:
    estacion == "Primavera"
else:
    estacion = "Error, no existe mes con ese numero digitado"
print(f"Para el mes {mes} la estacion correspondiente es : {estacion}")

