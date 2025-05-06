#ejercicio 1
for i in range(101):
    print(i)


#ejercicio 2
num = int(input("ingrese un numero entero "))
i = 0
while num > 0:
    num = num // 10
    i += 1
print(f"el numero tiene {i} digitos")


#ejercicio 3
num1 = int(input("Introduce el primer numero "))
num2 = int(input("Introduce el segundo numero "))
if num1 >= num2:
    print("El valor del primer numero debe ser menor que el segundo numero")
else:
    suma = sum(range(num1 + 1, num2))
    print(f"La suma de los números entre {num1} y {num2} (excluyéndolos) es: {suma}")



#ejercicio 4
total = 0
numero = int(input("Ingresá un número entero (0 para terminar): "))
while numero != 0:
    total += numero
    numero = int(input("Ingresá otro número (0 para terminar): "))
print(f"La suma total de los números ingresados es: {total}")


#ejercicio 5
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
adivino = False
print("¡Adiviná el número entre 0 y 9!")
while not adivino:
    numero = int(input("Ingresá tu intento: "))
    intentos += 1
    if numero == numero_aleatorio:
        adivino = True
    else:
        print("Incorrecto. Probá de nuevo.")
print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")


#ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


#ejercicio 7
numero = int(input("Introduce un número entero positivo: "))
while numero <= 0:
    print("Debes introducir un número entero positivo")
    numero = int(input("Introduce un número entero positivo: "))
total = sum(range(numero))
print(f"La suma de los números desde 0 hasta {numero - 1} es: {total}")



#ejercicio 8
numeros = 5
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f"Vas a ingresar {numeros} números enteros:")
for i in range(numeros):
    numero = int(input(f"Número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")



#ejercicio 9
cantidad_numeros = 5
suma = 0
print(f"Ingresá {cantidad_numeros} números enteros:")
for i in range(cantidad_numeros):
    numero = int(input(f"Número {i + 1}: "))
    suma += numero
media = total / cantidad_numeros
print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")



#ejercico 10
numero = int(input("Ingresá un número entero: "))
# Invertir los dígitos
invertido = int(str(numero)[::-1])
# Mostrar el resultado
print(f"El número invertido es: {invertido}")
