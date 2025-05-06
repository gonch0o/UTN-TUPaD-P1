#ejercicio 1
lista = list(range(4, 101, 4))
print(lista)

#ejercicio 2
lista_gustos = ["mate", "futbol", 27, "musica", "dormir"]
print(lista_gustos[-2])

#ejercicio 3
lista_vacia = []
lista_vacia.append("programacion")
lista_vacia.append("mundo")
lista_vacia.append("circulo")
print(lista_vacia)

#ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) #con la funcion max, se elimino el numero mas alto de la lista, que en este caso es el numero 22
print(numeros)

#ejerciocio 6
numeros = list(range(10, 31, 5))
print(numeros[:2])

#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ranger"
autos[2] = "passat"
print(autos)

#ejercicio 8
doble = []
doble.append(5 * 2)
doble.append(10 * 2)
doble.append(15 * 2)
print(doble)

#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#ejercicio 10
lista_anidada = []
lista_anidada.append(15)
lista_anidada.append(True)
segunda_lista_anidada = [25.5, 57.9, 30.6]
lista_anidada.append(segunda_lista_anidada)
lista_anidada.append(False)
print(lista_anidada)
