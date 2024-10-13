# Ejercicio 1.29
# Realiza un programa en Python que solicite un nombre y una edad.
# Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
# El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".

def main():

    validar_edad = True
    nombre: str = str(input("Introduce tu nombre: "))

    try:
        if nombre == "":
            nombre = "Desconocido"
        else:
            nombre = nombre
        while validar_edad:
            edad = int(input("Introduce tu edad (0-125): "))
            if edad <= 0 or edad >= 125:
                print("**ERROR** La edad debe estar comprendida entre 0 y 125 años.")
            else:
                validar_edad = False
        print(f"Te llamas {nombre} y tienes {edad}. Te quedan {125-edad} años por cumplir.")

    except ValueError as e:
        print(f"**ERROR** Tu edad no puede ser una letra. Código de error -> {e}")

if __name__ == "__main__":
    main()