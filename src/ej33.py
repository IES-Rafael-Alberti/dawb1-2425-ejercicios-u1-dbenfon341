# Escribir un programa que determine si un número es primo

def validar_primo(num) -> bool:
    while num <= 1:
        print(f"Error, el numero debe ser mayor que 1.")
        num = int(input("Introduce un número: "))

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("Introduce un número: "))
    validar_numero_primo = validar_primo(num)

    if validar_numero_primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")

if __name__ == "__main__":
    main()