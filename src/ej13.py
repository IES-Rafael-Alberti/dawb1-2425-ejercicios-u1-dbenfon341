# Ejercicio 1.2.13
# Escribir un programa que pida al usuario dos números enteros y muestre por
# pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el 
# cociente y el resto de la división entera respectivamente.

# def division(num1: float, num2: float) -> float:
#    return num1 / num2

def division_cociente(num1: int, num2: int) -> int:
    return num1 // num2

def division_resto(num1: int, num2: int) -> int:
    return num1 % num2

def main():
    try:
        num1: int = int(input("Introduce un número: "))
        num2: int = int(input("Introduce otro número: "))

        if num2 == 0:
            raise ZeroDivisionError
    
        print(f"La división de {num1} entre {num2} me da un cociente {division_cociente(num1, num2)} y un resto {division_resto(num1, num2)}.")

    except ValueError:
        print("**ERROR** Debes introducir números.")

    except ZeroDivisionError:
        print("**ERROR** La división por 0 no es posible.")

if __name__ == "__main__":
    main()