"""Cuatro iteraciones de Newton-Raphson para ln(x) + x - 2 = 0."""

from math import floor, log, log10


def f(x):
    return log(x) + x - 2


def derivada(x):
    return 1 / x + 1


def main():
    x = 1.0

    print("n    x_i              f(x_i)           Ea (%)")

    for iteracion in range(1, 5):
        siguiente = x - f(x) / derivada(x)
        error = abs((siguiente - x) / siguiente) * 100

        print(f"{iteracion:<5}{siguiente:<18.10f}{f(siguiente):<17.8g}{error:.8g}")
        x = siguiente

    if error == 0:
        cifras = "ilimitadas (error de maquina)"
    else:
        cifras = floor(2 - log10(2 * error))

    print(f"\nRaiz aproximada tras 4 iteraciones: {x:.10f}")
    print(f"Cifras significativas aproximadas: {cifras}")


if __name__ == "__main__":
    main()
