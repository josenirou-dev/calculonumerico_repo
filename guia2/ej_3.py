"""Serie de McLaurin para aproximar cos(0.3*pi) a 8 cifras significativas."""

import math


def main():
    x = 0.3 * math.pi
    valor_real = math.cos(x)

    suma = 1.0
    termino = 1.0
    k = 0

    # El error relativo porcentual debe ser menor que 0.5 * 10**(2 - 8).
    tolerancia = 0.5 * 10**(2 - 8) / 100

    print(f"x = {x:.12f}")
    print(f"cos(x) = {valor_real:.12f}")
    print("terminos       aproximacion       Ea (%)          Et (%)")

    while True:
        siguiente = termino * (-x**2) / ((2 * k + 1) * (2 * k + 2))
        error_siguiente = abs(siguiente / valor_real)

        if error_siguiente < tolerancia:
            break

        termino = siguiente
        suma = suma + termino
        k = k + 1

        error_aproximado = abs(termino / suma) * 100
        error_verdadero = abs((valor_real - suma) / valor_real) * 100

        print(
            f"{k + 1:<15}{suma:<19.12f}"
            f"{error_aproximado:<16.8g}{error_verdadero:.8g}"
        )

    error_verdadero = abs((valor_real - suma) / valor_real) * 100
    print(f"\nTerminos usados: {k + 1}")
    print(f"Aproximacion: {suma:.12f}")
    print(f"Error relativo verdadero: {error_verdadero:.8g}%")


if __name__ == "__main__":
    main()
