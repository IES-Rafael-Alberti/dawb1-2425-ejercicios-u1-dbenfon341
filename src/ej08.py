# Ejercicio 1.2.8
# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

def main():
    numero_suma: float = 0
    try:
        for _ in range(3):
            numero_suma += float(input("Introduce un número a sumar:"))
        print (f"La suma de los tres números es de {numero_suma}.")

    except ValueError:
        print("**ERROR** Solo puedo sumar números.")

if __name__ == "__main__":
    main()