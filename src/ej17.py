# Ejercicio 1.2.17¶
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
# líneas distintas el nombre del usuario tantas veces como el número introducido.

def main():
   nombre = str(input("Introduce tu nombre: "))
   n = int(input("Introduce un número entero: "))
   for i in range (0, n):
       print(nombre)

if __name__ == "__main__":
    main()