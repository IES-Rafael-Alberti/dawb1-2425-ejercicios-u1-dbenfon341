# Desarrolla una función en prueba1.py que reciba dos números y retorne 
# el mayor número de los dos o 0 si son iguales. Realiza las pruebas unitarias y ejecútalas con pytest desde la terminal 
# (puedes hacerlo en la terminal dentro de Visual Studio Code).

def num_mayor(num1:int, num2:int) -> int:
    if num1 == num2:
        return 0
    elif num1 > num2:
        return num1
    else:
        return num2