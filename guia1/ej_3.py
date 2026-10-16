"""Biseccion y falsa posicion para localizar la raiz mayor."""


def f(x):
    return -25 + 82 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5


def resolver_biseccion():
    inferior = 0.5
    superior = 1.0
    anterior = None

    print("\nBiseccion (Ea < 10 %):")
    print("n    x_i          f(x_i)        Ea (%)")

    for iteracion in range(1, 1001):
        actual = (inferior + superior) / 2

        if anterior is None:
            print(f"{iteracion:<5}{actual:<13.8f}{f(actual):<14.8f}---")
        else:
            error = abs((actual - anterior) / actual) * 100
            print(f"{iteracion:<5}{actual:<13.8f}{f(actual):<14.8f}{error:.6f}")

            if error < 10:
                return actual

        if f(inferior) * f(actual) < 0:
            superior = actual
        else:
            inferior = actual

        anterior = actual

    raise RuntimeError("La biseccion no convergio.")


def resolver_falsa_posicion():
    inferior = 0.5
    superior = 1.0
    anterior = None

    print("\nFalsa posicion (Ea < 0.2 %):")
    print("n    x_i          f(x_i)        Ea (%)")

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

            if error < 0.2:
                return actual

        if f(inferior) * f(actual) < 0:
            superior = actual
        else:
            inferior = actual

        anterior = actual

    raise RuntimeError("La falsa posicion no convergio.")


def main():
    print("La raiz mayor esta en el intervalo [0.5, 1.0].")
    resolver_biseccion()
    resolver_falsa_posicion()


if __name__ == "__main__":
    main()
