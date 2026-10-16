"""Tres iteraciones de falsa posicion para una funcion racional."""


def f(x):
    return (0.8 - 0.3 * x) / x


def main():
    raiz_exacta = 0.8 / 0.3
    inferior = 1.0
    superior = 3.0
    anterior = None

    print(f"Raiz analitica: {raiz_exacta:.8f}")
    print("n    x_r          Ea (%)        Et (%)")

    for iteracion in range(1, 4):
        f_inferior = f(inferior)
        f_superior = f(superior)
        actual = superior - f_superior * (inferior - superior) / (
            f_inferior - f_superior
        )

        error_verdadero = abs((raiz_exacta - actual) / raiz_exacta) * 100

        if anterior is None:
            print(
                f"{iteracion:<5}{actual:<13.8f}"
                f"{'---':<14}{error_verdadero:.6f}"
            )
        else:
            error_aproximado = abs((actual - anterior) / actual) * 100
            print(
                f"{iteracion:<5}{actual:<13.8f}"
                f"{error_aproximado:<14.6f}{error_verdadero:.6f}"
            )

        if f(inferior) * f(actual) < 0:
            superior = actual
        else:
            inferior = actual

        anterior = actual


if __name__ == "__main__":
    main()
