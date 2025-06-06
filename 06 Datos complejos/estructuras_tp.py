precios_frutas = {"banana": 1200, "anana": 2500, "melon": 3000, "uva": 1450}

#ejercicio 1 agregar frutas a la lista
precios_frutas["naranja"] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["pera"] = 2300
print(precios_frutas)

#ejercicio 2 actualizacion de precios
precios_frutas = {"banana": 1200, "anana": 2500, "melon": 3000, "uva": 1450, "naranja": 1200, "manzana": 1500, "pera": 2300}
precios_frutas["banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["melon"] = 2800
print(precios_frutas)

#ejercicio 3 mostrar lista sin precios
precios_frutas = {"banana": 1330, "anana": 2500, "melon": 2800, "uva": 1450, "naranja": 1200, "manzana": 1700, "pera": 2300}
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#ejercicio 4 lista de contacto
contactos = {"pedro": "123456", "maxi": "987654", "romina": "555555", "maria": "888888", "sofia": "222222"}
nombre = input("ingresa un nombre: ").lower()
if nombre in contactos:
    print("numero:", contactos[nombre])
else:
    print("no se encontro ese nombre")

#ejercicio 5 frase y recuento de palabras
frase = input("ingresa una frase: ").lower()
palabras = frase.split()
unicas = set(palabras)
print("palabras unicas:", unicas)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("recuento de palabras:", recuento)

#ejercicio 6 promedio de notas
alumnos = {}
for i in range(3):
    nombre = input("ingresa el nombre del alumno: ").lower()
    nota1 = float(input("ingresa la primera nota: "))
    nota2 = float(input("ingresa la segunda nota: "))
    nota3 = float(input("ingresa la tercera nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)
for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = sum(notas) / len(notas)
    print("promedio de", nombre + ":", promedio)


#ejercicio 7 aprobacion de parciales
parcial1 = {"ana", "juan", "maria", "sofia"}
parcial2 = {"juan", "mario", "sofia", "laura"}
ambos = parcial1 & parcial2
print("aprobaron ambos:", ambos)
solo_uno = parcial1 ^ parcial2
print("aprobaron solo uno:", solo_uno)
al_menos_uno = parcial1 | parcial2
print("aprobaron al menos uno:", al_menos_uno)


#ejercicio 8 lista de stock
stock = {"pan": 10, "leche": 5, "arroz": 8}
producto = input("ingresa un producto: ").lower()
if producto in stock:
    unidades = int(input("cuantas unidades queres agregar?: "))
    stock[producto] += unidades
    print("stock actualizado:", stock[producto])
else:
    nuevo_stock = int(input("producto no encontrado. ingresa stock inicial: "))
    stock[producto] = nuevo_stock
    print("producto agregado:", producto, "con stock:", nuevo_stock)
print("stock final:", stock)


#ejercicio 9 agenda
agenda = {("lunes", "10:00"): "reunion", ("martes", "15:00"): "clase de ingles", ("miercoles", "18:00"): "gimnasio"}
dia = input("ingresa un dia: ").lower()
hora = input("ingresa una hora (formato hh:mm): ")
clave = (dia, hora)
if clave in agenda:
    print("actividad:", agenda[clave])
else:
    print("no hay actividad programada")

#ejercicio 10
paises = {"argentina": "buenos aires", "brasil": "brasilia", "chile": "santiago", "uruguay": "montevideo"}
capitales = {}
for pais in paises:
    capital = paises[pais]
    capitales[capital] = pais
print(capitales)

