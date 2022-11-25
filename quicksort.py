import os, argparse, pathlib
from datetime import datetime

def partition(list, low, high):
    pivot = list[high].stat().st_ctime
    i = low - 1
    for j in range(low, high):
        if list[j].stat().st_ctime <= pivot:
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
        lista.append(pathlib.Path(os.path.join(path, filename)))
    quicksort(lista, 0, len(lista) - 1) # Ordenamiento por Quicksort
    for elemento in lista:
        print(f"\t{datetime.fromtimestamp(elemento.stat().st_ctime)}\t{elemento.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Directorio completo \
                        para ordenar por fecha", type=str)
    args = parser.parse_args()
    main(args.path)