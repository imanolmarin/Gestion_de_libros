import os.path
import pickle
from registro import *


# PUNTO 1

def texto_separado(renglon, separador):
    cadenas = []
    cadena_actual = ''

    for car in renglon:
        if car != separador:
            cadena_actual += car
        else:
            cadenas.append(cadena_actual)
            cadena_actual = ''

    if renglon[-1] != separador:
        cadenas.append(cadena_actual)

    return cadenas


def archivo_vector(nom_archivo):
    if not os.path.exists(nom_archivo):
        print('\nError: el arhivo no existe o tiene un nombre incorrecto.\n\n')
        return None

    archivo = open(nom_archivo, mode="rt", encoding="utf8")

    libros = []
    contador = 0
    for renglon in archivo:
        contador += 1
        if contador > 1:
            if renglon[-1] == '\n':
                renglon = renglon[:-1]

            cadenas = texto_separado(renglon, separador=',')

            # crear el registro
            reg = Libros(str(cadenas[0]), int(cadenas[1]), int(cadenas[2]), int(cadenas[3]), float(cadenas[4]),
                         str(cadenas[5]))
            libros_en_orden(libros, reg)

    archivo.close()
    return libros


def libros_en_orden(vector, reg):
    inicio, fin = 0, len(vector) - 1
    posicion_actual = 0
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if vector[medio].isbn == reg.isbn:
            posicion_actual = medio
            break

        if reg.isbn < vector[medio].isbn:
            fin = medio - 1
        else:
            inicio = medio + 1

    if inicio > fin:
        posicion_actual = inicio

    vector[posicion_actual:posicion_actual] = [reg]


# PUNTO 4


def popularidad_matriz(vector):
    idioma = 0
    mat = [[0] * 21 for x in range(27)]
    for f in range(len(mat)):
        anios = 1999
        idioma += 1
        for c in range(len(mat[f])):
            rating_mayor = 0
            anios += 1
            for k in range(len(vector)):
                if vector[k].anio == anios and vector[k].idioma == idioma:
                    if vector[k].rating > rating_mayor:
                        rating_mayor = vector[k].rating
                        libro_mayor = vector[k]
                        mat[f][c] = libro_mayor
    return mat


# PUNTO 5


def publicaciones(vector):
    vector_publi = [0] * 10
    anio_inicial = 1900
    anio_final = 1910
    decada = 0

    for a in range(10):#Serian las 10 decadas
        if a > 0:
            decada += 1
            anio_inicial += 10
            anio_final += 10
        for i in range(len(vector)):#Aca recorre el vector y con los libros y suma los que correspondan a la decada indicada
            if anio_inicial <= vector[i].anio <= anio_final:
                vector_publi[decada] += 1

    return vector_publi


def mostrar_publi(vector):
    decada = 1900
    n = len(vector)
    mayor_decada = 0
    ultima_decada = 0
    for i in range(n):
        if vector[i] != 0:
            print("Cantidad de libros para la decada", decada, ":", vector[i])
        if vector[i] > ultima_decada:
            mayor_decada = decada

        decada += 10
        ultima_decada = vector[i]

    return print("La decada con mayor libros fue", mayor_decada)


# PUNTO 6


def crear_archivo(archivo, matriz):
    archivo = open(archivo, 'wb')
    cont = 0

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                pickle.dump(matriz[f][c], archivo)
                cont += 1
    print("Se grabaron", cont, "Archivos")
    archivo.close()


# PUNTO 7


def mostrar_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo): # Esta condicion esta por si alguien llegase a borrar la condicion de la bandera y no crearon el archivo anteriormente
        return print('No existe el archivo ' + nombre_archivo + ", Primero debe crearlo")

    archivo = open(nombre_archivo, 'rb')
    size = os.path.getsize(nombre_archivo)

    while archivo.tell() < size:
        libro = pickle.load(archivo)
        print(libro)

    archivo.close()


