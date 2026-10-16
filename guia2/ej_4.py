"""Metodo de Heron para aproximar la raiz cuadrada de 10."""

import math


def calcular_raiz(inicial, cantidad):
    aproximacion = inicial
    valor_real = math.sqrt(10)

    print("n    aproximacion       error verdadero (%)")

    for iteracion in range(1, cantidad + 1):
        aproximacion = 0.5 * (aproximacion + 10 / aproximacion)
        error = abs((valor_real - aproximacion) / valor_real) * 100
        print(f"{iteracion:<5}{aproximacion:<19.12f}{error:.10g}")

    return aproximacion


def main():
    print("a) Cuatro iteraciones con x0 = 3:")
    calcular_raiz(3.0, 4)

    limite = 0.5 * 10**(2 - 6)

    print("\nb) Iteraciones necesarias con x0 = 3:")
    calcular_con_tolerancia(3.0, limite)

    print("\nc) Iteraciones necesarias con x0 = 10:")
    calcular_con_tolerancia(10.0, limite)


def calcular_con_tolerancia(inicial, limite):
    aproximacion = inicial
    valor_real = math.sqrt(10)
    iteracion = 0

    print("n    aproximacion       error verdadero (%)")

    while True:
        iteracion = iteracion + 1
        aproximacion = 0.5 * (aproximacion + 10 / aproximacion)
        error = abs((valor_real - aproximacion) / valor_real) * 100
        print(f"{iteracion:<5}{aproximacion:<19.12f}{error:.10g}")

        if error <= limite:
            break


if __name__ == "__main__":
    main()
