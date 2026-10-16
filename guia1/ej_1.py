"""Biseccion para encontrar la raiz mayor de un polinomio cuadratico."""

from math import sqrt


def f(x):
    return -0.5 * x**2 + 2.5 * x + 4.5


def main():
    a = -0.5
    b = 2.5
    c = 4.5

    discriminante = b**2 - 4 * a * c
    raiz_1 = (-b + sqrt(discriminante)) / (2 * a)
    raiz_2 = (-b - sqrt(discriminante)) / (2 * a)
    raiz_mayor = max(raiz_1, raiz_2)

    print(f"Raices por formula cuadratica: {raiz_1:.8f}, {raiz_2:.8f}")
    print(f"Raices aproximadas para el grafico: x = {raiz_1:.4f}, {raiz_2:.4f}")

    inferior = 5.0
    superior = 10.0
    anterior = None

    print("\nBiseccion (3 iteraciones):")
    print("n       x_i             error Ea (%)     error verdadero (%)")

    for iteracion in range(1, 4):
        medio = (inferior + superior) / 2
        error_verdadero = abs((raiz_mayor - medio) / raiz_mayor) * 100

        if anterior is None:
            print(
                f"{iteracion:<7}{medio:<16.8f}"
                f"{'---':<16}{error_verdadero:.6f}"
            )
        else:
            error_aproximado = abs((medio - anterior) / medio) * 100
            print(
                f"{iteracion:<7}{medio:<16.8f}"
                f"{error_aproximado:<16.6f}{error_verdadero:.6f}"
            )

        if f(inferior) * f(medio) < 0:
            superior = medio
        else:
            inferior = medio

        anterior = medio


if __name__ == "__main__":
    main()
