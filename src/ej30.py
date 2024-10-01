# Ejercicio 1.30
# Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

# El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a 
# que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
# Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10

def serie(inicio: float, incremento: int, total: int) -> str:
    serie = 0
    serie_string: str = ""
    for i in range (inicio, total, incremento):
        serie += i
        serie_string = serie + "-"
    serie =+ "-" + total

    return serie

def main():
    validar_incremento = True
    validar_total = True
    try:
        while validar_incremento:
            incremento: int = int(input("Dame un incremento: "))
            if incremento < 0:
                print("El número debe ser mayor que 0.")
            else:
                validar_incremento: False

        print(f"{serie(inicio, incremento, total)}")

    except ValueError as e:
        print(f"**ERROR** Valores incorrectos. Código de error -> {e}")

if __name__ == "__main__":
    main()