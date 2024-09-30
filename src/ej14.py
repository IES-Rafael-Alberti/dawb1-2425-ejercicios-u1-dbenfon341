# Ejercicio 1.2.14
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular 
# el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

def calculo_peso_juguetes(ud_payaso: int, ud_doll:int) -> int:
    ud_payaso *= 112
    ud_doll *= 75
    return ud_payaso + ud_doll

def main():
    ud_payaso: int = int(input("Introduce el número de payasos vendidos en el último pedido: "))
    ud_doll: int = int(input("Introduce el número de muñecas vendidas en el último pedido "))
    print(f"El peso total del paquete que será enviado es de {calculo_peso_juguetes(ud_payaso, ud_doll)} g")

if __name__ == "__main__":
    main()