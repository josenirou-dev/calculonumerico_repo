"""Sumas parciales y error de la serie alternada de ln(2)."""


def suma_parcial(cantidad):
    suma = 0.0

    for n in range(1, cantidad + 1):
        if n % 2 == 0:
            suma = suma - 1 / n
        else:
            suma = suma + 1 / n

    return suma


def main():
    valor_real = 0.69314718056

    print("n    suma parcial       error absoluto    error relativo (%)")

    for cantidad in range(4, 9):
        suma = suma_parcial(cantidad)
        error_absoluto = abs(valor_real - suma)
        error_relativo = error_absoluto / valor_real * 100

        print(
            f"{cantidad:<5}{suma:<19.12f}{error_absoluto:<18.10g}"
            f"{error_relativo:.10g}"
        )

    # El siguiente termino de la serie alternada limita el error absoluto.
    cantidad = 1_000_000
    cota_error = 1 / (cantidad + 1)

    print(f"\nTerminos necesarios para garantizar un error menor que 1e-6: {cantidad}")
    print(f"Cota del error: {cota_error:.10g}")


if __name__ == "__main__":
    main()
