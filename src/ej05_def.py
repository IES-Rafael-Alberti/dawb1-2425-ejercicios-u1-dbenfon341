# Ejercicio 1.2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#
# ++ recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def calcular_iva(importe: float, iva: float) -> float:
    """Recibe importe y iva y calcula el precio final"""
    return ((importe * iva) / 100) + importe

def main():
    try:   
        importe: float = float(input("Introduce el importe sin IVA del artículo: "))
        while (importe <= 0):
            importe: float = float(input("**ERROR** El importe no puede ser menor o igual a 0: "))

        iva: float = float(input("Introduce el porcentaje de IVA a aplicar: "))
        while (iva < 0):
            iva: float = float(input("**ERROR** El IVA no puede ser menor que 0: "))

        precio_total = calcular_iva(importe, iva)
        print(f"El precio total es de {precio_total} €")

    except ValueError:
        print("**ERROR** Debes introducir un número.")

if __name__ == "__main__":
    main()