import time

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

lista = [64, 25, 12, 22, 11]
start = time.time()
selection_sort(lista)
end = time.time()
print("Selection Sort:", lista)
print("Tiempo de ejecución:", end - start, "segundos")