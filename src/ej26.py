# Ejercicio 1.2.26
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

def separar_productos(productos):
    return productos.split(",")

def main():
    productos_usuario = str(input("Introduce productos separados por coma: "))
    
    for producto in separar_productos(productos_usuario):
        print(producto)

if __name__ == "__main__":
    main()