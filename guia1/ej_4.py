"""Falsa posicion para encontrar la raiz menor de un polinomio cubico."""


def f(x):
    return -12 - 21 * x + 18 * x**2 - 2.75 * x**3


def main():
    inferior = -1.0
    superior = 0.0
    anterior = None
    tolerancia = 0.05

    print("Raiz menor: intervalo inicial [-1, 0].")
    print("n    x_r          f(x_r)        Ea (%)")

    for iteracion in range(1, 1001):
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

            if error < tolerancia:
                break

        if f(inferior) * f(actual) < 0:
            superior = actual
        else:
            inferior = actual

        anterior = actual
    else:
        raise RuntimeError("La falsa posicion no convergio.")

    print(f"\nRaiz menor aproximada: {actual:.8f}")


if __name__ == "__main__":
    main()
