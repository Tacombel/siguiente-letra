import csv
from time import time

def cargar_datos():
    listado_de_palabras = []
    with open('listado_de_palabras_sin_tildes.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            listado_de_palabras.append(row[0])
    return listado_de_palabras

def busqueda_de_letras(data):
    x = input('Introduce las letras: ')
    print()
    inicio = time()
    y = len(x)
    palabras_coincidentes = 0
    candidatas = []
    match = False
    for e in data:
        if len(e) <= y:
            continue
        elif e.startswith(x):
            palabras_coincidentes += 1
            match = True
            if e[y] not in candidatas:
                candidatas.append(e[y])
        elif match == True and e.startswith(x) == False:
            break
    print(f'Palabras coincidentes: {palabras_coincidentes}')
    print("--- %s seconds ---" % (time() - inicio))
    return candidatas

def main():
    print (busqueda_de_letras(cargar_datos()))


if __name__ == "__main__":
    main()
