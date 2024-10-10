# Ejercicio 1.2.23
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def pedir_correo():
    return

def validar_correo():
    return

def formatear_correo():
    return

def main():
    correo = input("Introduce tu email: ")
    correo = correo.split("@")
    print(f"Tu correo es: {correo[0]}@ceu.es")

if __name__ == "__main__":
    main()