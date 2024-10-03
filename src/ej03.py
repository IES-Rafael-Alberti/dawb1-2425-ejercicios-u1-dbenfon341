# Ejercicio 1.2.3
# Suponiendo que se han ejecutado las siguientes sentencias de asignación:

# ancho = 17
# alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

# 1. ancho / 2
# 2. ancho // 2
# 3. alto / 3
# 4. 1 + 2 * 5
# Cuando termines comprueba con el intérprete si has acertado.

ancho: int = 17
alto: float = 12.0

def main():
    calculo_1 = ancho / 2
    calculo_2 = ancho // 2
    calculo_3 = alto / 3
    calculo_4 = 1+2*5

    print(fcalculo_1)
    print(f"{calculo_2}")
    print(f"{calculo_3}")
    print(f"{calculo_4}")

if __name__ == "__main__":
    main()