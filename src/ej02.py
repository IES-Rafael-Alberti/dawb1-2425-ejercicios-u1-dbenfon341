# Ejercicio 1.2.2¶
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
    precio_hora: int = int(input("Coste por hora: "))
    print(calcular_horas(horas, precio_hora))

if __name__ == "__main__":
    main()