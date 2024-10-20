# Calcular el área de un triángulo a partir de tres lados.

import math

def calcular_area(a: float, b: float, c: float) -> float:
    s = (a + b + c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]

    pos_punto = valor.find(".")
    if pos_punto >= 0:
        valor =  valor[:pos_punto] + valor[pos_punto + 1:]
    
    return valor.isdigit()


def validar_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def introduce_numero(msj: str) -> float:
    valor = input(msj).strip().replace(",", ".")

    while not comprobar_float(valor):
        print("error")
        valor = input(msj).strip().replace(",", ".")
    
    return float(valor)


def main():
    a = float(introduce_numero("Lado 1: "))
    b = float(introduce_numero("Lado 2: "))
    c = float(introduce_numero("Lado 3: "))
    validar_triangulo_var = True

    while validar_triangulo_var:
        if validar_triangulo(a,b,c):
            area = calcular_area(a, b, c)
            print(f"El área del triángulo con lados ({a}) ({b}) ({c}) es {area:.2f}")
            validar_triangulo_var = False
        else:
            print("El triángulo no es válido.")
            a = float(introduce_numero("Lado 1: "))
            b = float(introduce_numero("Lado 2: "))
            c = float(introduce_numero("Lado 3: "))

if __name__ == "__main__":
    main()