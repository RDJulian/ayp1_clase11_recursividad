def __calcular_factorial(numero: int, resultado_parcial: int) -> int:
    """
    PRE: El número debe ser positivo.
    El valor de resultado_parcial debe ser 1 inicialmente.
    Esta función solo debería ser llamada por calcular_factorial().
    POST: Devuelve el factorial del número ingresado.
    """
    if numero < 0:
        raise ValueError("El numero ingresado es negativo.")
    if numero <= 1:
        return resultado_parcial
    else:
        return __calcular_factorial(numero - 1, resultado_parcial * numero)


def calcular_factorial(numero: int) -> int:
    """
    PRE: El número debe ser positivo.
    POST: Devuelve el factorial del número ingresado.

    TESTS:
    >>> calcular_factorial(0)
    1
    >>> calcular_factorial(3)
    6
    >>> calcular_factorial(5)
    120
    >>> calcular_factorial(-3)
    Traceback (most recent call last):
        ...
    ValueError: El numero ingresado es negativo.
    """
    return __calcular_factorial(numero, 1)


def main():
    print(calcular_factorial(25))


if __name__ == "__main__":
    main()
