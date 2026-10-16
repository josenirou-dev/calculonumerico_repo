"""Tres iteraciones para resolver ln(x**2) = 0.7."""

from math import exp, log


def f(x):
    return log(x**2) - 0.7


def biseccion():
    inferior = 0.5
    superior = 2.0
    anterior = None

    print("\nBiseccion:")
    print("n    x_r          f(x_r)        Ea (%)")

    for iteracion in range(1, 4):
        actual = (inferior + superior) / 2

        if anterior is None:
            print(f"{iteracion:<5}{actual:<13.8f}{f(actual):<14.8f}---")
        else:
            error = abs((actual - anterior) / actual) * 100
            print(f"{iteracion:<5}{actual:<13.8f}{f(actual):<14.8f}{error:.6f}")

        if f(inferior) * f(actual) < 0:
            superior = actual
        else:
            inferior = actual

        anterior = actual


def falsa_posicion():
    inferior = 0.5
    superior = 2.0
    anterior = None

    print("\nFalsa posicion:")
    print("n    x_r          f(x_r)        Ea (%)")

    for iteracion in range(1, 4):
        f_inferior = f(inferior)
        f_superior = f(superior)
        actual = superior - f_superior * (inferior - superior) / (
            f_inferior - f_superior
        )

        if anterior is None:
            print(f"{iteracion:<5}{actual:<13.8f}{f(actual):<14.8f}---")
        else:
            error = abs((actual - anterior) / actual) * 100
            print(f"{iteracion:<5}{actual:<13.8f}{f(actual):<14.8f}{error:.6f}")

        if f(inferior) * f(actual) < 0:
            superior = actual
        else:
            inferior = actual

        anterior = actual


def main():
    print(f"Raiz positiva exacta: exp(0.35) = {exp(0.35):.8f}")
    biseccion()
    falsa_posicion()


if __name__ == "__main__":
    main()
