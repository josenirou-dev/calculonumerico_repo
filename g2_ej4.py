import matplotlib.pyplot as plt
import numpy as np
## definimos nuestra función a gráficar
def funcion(x):
    return -12 - 21 * x + 18 * (x**2) - 2.75 * (x**3)

# Generar la gráfica para identificar las raíces
x_grafica = np.linspace(-2, 6, 200)
y_grafica = funcion(x_grafica)

plt.figure(figsize=(8, 5))
plt.plot(x_grafica, y_grafica, label=r"$f(x) = -12 - 21x + 18x^2 - 2.75x^3$", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")

plt.title("Gráfica de f(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

# Método de Falsa Posición para la raíz más pequeña
limite_inferior = float(input("Ingrese el límite inferior del intervalo (a): "))
limite_superior = float(input("Ingrese el límite superior del intervalo (b): "))

# error con 3 cifras significativas
error_objetivo_porcentual = 0.05

aproximacion_anterior = None
numero_iteracion = 1
 ## se aplica la condición si f(a)*f(b) < 0 entonces se ejecuta el código
if funcion(limite_inferior) * funcion(limite_superior) < 0:
    print("Condición f(a)*f(b) < 0 cumplida. Iniciando cálculo:\n")
    while True: ## aplicamos formula 
        punto_interseccion = limite_superior - (funcion(limite_superior) * (limite_inferior - limite_superior)) / (funcion(limite_inferior) - funcion(limite_superior))
        
        if aproximacion_anterior is not None: ##iteramos el error aproximado porcentual
            error_aproximado_porcentual = abs((punto_interseccion - aproximacion_anterior) / punto_interseccion) * 100
        else:
            error_aproximado_porcentual = float('inf') ##infinito positivo 
            ## un print con los detalles de la iteración 
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_interseccion}, f(c) = {funcion(punto_interseccion)}, Error = {error_aproximado_porcentual}%")
        ## si el error aproximado porcentual es menor al error objetivo entonces se rompe el ciclo
        if error_aproximado_porcentual < error_objetivo_porcentual:
            print(f"\nRaíz más pequeña encontrada: c = {punto_interseccion}")
            break
        # actualizamos los límites del intervalo según el signo de f(c)
        if funcion(limite_inferior) * funcion(punto_interseccion) < 0:
            limite_superior = punto_interseccion
        else:
            limite_inferior = punto_interseccion
            
        aproximacion_anterior = punto_interseccion
        numero_iteracion += 1
else:
    print("No hay cambio de signo en ese intervalo. Revisa la gráfica e intenta con otros valores para a y b.")