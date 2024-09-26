# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
# 
# ++ NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.

def celsius_a_fahrenheit(temperatura: float) -> str:
    fahrenheit: float = (temperatura * 9/5) + 32
    string_conversion = f"La temperatura introducida ( {temperatura} Cº) pasada a Fahrenheit es: {fahrenheit}Fº"
    return string_conversion


def main():
    temperatura: float = float(input("Introduce la temperatura en grados Celsius que deseas convertir a Fahrenheit: "))
    while (temperatura <= 0):
        temperatura = float(input("**ERROR** La temperatura no puede ser igual o menor que 0: "))
    print(celsius_a_fahrenheit(temperatura))

if __name__ == "__main__":
    main()