# Ejercicio 1.2.24
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

# def formatear_precio():
#     return

# def validar_precio():
#     return

# def pedir_precio():
#     return

def main():
    precio: float = float(input("Introduce precio del producto con dos decimales: "))
    precio = str(precio)
    precio_con_split = precio.split(".")

    centimos = precio_con_split[1]
    euros = precio_con_split[0]

    print(f"El precio es de {precio_con_split[0]} euros y {precio_con_split[1]} céntimos.")
    print(f"El precio es de {euros} euros y {centimos} céntimos.")

if __name__ == "__main__":
    main()