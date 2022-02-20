import csv
from time import time

def cargar_datos():
    listado_de_palabras = []
    with open('listado_de_palabras_sin_tildes.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            listado_de_palabras.append(row[0])
    return listado_de_palabras

# TODO: Cuando la salida sean pocas palabras, mostrarlas.
def busqueda_de_letras(data, letras):
    y = len(letras)
    palabras_coincidentes = 0
    candidatas = []
    match = False
    for e in data:
        if len(e) <= y:
            continue
        elif e.startswith(letras):
            palabras_coincidentes += 1
            match = True
            if e[y] not in candidatas:
                candidatas.append(e[y])
        elif match == True and e.startswith(letras) == False:
            print(e)
            break
    return candidatas

def main(letras):
    listado = cargar_datos()
    return busqueda_de_letras(listado, letras)

if __name__ == "__main__":
    print('Introduce letras: ')
    x = input()
    print(f'Las candidatas para continuar son {main(x)}')
