# Ejercicio 1.2.19
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas 
# y n es el número de letras que tienen el nombre.

def contar_letras(palabra: str) -> str:
    cont = 0
    for letras in palabra:
        cont += 1
    return cont

def main():
    palabra_usuario = str(input("Introduce tu nombre: "))
    print(f"{palabra_usuario.upper()} tiene {contar_letras(palabra_usuario)} letras.")

if __name__ == "__main__":
    main()