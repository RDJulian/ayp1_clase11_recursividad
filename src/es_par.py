import doctest


def es_par(numero: int) -> bool:
    """
    PRE:
    POST: Devuelve True si el numero es par.

    TESTS:
    >>> es_par(4)
    True
    >>> es_par(-1)
    False
    >>> es_par(0)
    True
    """
    return numero % 2 == 0


def main():
    print(es_par(4))


if __name__ == "__main__":
    main()
    print(doctest.testmod())
