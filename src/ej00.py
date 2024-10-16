# 1. Desarrolla un programa "ej00.py" que gestione un menú para ejecutar otros programas
# En este ejercicio, debes crear un programa principal llamado "ej00.py" que actúe 
# como un menú para llamar a otros programas que estén ubicados en la carpeta "src". 
# El programa debe funcionar de la siguiente manera:

# Solicitar al usuario que introduzca el número del programa a ejecutar.

# Validación del número del programa:

# Si introduce un número entre 1 y 30, se mostrará el título del programa para 
# indicar lo que hace, por ejemplo, "ej01: Saludo". Luego, debes preguntar si desea ejecutar el programa.
# La respuesta afirmativa debe aceptar cualquiera de las 
# siguientes variantes: s, si, S, SI, y, YES, Y, yes o combinaciones con espacios antes, 
# después o entre letras. Si no desea ejecutarlo, el programa limpiará la consola y volverá a 
# solicitar el número del programa.
# Errores y validaciones:

# Si el número introducido no corresponde con un programa válido (es decir, no está entre 1 y 30), 
# debes mostrar un mensaje de error: "ERROR: Solo existen programas del 1 al 30".
# Al finalizar el programa seleccionado (o después de mostrar el error), debe aparecer 
# el mensaje "Presiona ENTER para continuar...". 
# Tras presionar ENTER, la pantalla debe limpiarse y el programa debe volver a solicitar el número 
# del programa.

# Salir del menú: El programa debe finalizar si el usuario introduce una cadena 
# vacía o solo presiona ENTER sin introducir ningún número.

import ej01, ej02, ej03, ej04, ej05, ej06, ej07, ej08, ej09, ej10, ej11, ej12, ej13, ej14, ej15, ej16, ej17, ej18, ej19, ej20, ej21, ej22, ej23, ej24, ej25, ej26, ej27, ej28, ej29, ej30
from utils import clear


# Constantes con el título del programa y valores que usaremos como confirmacion para ejecutar ejercicios.


TITULO = "Ejercicios 1-30 UD 1 de Python"
CONFIRMACION = "s", "si", "S", "SI", "y", "YES", "Y", "yes"


# Lista con la descripción de cada uno de los ejercicios.


descripcion_ejercicios = [
    "ej01: Pida el nombre del usuario para luego darle la bienvenida.",
    "ej02: ",
    "ej03: ",
    "ej04: ",
    "ej05: ",
    "ej06: ",
    "ej07: ",
    "ej08: ",
    "ej09: ",
    "ej10: ",
    "ej11: ",
    "ej12: ",
    "ej13: ",
    "ej14: ",
    "ej15: ",
    "ej16: ",
    "ej17: ",
    "ej18: ",
    "ej19: ",
    "ej20: ",
    "ej21: ",
    "ej22: ",
    "ej23: ",
    "ej24: ",
    "ej25: ",
    "ej26: ",
    "ej27: ",
    "ej28: ",
    "ej29: ",
    "ej30: ",
]


# Diccionario con clave:valor de numero:main de cada ejercicio en cuestión.


ejercicios = {
    1: ej01.main,
    2: ej02.main,
    3: ej03.main,
    4: ej04.main,
    5: ej05.main,
    6: ej06.main,
    7: ej07.main,
    8: ej08.main,
    9: ej09.main,
    10: ej10.main,
    11: ej11.main,
    12: ej12.main,
    13: ej13.main,
    14: ej14.main,
    15: ej15.main,
    16: ej16.main,
    17: ej17.main,
    18: ej18.main,
    19: ej19.main,
    20: ej20.main,
    21: ej21.main,
    22: ej22.main,
    23: ej23.main,
    24: ej24.main,
    25: ej25.main,
    26: ej26.main,
    27: ej27.main,
    28: ej28.main,
    29: ej29.main,
    30: ej30.main
}


def pausa():
    input("Presiona ENTER para continuar...")


def introducir_entero() -> int:
    entero = None
    while entero is None:
        try:
            entero = int(input("Introduce el número del programa"))
        except ValueError:
            print("**ERROR** Debes introducir un número.")
            entero = None
    return entero


def es_opcion_valida(opcion) -> bool:
    return 1 <= opcion <= 30


def main():
    iniciar = True
    opcion = None

    while iniciar:
        if opcion == None:
            opcion = introducir_entero()
            if not es_opcion_valida(opcion):
                print("**ERROR** Solo existen programas del 1 al 30")
                opcion = None
                pausa()
            else:
                print(f">{descripcion_ejercicios[opcion+1]}")
                ejecutar = input("¿ejecutar? (sí o no) ").replace(" ", "")
                if ejecutar in CONFIRMACION:
                    ejercicios[opcion]()
                    opcion = None
                    pausa()
                    clear()
                else:
                    opcion = None
                    pausa()
                    pausa()

if __name__ == "__main__":
    main()