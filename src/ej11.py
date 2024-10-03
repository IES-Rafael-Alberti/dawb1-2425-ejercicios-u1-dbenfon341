# Ejercicio 1.2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
# desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n+1)/2

def contar_numeros(contar_num: int) -> int:
    """ Funcion para contar desde 0 hasta input introducido por el usuario para luego sumar y actualizar una variable llamada numero_completo con la suma de todos ellos.
    Args:
        contar_numeros(int): La función sumará números hasta el valor de este parámetro.
    Returns:
        numero_completo(int): Retornará una variable con el valor de la suma de todos los numeros desde 0 hasta contar_num.
    """
    numero_completo: int = 0
    for i in range(0, contar_num+1):
        numero_completo += i
    return numero_completo

def main():
    try:
        contar_num: int = int(input("Introduce un número: "))
        print(f"La suma de los números enteros es: {contar_numeros(contar_num)}")
    except ValueError as e:
        print(f"**ERROR** Solo puedo tratar con números. Código de error -> {e}")

if __name__ == "__main__":
    main()