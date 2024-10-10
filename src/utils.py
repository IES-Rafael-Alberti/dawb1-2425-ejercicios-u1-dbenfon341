# Funcion que limpia la consola

from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

# Funciones auxiliares para validar entradas antes de realizar operaciones. Validan si una cadena representa un número entero o flotante.