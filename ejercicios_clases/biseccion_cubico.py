import matplotlib.pyplot as plt
import numpy as np
## definimos nuestra función a gráficar 
def f(x):
    return 5 * (x**3) - 5 * (x**2) + 6 * x - 2
## configuración de la gráfica 
x_grafica = np.linspace(-0.5, 1.5, 100)
y_grafica = f(x_grafica)

plt.figure(figsize=(8, 5))
plt.plot(x_grafica, y_grafica, label=r"$f(x) = 5x^3 - 5x^2 + 6x - 2$", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Método Gráfico para f(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

## ingresar el valor de a y b a partir de la gráfica 
print("Método de Bisección")
a = float(input("Ingrese el límite inferior del intervalo (a): "))
b = float(input("Ingrese el límite superior del intervalo (b): "))
## buscar que el error sea menor a 10% 
error_objetivo = 10.0

aproximacion_anterior = None
i = 1

if f(a) * f(b) < 0:
    print("Condición f(a)*f(b) < 0 cumplida. Iniciando bisección:\n") ## si la condición se cumple entonces se ejecuta 
    while True:
        c = (a + b) / 2 ## aplicamos formula 
        
        if aproximacion_anterior is not None: 
            error_relativo = abs((c - aproximacion_anterior) / c) * 100
        else:
            error_relativo = float('inf')
            
        print(f"Iteración {i}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}, error_relativo = {error_relativo}%")
        
        if error_relativo < error_objetivo:
            print(f"\nRaíz aproximada con error < {error_objetivo}%: c = {c}")
            break
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        aproximacion_anterior = c
        i += 1
else:
    print("No se cumple la condición f(a)*f(b) < 0. Intenta con otros valores de a y b.")