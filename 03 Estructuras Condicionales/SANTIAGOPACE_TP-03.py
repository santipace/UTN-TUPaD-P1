##1)Ejercicio 1

edad_usuario = int(input("Hola usuario ingrese su edad: "))

##Verifico si la edad ingresada por el usuario es mayor que 18
if edad_usuario > 18:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")

##2)Ejercicio 2

nota_alumno = int(input("Hola usuario ingrese su nota: "))

##Verifico que la nota del alumno sea mayor o igual que 6
if nota_alumno >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

##3)Ejercicio 3

numero = int(input("Hola usuario ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Error, porfavor ingrese un numero par")

##4)Ejercicio 4

edad = int(input("Hola usuario ingrese su edad: "))

##Voy verificando cual es la edad ingresada para informarle al usuario a que categoria pertenece
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

##5)Ejercicio 5

contraseña = input("Ingrese su contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


##6)Ejercicio 6

import random
from statistics import mean, median, mode


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


media_valor = mean(numeros_aleatorios)      
mediana_valor = median(numeros_aleatorios)  
moda_valor = mode(numeros_aleatorios)       

#Imprimo los resultados para poder analizarlos
print("Lista generada:", numeros_aleatorios)
print("Media:", media_valor)
print("Mediana:", mediana_valor)
print("Moda:", moda_valor)


if media_valor > mediana_valor > moda_valor:
    print("Hay un sesgo positivo (a la derecha).")
elif media_valor < mediana_valor < moda_valor:
    print("Hay un sesgo negativo (a la izquierda).")
elif media_valor == mediana_valor == moda_valor:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar un sesgo claro con estos valores.")

##7)Ejercicio 7
texto = input("Hola usuario ingrese una frase o palabra: ")

if texto[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
    texto += '!'

print(f"El resultado es:{texto}")

##8)Ejercicio 8

nombre = input("Hola usuario ingrese su nombre: ")


print("¿Cómo querés que se muestre tu nombre?")
print("1: En mayúsculas")
print("2: En minúsculas")
print("3: Con la primera letra en mayúscula")

##Le digo al usuario que ingrese una opción 
opcion = input("A continuación elegí una opción 1, 2 o 3: ")

if opcion == "1":
    print(f"Tu nombre en mayúsculas es:{nombre.upper()}") 
elif opcion == "2":
    print(f"Tu nombre en minúsculas es:{nombre.lower()}")
elif opcion == "3":
    print(f"Tu nombre con la primera letra en mayúscula es:{nombre.title()}")
else:
    print("Porfavor, ingrese una opción valida.") ##Si no ingresa 1, 2 o 3 mostrara que es una opción invalida

##9)Ejercicio 9

magnitud = float(input("Hola usuario ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Mayor o igual que 7: Extremo (puede causar graves daños a gran escala)")
else:
    print("Porfavor ingrese una opción valida")

#10)Ejercicio 10

hemisferio = input("Hola usuario ingrese en que hemisferio se encuentra N/S:").upper()
mes=int(input("Ingrese el mes en numeros(1 a 12):"))
dia = int(input("Y ahora ingrese el dia(1 a 31):"))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"

else:
    estacion = "Hemisferio no válido"

print(f"La estación del año es: {estacion}")