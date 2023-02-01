def calcularFactorial(numero: int) -> int:
    """
    PRE: El número debe ser positivo.
    POST: Devuelve el factorial del número ingresado.
    """
    if numero < 0:
        raise ValueError("El numero ingresado es negativo.")
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado


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
