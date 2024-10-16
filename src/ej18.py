# Ejercicio 1.2.18
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con
# todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

def nomenclatura_palabra(nombre: str) -> tuple:
    return nombre.lower(), nombre.upper(), nombre.title()

def main():
    lista_nombre = nomenclatura_palabra(str(input("Introduce tu nombre: ")))
    print(lista_nombre[0])
    print(lista_nombre[1])
    print(lista_nombre[2])

if __name__ == "__main__":
    main()