# Ejercicio 1.2.7
# Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def suma_numeros(num1: float, num2: float, num3: float) -> float:
    """Recibe tres parámetros y retorna la suma de los mismos"""
    return num1 + num2 + num3

def main():
    try:
        num1: float = float(input("Introduce un número para sumar: "))
        while(num1 <= 0):
            print("ERROR El número debe ser positivo.")
            num1: float = float(input("Introduce el número nuevamente: "))

        num2: float = float(input("Introduce otro número: "))
        while(num2 <= 0):
            print("ERROR El número debe ser positivo.")
            num2: float = float(input("Introduce el número nuevamente: "))

        num3: float = float(input("Introduce un tercer número: "))
        while(num3 <= 0):
            print("ERROR El número debe ser positivo.")
            num3: float = float(input("Introduce el número nuevamente: "))

        print(f"La suma de {num1}, {num2} y {num3} es de {suma_numeros(num1, num2, num3)}.")

    except ValueError:
        print("**ERROR** Solo puedo sumar números.")

if __name__ == "__main__":
    main()