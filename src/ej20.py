# Ejercicio 1.2.20
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte 
# por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

def formatear_telefono(telefono_validado):
    return telefono_validado[4:-3]

def pedir_telefono():
    telefono = str(input("Introduce tu número de teléfono con el formato +34-913724710-56: "))
    while not validar_telefono(telefono):
        telefono = input("El teléfono debe tener el formato +34-913724710-56: ")
    return formatear_telefono(telefono)

def validar_telefono(telefono) -> bool:
    if telefono[3] == '-' and telefono[-3] == '-':
        return True
    else:
        return False

def main():
    telefono_usuario = pedir_telefono()
    print(f"Tu teléfono formateado es: {telefono_usuario}")

if __name__ == "__main__":
    main()