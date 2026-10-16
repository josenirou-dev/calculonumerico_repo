def calcular_mcd(numero_a, numero_b):
    while numero_b != 0:
        numero_a, numero_b = numero_b, numero_a % numero_b
    return numero_a


def main():
    numero_a = int(input("ingrese numero "))
    numero_b = int(input("ingrese numero "))
    mcd = calcular_mcd(numero_a, numero_b)
    mcm = (numero_a * numero_b) / mcd

    print("maximo común divisor es", int(mcd))
    print("minimo común múltiplo es", int(mcm))


if __name__ == "__main__":
    main()
