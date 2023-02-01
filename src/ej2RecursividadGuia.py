def sumaDeElementos(lista: list[int]) -> int:
    """
    PRE:
    POST: Devuelve la suma de los elementos de la lista.

    """
    if len(lista) == 0:
        return 0
    else:
        return lista.pop() + sumaDeElementos(lista)


def main() -> None:
    print(sumaDeElementos([1, 2, 3, 4, 5]))


main()
