"""Newton-Raphson y biseccion para resolver e**x - 3*x = 0."""

from math import exp


def f(x):
    return exp(x) - 3 * x


def derivada(x):
    return exp(x) - 3


def main():
    tolerancia = 0.05

    x = 0.0
    iteraciones_newton = 0

    print("Newton-Raphson, x0 = 0:")
    print("n    x_i              Ea (%)")

    while True:
        pendiente = derivada(x)

        if pendiente == 0:
            raise ZeroDivisionError("La derivada es cero.")

        siguiente = x - f(x) / pendiente
        error = abs((siguiente - x) / siguiente) * 100
        iteraciones_newton = iteraciones_newton + 1

        print(f"{iteraciones_newton:<5}{siguiente:<18.10f}{error:.8f}")
        x = siguiente

        if error < tolerancia:
            break

    inferior = 0.0
    superior = 1.0
    anterior = None
    iteraciones_biseccion = 0

    print("\nBiseccion en [0, 1]:")
    print("n    x_i              Ea (%)")

    while True:
        medio = (inferior + superior) / 2
        iteraciones_biseccion = iteraciones_biseccion + 1

        if anterior is None:
            print(f"{iteraciones_biseccion:<5}{medio:<18.10f}---")
        else:
            error = abs((medio - anterior) / medio) * 100
            print(f"{iteraciones_biseccion:<5}{medio:<18.10f}{error:.8f}")

            if error < tolerancia:
                break

        if f(inferior) * f(medio) < 0:
            superior = medio
        else:
            inferior = medio

        anterior = medio

    print(f"\nCriterio de ambos metodos: Ea < {tolerancia} %.")
    print(f"Iteraciones de Newton-Raphson: {iteraciones_newton}")
    print(f"Iteraciones de biseccion: {iteraciones_biseccion}")


if __name__ == "__main__":
    main()
