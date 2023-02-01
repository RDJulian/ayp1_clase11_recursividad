def calcularFibonacci(numero: int, resultado: int, resultadoAnterior: int) -> int:
    """
    PRE: El número debe ser mayor o igual a 1. Los valores de resultado y resultadoAnterior deben ser 1 y 0
    inicialmente. Esta función solo debería ser llamada por fibonacci().
    POST: Devuelve el enesimo número de la serie de Fibonacci.
    """
    if numero < 1:
        raise ValueError("El numero ingresado no es valido.")
    if numero == 1:
        return resultado
    else:
        return calcularFibonacci(numero - 1, resultado + resultadoAnterior, resultado)


def fibonacci(numero: int) -> int:
    """
    PRE: El número debe ser positivo.
    POST: Devuelve el enesimo número de la serie de Fibonacci.
    """
    if numero < 0:
        raise ValueError("El numero ingresado es negativo.")
    if numero <= 1:
        return numero
    else:
        return calcularFibonacci(numero, 1, 0)


def main() -> None:
    print(fibonacci(30))


main()

"""
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
