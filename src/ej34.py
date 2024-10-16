# Mostrar todos los divisores de un número

def divisores_numero(numero) -> str:
    divisores = ""

    cont = 1
    while cont <= numero:
        if numero % cont == 0:
            divisores += f"{cont}, "
        cont += 1

    return divisores.strip(", ")

def main():
    numero = int(input("Introduce un número: "))
    print(f"Los divisores de tu número {numero} son: {divisores_numero(numero)}")

if __name__ == "__main__":
    main()