def generar_fibonacci(cantidad=10):
    secuencia = [1, 1]
    while len(secuencia) < cantidad:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:cantidad]


def calcular_cocientes(secuencia):
    return [secuencia[indice] / secuencia[indice - 1] for indice in range(1, len(secuencia))]


def main():
    secuencia = generar_fibonacci()
    cocientes = calcular_cocientes(secuencia)

    print("Los primeros 10 números de la secuencia de Fibonacci son:")
    print(secuencia)
    print("Límites de la secuencia de Fibonacci:")
    print(cocientes)
    print(f"Aproximación de lambda con n={len(secuencia)}:")
    print(f"λ ≈ {cocientes[-1]}")


if __name__ == "__main__":
    main()