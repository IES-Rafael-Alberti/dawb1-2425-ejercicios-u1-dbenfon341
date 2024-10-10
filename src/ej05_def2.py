# Ejercicio 1.2.5_def2
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#
# ++ recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
# 
# La función calcula_precio(importe: float, iva: float) -> str recibe el importe y el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el 
# iva y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> "El precio final del artículo con IVA (21.00) es 121.00€."

def calcular_precio(importe: float, iva: float) -> str:
    if iva < 0 or iva > 100:
        iva = 21
    return f"El precio final del artículo con IVA ({iva}) es {(((importe * iva) / 100) + importe):.2f} €"

def main():
    importe: float = float(input("Introduce el importe sin IVA del artículo: "))
    iva: float = float(input("Introduce el porcentaje de IVA a aplicar: "))
    print(calcular_precio(importe, iva))

if __name__ == "__main__":
    main()