# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

def celsius_a_fahrenheit(temperatura: float) -> float:
    return (temperatura * 9/5) + 32

def main():
    temperatura_celsius = float(input("Introduce la temperatura en grados Celsius que deseas convertir a Fahrenheit: "))
    print(f"La temperatura introducida ({temperatura_celsius:.2f} Cº) convertida a Fahrenheit es: {celsius_a_fahrenheit(temperatura_celsius):.2f} Fº")

if __name__ == "__main__":
    main()