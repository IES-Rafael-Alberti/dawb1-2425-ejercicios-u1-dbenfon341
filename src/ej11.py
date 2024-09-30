# Ejercicio 1.2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
# desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n+1)/2

def main():
    n: int = int(input("Introduce un número: "))
    numero_completo: int = 0
    for i in range(0, n+1):
        numero_completo += i
    print(numero_completo)

if __name__ == "__main__":
    main()