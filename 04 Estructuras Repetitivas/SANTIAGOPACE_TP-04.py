#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for y in range (0,101): #va de forma creciente hasta 100 
    print(y)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Hola usuario, ingrese un número: "))
#lo vamos a convertir en positivo si es negativo
numero = abs(numero)  

#iniciamos el contador en 0
contador = 0 

#Vamos a recorrer cada caracter del numero convertido a texto mediante str
for digito in str(numero):
    contador += 1

print(f"El número tiene {contador} dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

primer_num = int(input("Hola usuario ingrese el primer numero: "))
segundo_num = int(input("Ingrese el siguiente: "))

menor = min(primer_num, segundo_num)
mayor = max(primer_num, segundo_num)

suma = 0

for i in range (menor + 1, mayor):
    suma += i

print(f"El resultado es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

var_num = int(input("Ingrese un número entero: "))
#Iniciamos variable del resultado en 0 
sumatoria = 0


while var_num != 0:  
    if var_num != 0:  
        sumatoria += var_num
        print(f"El total es {sumatoria}")
    
    var_num = int(input("Ingrese un número entero (0 para terminar): "))

print(f"El total final de la suma es {sumatoria}") #Muestro el resultado final de la suma mas limpio



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  #funcion import en python para generar un numero aleatorio

numero_aleatorio = random.randint(0, 9)

var_true = 0
intentos = 0

while var_true == 0:
    numero_usuario = int(input("Adivina un numero entre 0 y 9: "))
    intentos += 1  #se aumenta el contador de intentos y luego lo mostramos en pantalla

    #verificamos si el número ingresado es correcto
    if numero_usuario == numero_aleatorio:
        print(f"Correcto, adivinaste el número en {intentos} intentos.")
        break  #salimos del bucle 
    elif numero_usuario < numero_aleatorio:
        print("El numero es mayor. Intenta de nuevo.")
    else:
        print("El numero es menor. Intenta de nuevo.")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.


for n in range(100, -1, -2):
    print(n)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.


num = int(input("Hola usuario ingrese un numero: "))
suma = 0

for i in range(1, num+1):
    suma += i

print(f"La suma de los numeros del 1 al {num} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0


for n in range(100):
    var_num = int(input("Ingrese numero: "))
    if var_num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

    if var_num > 0:
        num_positivos += 1
    elif var_num < 0:
        num_negativos += 1

print(f"Los numeros pares son: {num_pares}")
print(f"Los numeros impares son: {num_impares}")
print(f"Los numeros positivos son: {num_positivos}")
print(f"Los numeros negativos son: {num_negativos}")
        
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma = 0
cantidad_numeros = 5 #Cambia segun el rango que se quiera calcular

for n in range (cantidad_numeros):
    var_promedio = int(input("Ingrese numero: "))
    suma += var_promedio
    
promedio_total = (suma / cantidad_numeros)
print(f"El resultado es {promedio_total}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num_invertir = input("Ingrese un número: ")
num_invertido = ""

for digito in num_invertir:
    num_invertido = digito + num_invertido 

print(f"Número invertido: {num_invertido}")