import csv
from pickle import TRUE
from re import T
from time import time

listado_de_palabras = []
with open('listado_de_palabras_sin_tildes.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        listado_de_palabras.append(row[0])

x = input('Introduce las letras: ')
print()
inicio = time()
y = len(x)
palabras_coincidentes = 0
candidatas = []
match = False
for e in listado_de_palabras:
    if len(e) <= y:
        continue
    elif e.startswith(x):
        palabras_coincidentes += 1
        match = True
        if e[y] not in candidatas:
            candidatas.append(e[y])
    elif match == True and e.startswith(x) == False:
        print(e)
        break
print(candidatas)
print(f'Palabras coincidentes: {palabras_coincidentes}')
print("--- %s seconds ---" % (time() - inicio))
print()
