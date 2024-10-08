# Ejercicio 1.2.9
# ¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

def main():
    print("El resultado de la suma de los tres números es:",
    round(float(input("Introduce un número par sumar: ")) + float(input("Introduce otro número: ")) + float(input("Introduce otro número: ")),2))

if __name__ == "__main__":
    main()