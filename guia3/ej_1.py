"""Newton-Raphson y biseccion para encontrar la raiz cubica de 20."""


def f(x):
    return x**3 - 20


def derivada(x):
    return 3 * x**2


def main():
    tolerancia = 0.005
    x = 3.0
    iteraciones_newton = 0

    print("Newton-Raphson, x0 = 3:")
    print("n    x_i              Ea (%)")

    while True:
        siguiente = x - f(x) / derivada(x)
        error = abs((siguiente - x) / siguiente) * 100
        iteraciones_newton = iteraciones_newton + 1

        print(f"{iteraciones_newton:<5}{siguiente:<18.10f}{error:.8f}")
        x = siguiente

        if error < tolerancia:
            break

    print(f"Raiz aproximada: {x:.10f}")

    inferior = 2.0
    superior = 3.0
    anterior = None
    iteraciones_biseccion = 0

    print("\nBiseccion en [2, 3]:")
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

    print(f"Raiz aproximada: {medio:.10f}")
    print(f"\nCriterio de ambos metodos: Ea < {tolerancia} %.")
    print(f"Iteraciones de Newton-Raphson: {iteraciones_newton}")
    print(f"Iteraciones de biseccion: {iteraciones_biseccion}")


if __name__ == "__main__":
    main()
