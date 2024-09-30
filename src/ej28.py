# Ejercicio 1.28
# Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

# El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
# Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".

def numero_menor(num1:int, num2:int) -> int:
    """Funcion que compara y devuelve el número más bajo de los dos introducidos.
    Args:
        num1(int): Primer número introducido.
        num2(int): Segundo número introducido.
    Returns:
        num_menor(int): Variable con el valor del número menor."""

    num_menor: int = 0

    if num1 < num2:
        num_menor = num1
    else:
        num_menor = num2

    return num_menor

def contador_numeros(num1: int, num2: int) -> int:
    """Funcion para contar cuantos números hay entre los dos introducidos. Reice dos numeros y retorna la cantidad entre ellos después de ordenarlos.
    Args:
        num1(int): Primer número introducido.
        num2(int): Segundo número introducido.
    Returns:
        Devuelve la cantidad de números entre los dos.
    """

    num_mayor: int = 0
    
    if num1 > num2:
        num_mayor = num1
    else:
        num_mayor = num2

    return (num_mayor - numero_menor(num1, num2))

def main():
    try:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce un segundo número: "))   
        if num1 == num2:
            print("**ERROR** Los números no pueden ser iguales.")
        elif num1 <= 0 or num2 <= 0:
            print("Los números no pueden ser menores que 0")
        else:
            print(f"El número menor es el {numero_menor(num1, num2)} y entre ellos existen {contador_numeros(num1, num2)} números enteros.")

    except ValueError as e:
        print(f"**ERROR** Solo funciono con números. Mensaje de error -> {e}" )
            
if __name__ == "__main__":
    main()