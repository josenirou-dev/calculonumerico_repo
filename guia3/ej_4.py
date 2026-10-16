"""Newton-Raphson para una raiz doble y comparacion con el ejercicio 3."""

from math import log


def f(x):
    return (x - 1)**2 * (x + 2)


def derivada(x):
    return 3 * x**2 - 3


def main():
    x = 1.0
    iteraciones_ejercicio_3 = 0

    while True:
        siguiente = x - (log(x) + x - 2) / (1 / x + 1)
        error = abs((siguiente - x) / siguiente) * 100
        iteraciones_ejercicio_3 = iteraciones_ejercicio_3 + 1
        x = siguiente

        if error < 0.1:
            break

    x = 2.0
    iteraciones_ejercicio_4 = 0

    print("Newton-Raphson para (x - 1)**2 * (x + 2) = 0:")
    print("n    x_i              Ea (%)")

    while True:
        siguiente = x - f(x) / derivada(x)
        error = abs((siguiente - x) / siguiente) * 100
        iteraciones_ejercicio_4 = iteraciones_ejercicio_4 + 1

        print(f"{iteraciones_ejercicio_4:<5}{siguiente:<18.10f}{error:.8f}")
        x = siguiente

        if error < 0.1:
            break

    print(f"\nRaiz aproximada: {x:.10f}")
    print(f"Iteraciones en el ejercicio 3 con Ea < 0.1 %: {iteraciones_ejercicio_3}")
    print(f"Iteraciones en el ejercicio 4: {iteraciones_ejercicio_4}")
    print("La raiz x = 1 es doble, por eso Newton-Raphson avanza mas lento.")

    print("\nPrueba de biseccion alrededor de x = 1:")
    print(f"f(0.5) = {f(0.5):.8f}")
    print(f"f(1.5) = {f(1.5):.8f}")
    print("No hay cambio de signo porque la raiz tiene multiplicidad par.")


if __name__ == "__main__":
    main()
