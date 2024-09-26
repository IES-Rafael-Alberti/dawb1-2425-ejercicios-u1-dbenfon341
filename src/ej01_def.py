# Ejercicio 1.2.1
# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
#
# Escribe tu nombre: Juan
# Hola, Juan.
#
# ++ recibe un nombre y retorna una cadena de caracteres con el resultado.

def saludo(nombre: str) -> str:
    saludo_completo: str = f"Hola, {nombre}."
    return saludo_completo


def main():
    nombre: str = input("Introduce tu nombre: ")
    while (nombre == ""):
        nombre: str = str(input("**ERROR** Debes introducir un nombre: "))
    print(saludo(nombre))


if __name__ == "__main__":
    main()