# Ejercicio 1.2.4_def2
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
# La función grados_celsius(fahrenheit: float) -> float recibe los grados fahrenheit (redondeados a dos posiciones decimales) y retorna los grados celsius (redondeados a dos posiciones).

def grados_celsius(fahrenheit: float) -> float:
    fahrenheit = (fahrenheit * 9/5) + 32
    return round(fahrenheit, 2)

def main():
    temperatura: float = float(input("Introduce la temperatura en grados Celsius que deseas convertir a Fahrenheit: "))
    temperatura = round(temperatura, 2)
    print(f"La temperatura convertida es: {grados_celsius(temperatura):.2f} Fº")

if __name__ == "__main__":
    main()