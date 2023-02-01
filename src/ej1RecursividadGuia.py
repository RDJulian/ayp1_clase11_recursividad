# Ejercicio resuelto por Benjamín Sardini

# Precond: Se recibe un entero que debe ser positivo
# Postcond: Devuelve la sumatoria desde 1 hasta el número ingresado
def sumatoria(numero: int) -> int:
    if numero < 1:
        raise ValueError("El numero debe ser positivo")
    # Caso Base:
    if numero == 1:
        return numero
    # Otro caso
    else:
        return numero + sumatoria(numero - 1)


def main():
    numero = int(input("Ingrese un número positivo: "))
    print(sumatoria(numero))


main()
