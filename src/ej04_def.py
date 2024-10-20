# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
# ++ NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Fahrenheit.

def fahrenheit_a_celsius():
    temperatura: float = float(input("Introduce la temperatura en grados Fahrenheit que deseas convertir a Celsius: "))
    return (temperatura - 32) * 5/9

def main():
    print(f"La temperatura convertida es: {fahrenheit_a_celsius():.2f} Cº")

if __name__ == "__main__":
    main()