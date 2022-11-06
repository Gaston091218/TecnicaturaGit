# Ejercicio 9 : Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese esa frase,
# se le devolverá la misma frase pero sin espacios en blanco, y
# ademas un contador de cuantoas caracteres tiene la frase
#(Sin contar los espacios en blanco)
# Ejemplo : Frase = vivir por siempre en paz
#            Frase final = vivirporsiempreenpaz
#            N° de Caracteres = 21
frase1 = input("Digite una frase:  ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\n Frase final: {frase1}")
print(f"N° de caracteres: {len(frase1)}")
