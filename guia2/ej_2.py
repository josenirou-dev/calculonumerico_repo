"""Dos series para aproximar e**(-5), con 20 terminos."""

import math


def serie_directa():
    x = -5.0
    suma = 1.0
    termino = 1.0
    valor_real = 6.737947e-3

    print("\nSerie directa para e**(-5):")
    print("terminos       aproximacion       Ea (%)          Et (%)")

    for n in range(1, 20):
        termino = termino * x / n
        suma_anterior = suma
        suma = suma + termino

        error_aproximado = abs((suma - suma_anterior) / suma) * 100
        error_verdadero = abs((valor_real - suma) / valor_real) * 100

        print(
            f"{n + 1:<15}{suma:<19.11g}"
            f"{error_aproximado:<16.8g}{error_verdadero:.8g}"
        )

    print(f"Resultado con 20 terminos: {suma:.12g}")


def serie_reciproca():
    x = 5.0
    suma = 1.0
    termino = 1.0
    valor_real = 6.737947e-3

    print("\nReciproco de la serie para e**5:")
    print("terminos       aproximacion       Ea (%)          Et (%)")

    for n in range(1, 20):
        termino = termino * x / n
        suma_anterior = suma
        suma = suma + termino

        aproximacion = 1 / suma
        aproximacion_anterior = 1 / suma_anterior
        error_aproximado = abs(
            (aproximacion - aproximacion_anterior) / aproximacion
        ) * 100
        error_verdadero = abs((valor_real - aproximacion) / valor_real) * 100

        print(
            f"{n + 1:<15}{aproximacion:<19.11g}"
            f"{error_aproximado:<16.8g}{error_verdadero:.8g}"
        )

    print(f"Resultado con 20 terminos: {1 / suma:.12g}")


def main():
    print(f"Valor verdadero de referencia: {6.737947e-3:.9g}")
    serie_directa()
    serie_reciproca()


if __name__ == "__main__":
    main()
