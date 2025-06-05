#Ejercicio 1
#definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# rograma principal
imprimir_hola_mundo()

#Ejercicio 2
#definicion de funciones
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# programa principal
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

#Ejercicio 3
#definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
#definicion de funciones
def calcular_area_circulo(radio):
    PI = 3.1416
    return PI * radio ** 2

def calcular_perimetro_circulo(radio):
    PI = 3.1416
    return 2 * PI * radio

# programa principal
radio = float(input("ingrese el radio del circulo: "))
print("area:", calcular_area_circulo(radio))
print("perimetro:", calcular_perimetro_circulo(radio))


#Ejercicio 5
#definicion de funciones
def segundos_a_horas(segundos):
    return segundos / 3600

# programa principal
seg = int(input("ingrese la cantidad de segundos: "))
print(f"equivale a {segundos_a_horas(seg):.2f} horas")

#Ejercicio 6
#definicion de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
num = int(input("ingrese un número: "))
tabla_multiplicar(num)


#Ejercicio 7
#definicion de funciones
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "division por cero"

# Programa principal
a = float(input("primer numero: "))
b = float(input("segundo numero: "))
suma, resta, mult, div = operaciones_basicas(a, b)

print("suma:", suma)
print("resta:", resta)
print("multiplicacion:", mult)
print("division:", div)


#Ejercicio 8
#definicion de funciones
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# programa principal
peso = float(input("ingrese su peso (kg): "))
altura = float(input("ingrese su altura (m): "))
imc = calcular_imc(peso, altura)
print(f"su IMC es: {imc:.2f}")


#Ejercicio 9
#definicion de funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# programa principal
c = float(input("ingrese la temperatura en celsius: "))
print(f"equivale a {celsius_a_fahrenheit(c):.2f}°F")


#Ejercicio 10
#definicion de funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
n1 = float(input("primer numero: "))
n2 = float(input("segundo numero: "))
n3 = float(input("tercer numero: "))
print(f"el promedio es: {calcular_promedio(n1, n2, n3):.2f}")
