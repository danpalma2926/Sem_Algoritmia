import os
import argparse, pathlib
from datetime import datetime

def partition(list, low, high):
    pivot = list[high][1]
    i = low - 1
    for j in range(low, high):
        if list[j][1] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    return i+1

def quicksort(list, low, high):
    if low < high:
        pivot = partition(list, low, high)
        quicksort(list, low, pivot - 1)
        quicksort(list, pivot + 1, high)

def main(path):
    print(f"Ordenando archivos en el directorio '{path}': ({len(os.listdir(path))}) archivos")
    lista = []
    for filename in os.listdir(path):
        archivo = []
        file_name = pathlib.Path(os.path.join(path, filename))
        c_timestamp = file_name.stat().st_ctime 
        archivo.append(file_name.name)
        archivo.append(c_timestamp)
        lista.append(archivo)
        # Ordenamiento por Quicksort
        quicksort(lista, 0, len(lista) - 1)
    for elemento in lista:
        print(f"\t{datetime.fromtimestamp(elemento[1])}\t{elemento[0]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Directorio completo \
                        para ordenar por fecha", type=str)
    args = parser.parse_args()
    main(args.path)