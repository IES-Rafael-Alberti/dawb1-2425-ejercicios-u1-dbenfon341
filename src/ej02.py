# Ejercicio 1.2.2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
#
# Horas de trabajo: 6
# Coste por hora: 10
# Importe total: 60

def calcular_horas(horas: int, precio_hora: int) -> str:
    string_importe = f"Importe total: {horas*precio_hora}"
    return string_importe

def main():
    horas: int = int(input("Horas de trabajo: "))
    while (horas <= 0):
        horas: int = int(input("**ERROR** Las horas no puede ser 0 o estar vacío: "))
    precio_hora: int = int(input("Coste por hora: "))
    while (precio_hora <= 0):
        precio_hora: int = int(input("**ERROR** El precio/hora no puede ser 0 o estar vacío: "))

    print(calcular_horas(horas, precio_hora))

if __name__ == "__main__":
    main()