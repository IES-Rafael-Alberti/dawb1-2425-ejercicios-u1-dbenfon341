# Calcular la serie de Fibonacci hasta un número dado

def serie_fibonacci(num) -> str:
    serie = "1+1"
    a = 1
    b = 1

    for i in range(2, num):
        c = a + b
        serie += f"+{c}"
        if c > num:
            return serie
        a = b
        b = c
    return serie

def main():
    print(serie_fibonacci(10))

if __name__ == "__main__":
        main()