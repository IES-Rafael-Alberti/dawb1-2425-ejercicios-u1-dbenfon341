# Ejercicio 1.2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#
# ++ recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def calcular_iva():
    importe: float = float(input("Introduce el importe sin IVA del artículo: "))
    iva: float = float(input("Introduce el porcentaje de IVA a aplicar: "))
    print(f"El precio total es de: {((importe * iva) / 100) + importe} €")


def main():
    calcular_iva()

if __name__ == "__main__":
    main()