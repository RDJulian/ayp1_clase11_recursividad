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
    if numero < 0:
        raise ValueError("El numero ingresado es negativo.")
    resultado = 1
    for i in range(2, numero + 1):
        resultado = resultado * i
    return resultado


def main():
    print(calcular_factorial(25))


if __name__ == "__main__":
    main()
