"""Suma de 1/i**4 en precision sencilla y en ambos sentidos."""

import math
import struct


def a_precision_sencilla(numero):
    return struct.unpack("f", struct.pack("f", numero))[0]


def sumar(indices):
    suma = a_precision_sencilla(0.0)

    for i in indices:
        termino = a_precision_sencilla(1.0 / i**4)
        suma = a_precision_sencilla(suma + termino)

    return suma


def main():
    cantidad = 10_000
    valor_real = math.pi**4 / 90

    suma_ascendente = sumar(range(1, cantidad + 1))
    suma_descendente = sumar(range(cantidad, 0, -1))

    error_ascendente = abs((valor_real - suma_ascendente) / valor_real) * 100
    error_descendente = abs((valor_real - suma_descendente) / valor_real) * 100

    print("Suma desde 1 hasta 10 000:")
    print(f"Suma = {suma_ascendente:.10f}")
    print(f"Error relativo porcentual verdadero = {error_ascendente:.8f}%")

    print("\nSuma desde 10 000 hasta 1:")
    print(f"Suma = {suma_descendente:.10f}")
    print(f"Error relativo porcentual verdadero = {error_descendente:.8f}%")

    print(f"\nValor limite pi**4 / 90 = {valor_real:.12f}")


if __name__ == "__main__":
    main()
