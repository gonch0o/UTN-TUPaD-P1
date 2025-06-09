import time

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

lista = [4, 2, 7, 1, 9, 3]
start = time.time()
resultado = busqueda_lineal(lista, 9)
end = time.time()
print("Búsqueda lineal:", resultado)
print("Tiempo de ejecución:", end - start, "segundos")