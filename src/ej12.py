# Ejercicio 1.2.12
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

def calcular_imc(peso: int, estatura: float) -> str:
    imc: float = peso / (estatura ** 2)
    string_imc: str = (f"Tu índice de masa corporal es {round(imc, 2)}.")
    return string_imc
    

def main():
    try: 
        peso: int = int(input("Introduce tu peso: "))
        estatura: float = float(input("Introduce tu estatura: "))
        print (calcular_imc(peso, estatura))
    except ValueError:
        print("**ERROR** No has introducido los valores correctos.")

if __name__ == "__main__":
    main()