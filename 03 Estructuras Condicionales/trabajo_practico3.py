#solicitamos al usuario que ingrese su edad"
edad = int(input("ingrese su edad: "))
#verificamos si es mayor de edad
if edad > 18:
    print("Es mayor de edad")


#le pedimos al usuario que ingrese su nota
nota = int(input("ingrese su nota: "))
#comprobamos si aprobo o desaprobo
if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado!")


#le pedimos al usuario que ingrese un muero
numero = int(input("ingrese un numero"))
#verificamos si el numero es pas
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#le solicitamos al usuario que ingrese su edad
edad = int(input("ingrese su edad: "))
if edad < 12:
    print("usted es un/a niño/a.")
elif edad >= 12 and edad < 18:
    print("ustedes es adolecente.")
elif edad >= 18 and edad < 30:
    print("usted es adulto/a joven.")
else:
    print("usted es adulto/a.")


# Solicitar al usuario que ingrese una contraseña
contraseña = input("Ingresá una contraseña: ")
# Verificamos si la longitud esta entre 8 y 14 caracteres inclusive
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


import random
from statistics import mode, median, mean
# crear una lista de 50 numeros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# calcular los valores estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
# mostrar los resultados
print("numeros aleatorios:", numeros_aleatorios)
print("media:", media)
print("mediana:", mediana)
print("moda:", moda)
# determinar el tipo de sesgo
if media > mediana > moda:
    print("sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("sin sesgo")
else:
    print("distribución sin un sesgo claro")


# solicitar una frase o palabra al usuario
texto = input("ingresa una frase o palabra: ")
# erificar si termina en vocal (mayuscula o minuscula)
if texto.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    texto += '!'
# Imprimir el resultado
print(texto)


# solicitar el nombre al usuario
nombre = input("ingresa tu nombre: ")
# mostrar las opciones
print("elegi una opcion:")
print("1 - mostrar el nombre en MAYUSCULAS")
print("2 - mostrar el nombre en minusculas")
print("3 - mostrar el nombre con la primera letra en mayuscula")
# solicitar la opción
opcion = input("ingresa 1, 2 o 3: ")
# transformar el nombre segun la opcion
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("opcion no valida.")


 # solicitar la magnitud del terremoto al usuario
magnitud = float(input("ingresa la magnitud del terremoto: "))
# clasificar segun la escala de richter
if magnitud < 3:
    print("muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("fuerte (puede causar daños en estructuras debiles)")
elif 6 <= magnitud < 7:
    print("muy fuerte (puede causar daños significativos)")
else:
    print("extremo (puede causar graves daños a gran escala)")



# solicitar datos al usuario
hemisferio = input("¿en qué hemisferio estas? (N/S): ").upper()
mes = int(input("¿en que mes estamos? (1-12): "))
dia = int(input("¿que día del mes es hoy?: "))
# determinar la estación según el mes y el día
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "invierno"
    estacion_sur = "verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "primavera"
    estacion_sur = "otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "verano"
    estacion_sur = "invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "otoño"
    estacion_sur = "primavera"
else:
    estacion_norte = estacion_sur = "desconocida"
# mostrar el resultado
if hemisferio == "N":
    print("te encontras en la estacion:", estacion_norte)
elif hemisferio == "S":
    print("te encontras en la estacion:", estacion_sur)
else:
    print("hemisferio no reconocido. usa 'N' o 'S'.")

