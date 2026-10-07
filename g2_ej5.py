import matplotlib.pyplot as plt
import numpy as np

def funcion(x): ## definir funcion (se usa numpy para poder graficar y hacer operaciones matematicas)
    return np.sin(x) - x**2

# comoo siempree graficar c: 
x_grafica = np.linspace(0, 1.2, 200)
y_grafica = funcion(x_grafica)

plt.figure(figsize=(8, 5))
plt.plot(x_grafica, y_grafica, label=r"$f(x) = \sin(x) - x^2$", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Método Gráfico para f(x) = sin(x) - x^2")
plt.xlabel("Eje X (radianes)")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

# metodo de bisección para encontrar la raíz no trivial
print("--- Método de Bisección ---")
limite_inferior = 0.5 ## el ejercicio nos entrega los limites 
limite_superior = 1.0
error_objetivo_porcentual = 2.0 ## menor a esto

aproximacion_anterior = None
numero_iteracion = 1
## Aplicamos la misma formula de las veces anteriores 
if funcion(limite_inferior) * funcion(limite_superior) < 0:
    print("Condición f(a)*f(b) < 0 cumplida. Iniciando Bisección:\n")
    while True:
        punto_medio = (limite_inferior + limite_superior) / 2
        
        if aproximacion_anterior is not None:
            error_aproximado_porcentual = abs((punto_medio - aproximacion_anterior) / punto_medio) * 100
        else:
            error_aproximado_porcentual = float('inf')
            
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_medio}, f(c) = {funcion(punto_medio)}, Error = {error_aproximado_porcentual}%")
        
        if error_aproximado_porcentual < error_objetivo_porcentual:
            print(f"\nRaíz no trivial encontrada: c = {punto_medio}\n")
            break
            
        if funcion(limite_inferior) * funcion(punto_medio) < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio
            
        aproximacion_anterior = punto_medio
        numero_iteracion += 1

    # prueba de error de sustitución en la ecuación original
    raiz_obtenida = punto_medio
    resultado_sustitucion = funcion(raiz_obtenida)
    
    print(f"Sustituyendo x = {raiz_obtenida} en f(x) = sin(x) - x^2:")
    print(f"f({raiz_obtenida}) = {resultado_sustitucion}")
else:
    print("No se cumple la condición f(a)*f(b) < 0 en el intervalo proporcionado.")