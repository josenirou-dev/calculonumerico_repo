import matplotlib.pyplot as plt
import numpy as np


##definir función a graficar
def funcion(x):
    return -25 + 82 * x - 90 * (x**2) + 44 * (x**3) - 8 * (x**4) + 0.7 * (x**5)

valores_grafica = np.linspace(0, 3.5, 200)
funcion_grafica = funcion(valores_grafica)

plt.figure(figsize=(8, 5))
plt.plot(valores_grafica, funcion_grafica, label=r"$f(x) = -25 + 82x - 90x^2 + 44x^3 - 8x^4 + 0.7x^5$", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Método Gráfico para f(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()
## ingresar el valor de a y b a partir de la gráfica
limite_inferior = float(input("Ingrese el límite inferior del intervalo (a): "))
limite_superior = float(input("Ingrese el límite superior del intervalo (b): "))
error_objetivo_porcentual = 10.0

aproximacion_anterior = None
numero_iteracion = 1

if funcion(limite_inferior) * funcion(limite_superior) < 0:
    print("Condición f(a)*f(b) < 0 cumplida. Iniciando Bisección:\n")
    while True:
        punto_medio = (limite_inferior + limite_superior) / 2
        
        if aproximacion_anterior is not None:
            error_aproximado_porcentual = abs((punto_medio - aproximacion_anterior) / punto_medio) * 100
        else:
            error_aproximado_porcentual = float('inf')
            
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_medio}, f(c) = {funcion(punto_medio)}, Error Aproximado Porcentual = {error_aproximado_porcentual}%")
        
        if error_aproximado_porcentual < error_objetivo_porcentual:
            print(f"\nRaíz aproximada (Bisección) con error < {error_objetivo_porcentual}%: c = {punto_medio}\n")
            break
            
        if funcion(limite_inferior) * funcion(punto_medio) < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio
            
        aproximacion_anterior = punto_medio
        numero_iteracion += 1
else:
    print("No se cumple la condición f(a)*f(b) < 0 en Bisección.\n")

##metodo de la falsa posición
limite_inferior = float(input("Ingrese el límite inferior del intervalo (a): "))
limite_superior = float(input("Ingrese el límite superior del intervalo (b): "))
error_objetivo_porcentual = 0.2 ## menor a esto

aproximacion_anterior = None
numero_iteracion = 1

if funcion(limite_inferior) * funcion(limite_superior) < 0:
    print("Condición f(a)*f(b) < 0 cumplida. Iniciando Falsa Posición:\n")
    while True:
        punto_interseccion = limite_superior - (funcion(limite_superior) * (limite_inferior - limite_superior)) / (funcion(limite_inferior) - funcion(limite_superior))
        
        if aproximacion_anterior is not None:
            error_aproximado_porcentual = abs((punto_interseccion - aproximacion_anterior) / punto_interseccion) * 100
        else:
            error_aproximado_porcentual = float('inf')
            
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_interseccion}, f(c) = {funcion(punto_interseccion)}, Error Aproximado Porcentual = {error_aproximado_porcentual}%")
        
        if error_aproximado_porcentual < error_objetivo_porcentual:
            print(f"\nRaíz aproximada (Falsa Posición) con error < {error_objetivo_porcentual}%: c = {punto_interseccion}\n")
            break
            
        if funcion(limite_inferior) * funcion(punto_interseccion) < 0:
            limite_superior = punto_interseccion
        else:
            limite_inferior = punto_interseccion
            
        aproximacion_anterior = punto_interseccion
        numero_iteracion += 1
else:
    print("No se cumple la condición f(a)*f(b) < 0 en Falsa Posición.\n")