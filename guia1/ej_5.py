"""Biseccion para resolver sin(x) = x**2."""

from math import sin


def f(x):
    return sin(x) - x**2


def main():
    inferior = 0.5
    superior = 1.0
    anterior = None

    print("n    x_i          f(x_i)        Ea (%)")

    for iteracion in range(1, 101):
        medio = (inferior + superior) / 2

        if anterior is None:
            print(f"{iteracion:<5}{medio:<13.8f}{f(medio):<14.8f}---")
        else:
            error = abs((medio - anterior) / medio) * 100
            print(f"{iteracion:<5}{medio:<13.8f}{f(medio):<14.8f}{error:.6f}")

            if error < 2:
                break

        if f(inferior) * f(medio) < 0:
            superior = medio
        else:
            inferior = medio

        anterior = medio
    else:
        raise RuntimeError("La biseccion no convergio.")

    print(f"\nRaiz aproximada: {medio:.8f}")
    print(f"Comprobacion sin(x) - x**2 = {f(medio):.3e}")


if __name__ == "__main__":
    main()
