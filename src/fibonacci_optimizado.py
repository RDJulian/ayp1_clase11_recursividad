def __fibonacci(n: int, n_menos1: int, n_menos2: int) -> int:
    """
    PRE: El número debe ser positivo.
    Los valores de n_menos1 y n_menos2 deben ser 1 y 0 inicialmente.
    Esta función solo debería ser llamada por fibonacci().
    POST: Devuelve el enesimo número de la serie de Fibonacci.
    """
    if n < 0:
        raise ValueError("El numero ingresado es negativo.")
    if n == 0:
        return n_menos2
    else:
        return __fibonacci(n - 1, n_menos1 + n_menos2, n_menos1)


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
    return __fibonacci(n, 1, 0)


def main():
    print(fibonacci(1000))


if __name__ == "__main__":
    main()
