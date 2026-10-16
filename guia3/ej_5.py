"""Newton-Raphson para arctan(x) y comparacion con biseccion."""

from math import atan


def f(x):
    return atan(x)


def derivada(x):
    return 1 / (1 + x**2)


def newton(inicial):
    x = inicial

    print(f"\nNewton-Raphson con x0 = {inicial}:")
    print("n    x_i              Ea (%)")

    for iteracion in range(1, 13):
        siguiente = x - f(x) / derivada(x)

        if siguiente == 0:
            error = 0.0
        else:
            error = abs((siguiente - x) / siguiente) * 100

        print(f"{iteracion:<5}{siguiente:<18.10g}{error:.8g}")
        x = siguiente

        if abs(x) < 1e-12:
            print("El metodo convergio a cero.")
            return

        if abs(x) > 100:
            print("El metodo diverge y la aproximacion se aleja de cero.")
            return

    print("No convergio en 12 iteraciones.")


def biseccion():
    inferior = -1.0
    superior = 2.0

    for iteracion in range(1, 101):
        medio = (inferior + superior) / 2

        if abs(f(medio)) < 1e-6:
            print(
                f"\nBiseccion en [-1, 2]: raiz = {medio:.10g}, "
                f"iteraciones = {iteracion}"
            )
            return

        if f(inferior) * f(medio) < 0:
            superior = medio
        else:
            inferior = medio

    raise RuntimeError("La biseccion no convergio en 100 iteraciones.")


def main():
    newton(1.0)
    newton(1.5)
    biseccion()
    print("Biseccion mantiene el intervalo con cambio de signo entre iteraciones.")


if __name__ == "__main__":
    main()
