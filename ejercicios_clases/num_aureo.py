import math

# numero aureo
num_aureo = (1 + math.sqrt(5)) / 2

# listas principales 
secuencia_fibonacci = [1, 1]
cocientes_consecutivos = []

# Bucle que genera la secuencia hasta que la división sea idéntica al numero aureo
while (secuencia_fibonacci[-1] / secuencia_fibonacci[-2]) != num_aureo:
    siguiente_numero = secuencia_fibonacci[-1] + secuencia_fibonacci[-2]
    secuencia_fibonacci.append(siguiente_numero)

# lista de límites (division entre cada termino c:)
for i in range(1, len(secuencia_fibonacci)):
    cociente = secuencia_fibonacci[i] / secuencia_fibonacci[i - 1]
    cocientes_consecutivos.append(cociente)

# mostrar resultados
print("--- RESULTADOS ---")
print(f"Número Áureo (fórmula matemática): {num_aureo}")
print("\nSecuencia de Fibonacci generada:")
print(secuencia_fibonacci)
print(f"Cantidad de números de Fibonacci necesarios: {len(secuencia_fibonacci)}")
print("\nLista de límites:")
print(cocientes_consecutivos)
print(f"\nAproximación final (último término de la división): {cocientes_consecutivos[-1]}")