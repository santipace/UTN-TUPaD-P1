# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

#Llamo a la funcion
imprimir_hola_mundo()

print("/////////////////////////////////////")

# 2. Crear  una  función  llamada  saludar_usuario(nombre)  que  reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Programa principal
imprimir_saludo = saludar_usuario(input("Ingrese su nombre: "))
print(imprimir_saludo)

print("/////////////////////////////////////")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima:  “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta funcion con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

imprimir_info = informacion_personal(nombre, apellido, edad, residencia)

print("/////////////////////////////////////")

# 4. Crear dos funciones: calcular_area_circulo(radio)
#  que reciba el radio como parámetro y devuelva el área del círculo.
#  calcular_perimetro_circulo(radio)
#  que reciba el radio como parámetro y devuelva el perímetro del círculo.
#  Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14 * 2 ** 2
def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

print("/////////////////////////////////////")

# 5. Crear una función llamada segundos_a_horas(segundos)
# que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))

#Calculo las horas
resultado_de_horas = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos equivalen a {resultado_de_horas:.2f} horas.")

print("/////////////////////////////////////")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero_ingresado = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

tabla_multiplicar(numero_ingresado)

print("/////////////////////////////////////")

# 7. Crear  una  función  llamada  operaciones_basicas(a,  b)  
# que  reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por 0"
    return(suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

print("/////////////////////////////////////")

# 8. Crear una función llamada calcular_imc(peso, altura) 
# que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
resultado_imc = calcular_imc(peso, altura)

print(f"Su indice de masa corporal (IMC) es: {resultado_imc:.2f}")

print("/////////////////////////////////////")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_celsius = float(input("Hola, ingrese la temperatura en grado celsius: "))

temp_a_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C equivalen a {temp_a_fahrenheit:.2f}°F")

print("/////////////////////////////////////")

# 10.Crear una función  llamada calcular_promedio(a,  b, c)  que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

prom = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres numeros es {prom:.2f}")