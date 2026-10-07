import matplotlib.pyplot as plt
import numpy as np

## sección para modelar la función cuadrática 
def f(x):
    return -0.5 * (x**2) + 2.5 * x + 4.5

valores_x = np.linspace(-2, 7, 100)
valores_y = f(valores_x)


plt.figure(figsize=(8, 5))
plt.plot(valores_x, valores_y, label=r"$f(x) = -0.5x^2 + 2.5x + 4.5$", color="blue", lw=2)


plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")


plt.title("Modelado de la Función Cuadrática")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

plt.show()


## Método de Bisección 

a = float(input("Ingrese el límite inferior del intervalo (a): "))
b = float(input("Ingrese el límite superior del intervalo (b): ")) 

## Ejecución del método de bisección

if f(a) * f(b) < 0:
    print("Se cumple la condición de cambio de signo. Se puede aplicar el método de bisección.")
    for i in range(10):
        c = (a + b) / 2
        print(f"Iteración {i+1}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")
        ## formula para calcular error a-b/a+b
        error = abs((a - b) / (a + b)) if (a + b) != 0 else float('inf')
        print(f"Error: {error}")
        if f(c) == 0:
            print(f"Se encontró una raíz exacta: {c}")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

## formula para calcular error a-b/a+b 