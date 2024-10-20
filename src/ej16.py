# Ejercicio 1.2.16
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas 
# que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser 
# fresca y el coste final total de todas las barras no frescas.

BARRA_PAN: float = 3.49

barra_descuento = BARRA_PAN * 0.60

barra_dura = BARRA_PAN - barra_descuento

def main():
    barras_vendidas = int(input(f"¿Cuantas barras (que no son del día) se han vendido?: "))
    print(f"Precio de una barra de pan: {BARRA_PAN:.2f}\nDescuento por no ser fresca: {barra_descuento:.2f}\nCOSTE TOTAL DE LAS BARRAS NO FRESCAS: {(barra_dura*barras_vendidas):.2f}")

if __name__ == "__main__":
    main()