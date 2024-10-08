# Ejercicio 1.2.25
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también
# funcione cuando el día o el mes se introduzcan con un solo carácter.

def formatear_fecha(fecha) -> tuple:

    dic_meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    fecha_split = fecha.split("/")
    dia, mes, anio = fecha_split
    mes = int(mes)
    mes_traducido = dic_meses.get(mes)

    return dia, mes_traducido, anio

def main():
    dia, mes, anio = formatear_fecha(fecha = input("Introduce una fecha con el formato aa/aa/aaaa: "))

    print(f"Día {dia}, del mes {mes} del año {anio}.")


if __name__ == "__main__":
    main()