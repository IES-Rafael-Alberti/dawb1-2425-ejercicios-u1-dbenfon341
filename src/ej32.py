# Cálculo de un número aleatorio entre dos valores
import random

def numero_random(num1: int, num2: int) -> int:
    num_rand = random.randint(num1, num2)
    return num_rand

def main():
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce un segundo número: "))
    print(f"Tu número random es: {numero_random(num1, num2)}")

if __name__ == "__main__":
    main()