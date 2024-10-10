# Ejercicio 1.2.6
# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

def calcular_importe(precio_articulo: float, iva) -> tuple:

    iva_pagado = precio_articulo * iva / 100
    importe_con_iva: float = precio_articulo + iva_pagado
    importe_sin_iva: float = precio_articulo - iva_pagado

    return importe_con_iva, importe_sin_iva


def main():
    IVA_10 = 10

    importe_articulo = float(input("Introduce el precio del artículo: "))

    importe_iva, importe_sn_iva = calcular_importe(float(input(importe_articulo, IVA_10)))
    print(f"Para tu artículo de {importe_articulo} has pagado un precio final (por el 10% de IVA) de {importe_iva:.2f}. \nEl precio del artículo sin IVA es de {importe_sn_iva:.2f}.")

if __name__ == "__main__":
    main()