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

import ej01, ej02, ej03, ej04, ej05, ej06, ej07, ej08, ej09, ej10, ej11, ej12, ej13, ej14, ej15, ej16, ej17, ej18, ej19, ej20, ej21, ej22, ej23, ej24, ej25, ej26, ej27, ej28, ej29, ej30, ej31, ej32, ej33, ej34, ej35, adivina_numero
from utils import clear

TITULO = "Ejercicios 1-35 + adivina_numero UD 1 de Python"

# Constante con los valores que usaremos como confirmacion para ejecutar ejercicios.
CONFIRMACION = "s", "si", "S", "SI", "y", "YES", "Y", "yes"


# Lista con la descripción de cada uno de los ejercicios.
descripcion_ejercicios = [
    "ej01: Saludar",
    "ej02: Calcular importe",
    "ej03: Mostrar expresiones",
    "ej04: Convertir grados",
    "ej05: Calcular precio IVA",
    "ej06: Calcular importe IVA 10",
    "ej07: Suma tres números 1",
    "ej08: Suma tres números 2",
    "ej09: Suma tres números 3",
    "ej10: Mostrar calculo",
    "ej11: Sumar enteros",
    "ej12: Calcular IMC",
    "ej13: Dividir números",
    "ej14: Juguetería",
    "ej15: Cuenta de ahorros",
    "ej16: Panadería",
    "ej17: Imprimir nombre",
    "ej18: Mostrar nombre mayus/minus",
    "ej19: Numero de letras en nombre",
    "ej20: Número de teléfono formateado",
    "ej21: Invertir frase",
    "ej22: Transformar vocales en mayúscula",
    "ej23: Transformar correo electrónico",
    "ej24: Formatear precio de producto",
    "ej25: Formatear fecha",
    "ej26: Cesta de la compra",
    "ej27: Descripcion de producto",
    "ej28: Mostrar número mayor",
    "ej29: Mostrar edad por cumplir",
    "ej30: Mostrar serie de números",
    "ej31: Calcular area de triangulo",
    "ej32: Mostrar número aleatorio",
    "ej33: Mostrar número primo",
    "ej34: Mostrar divisores",
    "ej35: Calcular serie Fibonacci",
    "ej36: Juego de adivina el número",
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
    30: ej30.main,
    31: ej31.main,
    32: ej32.main,
    33: ej33.main,
    34: ej34.main,
    35: ej35.main,
    36: adivina_numero.main
}


def pausa():
    """
    
    """
    input("Presiona ENTER para continuar...")


def introducir_entero() -> int:
    """
    
    """
    entero = None
    while entero is None:
        try:
            entero = int(input("Introduce el número del programa: "))
        except ValueError:
            print("**ERROR** Debes introducir un número.")
            entero = None
    return entero


def es_opcion_valida(opcion) -> bool:
    """
    
    """
    return 1 <= opcion <= 36


def main():
    iniciar = True
    opcion = None

    while iniciar:
        if opcion == None:
            opcion = introducir_entero()
            if not es_opcion_valida(opcion):
                print("**ERROR** Solo existen programas del 1 al 36")
                opcion = None
                pausa()
            else:
                print(f"> {descripcion_ejercicios[opcion-1]}")
                ejecutar = input("> ¿ejecutar? (sí o no) ").replace(" ", "")
                if ejecutar in CONFIRMACION:
                    ejercicios[opcion]()
                    opcion = None
                    pausa()
                    clear()
                else:
                    opcion = None
                    pausa()
                    clear()

if __name__ == "__main__":
    main()