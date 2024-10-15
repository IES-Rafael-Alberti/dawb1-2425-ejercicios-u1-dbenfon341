# Adivina el número utilizando randint.
# Incluye validaciones y menú, intentando seguir los principios de responsabilidad única (SPR).

import random
from utils import clear

##########################################################################################################################
# Variables con valores por defecto para adivinar el número.
# num_base: se utiliza como el numero base que se utilizará en el rango desde el que se genera el número aleatorio.
# num_limite: se utiliza como el numero límite que se utilizara en el rango desde el que se genera el número aleatorio.
#
#  ^ Ejemplo: "num_base 1 + num_limite 100" generará un número al azar entre 1 y 100 (1-100).
# 
# intentos: número máximo de intentos que tiene el usuario para adivinar el número.
##########################################################################################################################

num_base = 1
num_limite = 100
intentos = 10

##########################################################################################################################

def configurar_numero_oculto():
    """
    Función que sirve para configurar el juego.
    Valida si el input del usuario es correcto y devuelve la configuración deseada por el usuario.
    Edita de manera global las los valores de las variables num_base, num_limite y intentos.
    """
    global num_base, num_limite, intentos
    
    num_base = None
    num_limite = None
    intentos = None

    while num_base is None:
        try:
            num_base = int(input("Introduce el primer número (mayor que 0): "))
            if num_base <= 0:
                print("**ERROR** El número debe ser mayor que 0.")
                num_base = None
        except ValueError:
            print("No has introducido un número. Vuelve a intentarlo: ")

    while num_limite is None:
        try:
            num_limite = int(input("Introduce el numero máximo (mayor que 0): "))
            if num_limite < num_base:
                print("**ERROR** El número límite debe ser mayor que el número base.")
                num_limite = None
        except ValueError:
            print("No has introducido un número. Vuelve a intentarlo: ")

    while intentos is None:
        try:
            intentos = int(input("Introduce la cantidad de intentos: "))
            if intentos <= 0:
                print("**ERROR** El número debe ser mayor que 0.")
                intentos = None
        except ValueError:
            print("No has introducido un número. Vuelve a intentarlo: ")


def menu():
    """
    
    """
    clear()
    print("********************")
    print("* ADIVINA EL JUEGO *")
    print("********************")
    print("1) Jugar.")
    print("2) Configuracion.")
    print("3) Salir.")


def seleccionar_opcion(opcion: int):
    """
    
    """
    if opcion == 1:
        start()
    elif opcion == 2:
        configurar_numero_oculto()
    elif opcion == 3:
        print("Hasta pronto!")
        exit


def introducir_opcion() -> int:
    """
    
    """
    menu()
    OPCIONES = (1, 2, 3)
    opcion = None
    while opcion is None:
        try:
            opcion = int(input("Introduce opción (1-3): "))
            if opcion not in OPCIONES:
                print(f"**ERROR** La opción {opcion} no existe.")
                opcion = None
        except ValueError:
            print("No has introducido un número")
    return opcion


def validar_numero_usuario() -> int:
    """
    
    """
    numero_usuario = None
    while numero_usuario is None:
        try:
            numero_usuario = int(input("Introduce tu número: "))
        except ValueError:
            print("Debes introducir un número.")
    return numero_usuario


def generar_numero_oculto(num_base: int, num_limite: int):
    """"""
    return random.randint(num_base, num_limite)


def start():
    """
    
    """
    global num_base, num_limite, intentos

    numero_oculto = generar_numero_oculto(num_base, num_limite)

    clear()
    print(f"Introduce un número desde {num_base} hasta {num_limite}. Tienes {intentos} intentos.")

    while intentos > 0:
        try:
            numero_usuario = validar_numero_usuario()
        except ValueError:
            print("Debes introducir un número.")
        if numero_usuario > numero_oculto:
            intentos -= 1
            clear()
            print(f"Tu número es: {numero_usuario}.")
            print(f"El número oculto está entre {num_base} y {num_limite}.")
            print(f"Tu número debe ser más bajo. Te quedan {intentos} intentos.")
        elif numero_usuario < numero_oculto:
            clear()
            intentos -= 1
            print(f"Tu número es: {numero_usuario}.")
            print(f"El número oculto está entre {num_base} y {num_limite}.")
            print(f"El número debe ser más alto. Te quedan {intentos} intentos.")
        else:
            clear()
            print(f"Tu número es: {numero_usuario}.")
            print(f"¡Ganaste! el número oculto era {numero_oculto} y acabaste con {intentos} intento/s restantes. ¿jugar de nuevo?")
            repetir_juego = input("S/N").upper()
            if repetir_juego == "S":
                clear()
                seleccionar_opcion(introducir_opcion())
                numero_oculto = generar_numero_oculto(num_base, num_limite)
            else:
                print("Hasta pronto!")
    else:
        clear()
        print(f"Tu número es: {numero_usuario}")
        print(f"Vaya, no adivinaste el número. El número oculto era {numero_oculto}. ¿Jugar de nuevo?")
        repetir_juego = input("S/N").upper()
        if repetir_juego == "S":
                clear()
                seleccionar_opcion(introducir_opcion())
                numero_oculto = generar_numero_oculto(num_base, num_limite)


def main():
    """
    
    """
    while True:
        seleccionar_opcion(introducir_opcion())


if __name__ == "__main__":
    main()