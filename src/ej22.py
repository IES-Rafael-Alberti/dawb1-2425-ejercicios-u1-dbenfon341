# Ejercicio 1.2.22
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def reemplazo_vocal_mayus(frase: str, vocal: str) -> str:
    return frase.replace(vocal, vocal.upper())

def main():
    frase_usuario = input("Introduce una frase: ")
    vocal_usuario = input("Introduce una vocal a transforma en mayúscula: ")

    resultado = reemplazo_vocal_mayus(frase_usuario, vocal_usuario.lower())

    print(f"Frase con la vocal {vocal_usuario} en mayúscula: {resultado}")

if __name__ == "__main__":
    main()