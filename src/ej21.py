# Ejercicio 1.2.21
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

def invertir_frase(frase: str) -> str:
    return frase [::-1]

def main():
    frase: str = str(input("Frase: "))
    
    print(f"Tu frase invertida es: {invertir_frase(frase)}")

if __name__ == "__main__":
    main()