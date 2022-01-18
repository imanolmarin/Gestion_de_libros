import menus
from functions import *

NOMBRE_ARCHIVO_PRINCIPAL = "libros.csv"
NOMBRE_ARCHIVO_MATRIZ = "populares.dat"


def principal():
    bandera_1 = False
    bandera_matriz = False
    bandera_archivo = False
    opciones = ('1 - Cargar el contenido del archivo a un vector', \
                '2 - Sumar revisión', \
                '3 - Mayor revisiones', \
                '4 - Popularidad 2000', \
                '5 - Publicaciones por década', \
                '6 - Guardar populares en archivo binario', \
                '7 - Mostrar archivo', \
                '8 - Salir')

    opc = None
    while opc != 8:
        menus.mostrar_menu('Gestión de Libros [v2.0]', opciones)
        opc = menus.leer_entero_valido('Ingrese su opción: ', \
                                       limite_inferior=1, \
                                       limite_superior=8)
        if opc == 8:
            return print('Fin.')
        elif opc == 1:
            vector = archivo_vector(NOMBRE_ARCHIVO_PRINCIPAL)
            bandera_1 = True
        elif opc == 2:
            if bandera_1:
                pass
            else:
                print("Primero debe crear el vector de registros")
        elif opc == 3:
            if bandera_1:
                pass
            else:
                print("Primero debe crear el vector de registros")
        elif opc == 4:
            if bandera_1:
                matriz = popularidad_matriz(vector)
                bandera_matriz = True
            else:
                print("Primero debe crear el vector de registros")
        elif opc == 5:
            if bandera_1:
                publi = publicaciones(vector)
                mostrar_publi(publi)
            else:
                print("Primero debe crear el vector con registros")
        elif opc == 6:
            if bandera_matriz:
                crear_archivo(NOMBRE_ARCHIVO_MATRIZ, matriz)
                bandera_archivo = True
            else:
                print("Primero debe crear la matriz")
        elif opc == 7:
            if bandera_archivo:
                mostrar_archivo(NOMBRE_ARCHIVO_MATRIZ)
            else:
                print("Primero debe crear el archivo")

        input('\nPresione intro para continuar.\n')


if __name__ == '__main__':
    principal()
