def mostrar_menu(titulo, opciones):
    print('|' * (len(titulo) + 4))
    print('|', titulo, '|')
    print('|' * (len(titulo) + 4))
    print()
    for opcion in opciones:
        print(opcion)


def leer_entero_valido(msg, limite_superior, limite_inferior=0):
    x = int(input(msg))
    while x < limite_inferior or x > limite_superior:
        print('El valor deber estar entre', limite_inferior,
              'y', limite_superior, ' por favor ingresar una opcion correcta.')
        x = int(input(msg))
    return x
