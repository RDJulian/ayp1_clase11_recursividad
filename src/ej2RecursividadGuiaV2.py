# Ejercicio resuelto por Nicolás Lopez

"""
Pre: Esta función solo debe ser llamada por suma_elementos()
Post: Devuelve el resultado obtenido cuando llega al final de la lista, o bien hace una llamada recursiva hasta
obtener ese resultado.
"""


def suma_elementos_rec(lista: list, indice_actual: int, resultado: int) -> int:
    if indice_actual >= len(lista):
        return resultado
    else:
        resultado += lista[indice_actual]
        return suma_elementos_rec(lista, indice_actual + 1, resultado)


"""
Pre: -
Post: Devuelve la suma de todos los elementos de lista.
"""


def suma_elementos(lista: list[int]) -> int:
    """
    >>> suma_elementos([1, 2, 3, 4, 5])
    15
    >>> suma_elementos([0])
    0
    >>> suma_elementos([54, 654, 23, 0, 0, 0])
    731
    >>> suma_elementos([5, -1, -2, -2])
    0
    >>> suma_elementos([])
    0
    """
    return suma_elementos_rec(lista, 0, 0)
