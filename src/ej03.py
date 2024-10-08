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

# ```ancho / alto = 1.4166666666666667 y es de tipo <class 'float'>```

ancho: int = 17
alto: float = 12.0

def main():
    calculo_1 = ancho / 2
    calculo_2 = ancho // 2
    calculo_3 = alto / 3
    calculo_4 = 1+2*5

    print(f"ancho / 2 = {calculo_1} y es de tipo {type(calculo_1)}")
    print(f"ancho // 2 = {calculo_2} y es de tipo {type(calculo_2)}")
    print(f"alto /3 = {calculo_3} y es de tipo {type(calculo_3)}")
    print(f"1+2*5 = {calculo_4} y es de tipo {type(calculo_4)}")

if __name__ == "__main__":
    main()