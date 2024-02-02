def __calcular_sumatoria(numero: int, acumulador: int) -> int:
    """
    PRE: Numero tiene que ser estrictamente mayor a 0.
    El valor de acumulador debe ser 1 inicialmente.
    Esta función solo debería ser llamada por calcular_sumatoria().
    POST: Calcula la sumatoria desde 1 hasta el numero.
    """
    if numero < 1:
        raise ValueError
    if numero == 1:
        return acumulador
    else:
        return __calcular_sumatoria(numero - 1, acumulador + numero)


def calcular_sumatoria(numero: int):
    """
    PRE: Numero tiene que ser estrictamente mayor a 0.
    POST: Calcula la sumatoria desde 1 hasta el numero.

    TEST:
    >>> calcular_sumatoria(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> calcular_sumatoria(1)
    1
    >>> calcular_sumatoria(3)
    6
    >>> calcular_sumatoria(5)
    15
    >>> calcular_sumatoria(-2)
    Traceback (most recent call last):
        ...
    ValueError
    """
    return __calcular_sumatoria(numero, 1)


def main():
    print(calcular_sumatoria(20))


if __name__ == "__main__":
    main()
