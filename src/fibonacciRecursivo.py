def fibonacci(numero: int) -> int:
    """
    PRE: El número debe ser positivo.
    POST: Devuelve el enesimo número de la serie de Fibonacci.
    """
    if numero < 0:
        raise ValueError("El numero ingresado es negativo.")
    if numero <= 1:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


def main() -> None:
    print(fibonacci(30))


main()

"""
TESTS:
>>> fibonacci(-1)
Traceback (most recent call last):
    ...
ValueError: El numero ingresado es negativo.
>>> fibonacci(0)
0
>>> fibonacci(1)
1
>>> fibonacci(5)
5
"""
