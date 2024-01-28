def fibonacci(n: int) -> int:
    """
    PRE: El número debe ser positivo.
    POST: Devuelve el enesimo número de la serie de Fibonacci.

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
    if n < 0:
        raise ValueError("El numero ingresado es negativo.")
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(fibonacci(25))


if __name__ == "__main__":
    main()
