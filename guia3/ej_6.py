"""Eliminacion gaussiana para resolver un sistema de tres ecuaciones."""


def resolver_sistema(matriz, resultados):
    aumentada = []

    for i in range(3):
        fila = []

        for j in range(3):
            fila.append(float(matriz[i][j]))

        fila.append(float(resultados[i]))
        aumentada.append(fila)

    if aumentada[0][0] == 0:
        raise ValueError("El primer pivote no puede ser cero.")

    # Eliminamos x1 de la segunda y la tercera ecuacion.
    factor_2 = aumentada[1][0] / aumentada[0][0]
    factor_3 = aumentada[2][0] / aumentada[0][0]

    for columna in range(4):
        aumentada[1][columna] = (
            aumentada[1][columna] - factor_2 * aumentada[0][columna]
        )
        aumentada[2][columna] = (
            aumentada[2][columna] - factor_3 * aumentada[0][columna]
        )

    if aumentada[1][1] == 0:
        raise ValueError("El segundo pivote no puede ser cero.")

    # Eliminamos x2 de la tercera ecuacion.
    factor_3 = aumentada[2][1] / aumentada[1][1]

    for columna in range(1, 4):
        aumentada[2][columna] = (
            aumentada[2][columna] - factor_3 * aumentada[1][columna]
        )

    if aumentada[2][2] == 0:
        raise ValueError("El tercer pivote no puede ser cero.")

    x3 = aumentada[2][3] / aumentada[2][2]
    x2 = (aumentada[1][3] - aumentada[1][2] * x3) / aumentada[1][1]
    x1 = (
        aumentada[0][3] - aumentada[0][1] * x2 - aumentada[0][2] * x3
    ) / aumentada[0][0]

    return x1, x2, x3


def main():
    matriz = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]
    resultados = [8, -11, -3]

    x1, x2, x3 = resolver_sistema(matriz, resultados)

    print("Solucion del sistema:")
    print(f"x1 = {x1:.10g}")
    print(f"x2 = {x2:.10g}")
    print(f"x3 = {x3:.10g}")


if __name__ == "__main__":
    main()
