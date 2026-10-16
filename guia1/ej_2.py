"""Biseccion hasta que el error aproximado sea menor que 10 %."""


def f(x):
    return 5 * x**3 - 5 * x**2 + 6 * x - 2


def main():
    inferior = 0.0
    superior = 1.0
    anterior = None

    print("n    x_i          f(x_i)        Ea (%)")

    for iteracion in range(1, 101):
        medio = (inferior + superior) / 2

        if anterior is None:
            print(f"{iteracion:<5}{medio:<13.8f}{f(medio):<14.8f}---")
        else:
            error_aproximado = abs((medio - anterior) / medio) * 100
            print(
                f"{iteracion:<5}{medio:<13.8f}"
                f"{f(medio):<14.8f}{error_aproximado:.6f}"
            )

        if f(inferior) * f(medio) < 0:
            superior = medio
        else:
            inferior = medio

        if anterior is not None and error_aproximado < 10:
            break

        anterior = medio
    else:
        raise RuntimeError("La biseccion no convergio en 100 iteraciones.")

    print(f"\nRaiz menor aproximada: {medio:.8f}")


if __name__ == "__main__":
    main()
