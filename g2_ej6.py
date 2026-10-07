import matplotlib.pyplot as plt
import numpy as np

# aca pongo la funcion igualada a cero 
def funcion(x):
    return np.log(x**2) - 0.7

# tiro unos puntos entre 0.1 y 3 para ver donde corta la curva
x_grafica = np.linspace(0.1, 3.0, 200)
y_grafica = funcion(x_grafica)

plt.figure(figsize=(8, 5))
plt.plot(x_grafica, y_grafica, label=r"$f(x) = \ln(x^2) - 0.7$", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfico de f(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()


# los valores que me da el ejercicio
limite_inferior = 0.5
limite_superior = 2.0

aproximacion_anterior = None


if funcion(limite_inferior) * funcion(limite_superior) < 0:
    # solo 3 vueltas como pide la guia
    for numero_iteracion in range(1, 4):
        punto_medio = (limite_inferior + limite_superior) / 2
        
        # el error solo se calcula desde la segunda vuelta
        if aproximacion_anterior is not None:
            error_aproximado_porcentual = abs((punto_medio - aproximacion_anterior) / punto_medio) * 100
        else:
            error_aproximado_porcentual = float('inf')
            
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_medio}, f(c) = {funcion(punto_medio)}, Error = {error_aproximado_porcentual}%")
        
        # ver para que lado achicamos el intervalo c: 
        if funcion(limite_inferior) * funcion(punto_medio) < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio
            
        
        aproximacion_anterior = punto_medio

    print(f"\nResultado final Bisección (3 vueltas): c = {punto_medio}\n")
else:
    print("No hay cambio de signo asi que no se puede hacer bisección\n")



# reinicio los limites
limite_inferior = 0.5
limite_superior = 2.0

aproximacion_anterior = None

if funcion(limite_inferior) * funcion(limite_superior) < 0:
    for numero_iteracion in range(1, 4):
        # la formula de la recta en falsa posicion
        punto_interseccion = limite_superior - (funcion(limite_superior) * (limite_inferior - limite_superior)) / (funcion(limite_inferior) - funcion(limite_superior))
        
        if aproximacion_anterior is not None:
            error_aproximado_porcentual = abs((punto_interseccion - aproximacion_anterior) / punto_interseccion) * 100
        else:
            error_aproximado_porcentual = float('inf')
            
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_interseccion}, f(c) = {funcion(punto_interseccion)}, Error = {error_aproximado_porcentual}%")
        
        # achicamos intervalo
        if funcion(limite_inferior) * funcion(punto_interseccion) < 0:
            limite_superior = punto_interseccion
        else:
            limite_inferior = punto_interseccion
            
        aproximacion_anterior = punto_interseccion

    print(f"\nResultado final Falsa Posición (3 vueltas): c = {punto_interseccion}")
else:
    print("No hay cambio de signo en falsa posición")