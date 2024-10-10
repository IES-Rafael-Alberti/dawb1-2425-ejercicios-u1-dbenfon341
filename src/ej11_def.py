# Ejercicio 1.2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
# desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n+1)/2
#
# ++ recibe un número y retorna una cadena de caracteres con el resultado de la función.

def contar_numeros(num: int) -> str:
    numero_completo: int = 0
    serie = ""
    for i in range(1, num+1):
        numero_completo += i
        serie += f"{i}+"
    serie = serie[:-1]

    return f"La suma de {serie} es {numero_completo}."

def main():
    try:
        num: int = int(input("Introduce un número: "))
        print(contar_numeros(num))
    except ValueError as e:
        print(f"**ERROR** Solo puedo tratar con números. Código de error -> {e}")
        
if __name__ == "__main__":
    main()