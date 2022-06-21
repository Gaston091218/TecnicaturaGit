# Ejercicio: Etapas de la vida segun la edad
edad = int(input("Digite su edad:"))
mensaje = None
if 0 <= edad < 10: #Sintaxis simplificada
    mensaje = "la infancia es divertida disfrutala"
elif 10 <= edad < 20:
    mensaje = "La adolescencia es una etapa de muchos cambios"
elif 20 <= edad < 30:
    mensaje = " Bienvenido a la adultez"
elif 30 <= edad < 50:
    mensaje = "Si no encontraste el camino no te preocupes, seguí intentando"
elif 50 < edad < 100 :
    mensaje = "Dale a tu sabiduraria ganada un buen uso"
else:
    mensaje = "Si superaste los 100 años felicidades! Esperemos haya sido una buena vida!"
print(f"Tu edad es : {edad} , {mensaje}")