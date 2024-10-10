# Ejercicio 1.2.27
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 
# 6 dígitos enteros y 2 decimales, el número de unidades con tres
# dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def informacion_producto(nombre: str, precio: float, unidades: int) -> tuple:

    precio_total_pr = round(precio * unidades, 2)

    return nombre, precio, unidades, precio_total_pr

def main():
    nombre = str(input("Introduce el nombre del producto: "))
    precio = float(input("Introduce el precio del producto: "))
    unidades = int(input("¿Número de unidades?"))

    nombre, precio, unidades, precio_total = informacion_producto(nombre, precio, unidades)

    print(f"Nombre del producto: {nombre}\nPrecio: {precio:09.2f}\nUnidades: {unidades:03d}\nPrecio total: {precio_total:011.2f}")

if __name__ == "__main__":
    main()