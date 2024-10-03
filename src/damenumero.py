def comprobar_entero(entero: str)-> bool:
    validar_entero = True
    while validar_entero:
        if entero.isdigit():
            validar_entero = False
            return True
        else:
            entero = input("Debes introducir un número entero: ")

def dame_entero():
    numero = input("Introduce un número entero: ")
    valido = comprobar_entero(numero)
    while not valido:
        valido = comprobar_entero(numero)
    else:
        return numero


def main():
    numero = dame_entero()
    print (f"Tu número es: {numero}")

if __name__ == "__main__":
    main()