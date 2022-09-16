# Ejercicio 5: Factorial de un número positivo
# HACER UN PROGRAMA PARA CALCULAR EL FACTORIAL DE UN NÚMERO POSITIVO
numero = int(input("Digite un número: "))
while numero < 0: #Mientras el numero sea negativo
    print("Error -> El número tiene que ser positivo")
    numero = int(input("Digite un número: "))
factorial = 1 # La variable para calcular el factorial
for i in range (1, numero+1):
    factorial *= i
print(f"\n El factorial del número {numero} positivo ingresado es :{factorial}")
