"""Hacer una función recursiva que devuelva la sumatoria desde 1 hasta un número n
que se pase por parámetro. Probarla con un pequeño programa."""


def calcular_sumatoria(numero: int) -> int:
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
    if numero < 1:
        raise ValueError
    if numero == 1:
        return 1
    else:
        return numero + calcular_sumatoria(numero - 1)
