# Ejercicio 1.2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#
# ++ recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def calcular_iva(importe: float, iva: float) -> str:
    precio_final: float = ((importe / 100) * iva) + importe
    precio_final_string: str = f"El precio final del artículo es: {precio_final} €"
    return precio_final_string


def main():
    importe: float = float(input("Introduce el importe sin IVA del artículo: "))
    while (importe <= 0):
        importe: float = float(input("**ERROR** El importe no puede ser menor o igual a 0: "))
    iva: float = float(input("Introduce el tipo de IVA a aplicar: "))
    while (iva <= 0):
        iva: float = float(input("**ERROR** El IVA no puede ser menor o igual a 0: "))
    print (calcular_iva(importe, iva))

if __name__ == "__main__":
    main()