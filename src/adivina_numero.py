# Adivina el número utilizando randomint y un contador en bucle while.

import random

def obtener_numero(num1: int, num2: int):
    return

def validar_numero():
    return

def main():
    numero_oculto = random.randint(1, 20)
    contador = 10

    print(f"Introduce un número desde 1 hasta 500. Tienes {contador} intentos.")

    while contador > 0:
        numero_usuario = int(input("Introduce tu número: "))

        if numero_usuario > numero_oculto:
            contador -= 1
            print(f"El número debe ser más bajo. Te quedan {contador} intentos.")
        elif numero_usuario < numero_oculto:
            contador -= 1
            print(f"El número debe ser más alto. Te quedan {contador} intentos.")
        else:
            print("Ganaste!")
    else:
        print(f"Vaya, no adivinaste el número. El número oculto era {numero_oculto}.")


if __name__ == "__main__":
    main()