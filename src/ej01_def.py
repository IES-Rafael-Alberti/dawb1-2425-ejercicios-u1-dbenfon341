# Ejercicio 1.2.1
# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
#
# Escribe tu nombre: Juan
# Hola, Juan.
#
# ++ recibe un nombre y retorna una cadena de caracteres con el resultado.

def saludo(nombre: str) -> str:
    """Recibe una palabra y devuelve un saludo al usuario.
    Args:
        nombre(str): Recibe el nombre introducido por el usuario para introducirlo como valor en una variable llamada saludo_completo junto a un saludo.
    Returns:
        Retorna variable saludo_completo unificando el parámetro de entrada introducido por el usuario + un string "Hola, ".
    """
    while (nombre == ""):
        nombre: str = str(input("**ERROR** Debes introducir un nombre: "))
    saludo_completo: str = f"Hola, {nombre}."
    return saludo_completo

def main():
    nombre: str = input("Introduce tu nombre: ")
    print(saludo(nombre))


if __name__ == "__main__":
    main()