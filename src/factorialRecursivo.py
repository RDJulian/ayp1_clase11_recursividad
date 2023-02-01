def calcularFactorial(numero: int) -> int:
    """
    PRE: El número debe ser positivo.
    POST: Devuelve el factorial del número ingresado.
    """
    if numero < 0:
        raise ValueError("El numero ingresado es negativo.")
    if numero <= 1:
        return 1
    else:
        return numero * calcularFactorial(numero - 1)


def main() -> None:
    print(calcularFactorial(30))


main()

"""
TESTS:
>>> calcularFactorial(0)
1
>>> calcularFactorial(3)
6
>>> calcularFactorial(-3)
Traceback (most recent call last):
    ...
ValueError: El numero ingresado es negativo.
"""
