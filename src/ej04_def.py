# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
# 
# ++ NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.

def celsius_a_fahrenheit():
    temperatura: float = float(input("Introduce la temperatura en grados Celsius que deseas convertir a Fahrenheit: "))
    return (temperatura * 9/5) + 32

def main():
    print(f"La temperatura convertida es: {celsius_a_fahrenheit():.2f} Fº")

if __name__ == "__main__":
    main()