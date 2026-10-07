import math

a = 10 # Raiz a encontrar 
valor_verdadero = math.sqrt(a)

x0 = 3 # se le asigna un valor inicial cercano 3x3= 9, cercano a 10
aproximacion = x0 # actualizamos el valor 

## parte a de la guía 
print("Parte a)") ## generamos 4 iteraciones y calculamos el error relativo porcentual
for i in range(1, 5):
    aproximacion = 0.5 * (aproximacion + a / aproximacion) ## Formula de la raiz cuadrada y nuevo valor de x :D
    error_rel_porcentual = abs((valor_verdadero - aproximacion) / valor_verdadero) * 100
    print(f"Iteracion {i}: x = {aproximacion}, Error relativo porcentual = {error_rel_porcentual}%") ## muestra el error relativo en cada iteración :D

tol_6_cifras = 0.5 * (10 ** (2 - 6)) ## formula para hacer una comparación de las 6 cifras significativas

aproximacion = x0 ## volvemos a definir x como 3 
iteraciones_b = 0 ## inicializamos una variable 

while True:
    x_nuevo = 0.5 * (aproximacion + a / aproximacion) ## lo mismo que la anterior sin embargo aca comparamos el error relativo porcentual, osea, que sean iguales en 6 cifras significativas
    iteraciones_b += 1
    error_rel_porcentual = abs((valor_verdadero - x_nuevo) / valor_verdadero) * 100
    if error_rel_porcentual < tol_6_cifras:
        break
    aproximacion = x_nuevo

print("\nParte b)")
print(f"Iteraciones necesarias con x0 = 3: {iteraciones_b}")

x0_c = 10  ## respuesta de la c, en vez de iniciar con 3, iniciamos con 10, y 10x10 es 100 por lo cual llevará mas iteraciones acercarse al valor de las cifras significativas
aproximacion = x0_c
iteraciones_c = 0
## usamos el mismo código de la vez pasada :D
while True:
    x_nuevo = 0.5 * (aproximacion + a / aproximacion)
    iteraciones_c += 1
    error_rel_porcentual = abs((valor_verdadero - x_nuevo) / valor_verdadero) * 100
    if error_rel_porcentual < tol_6_cifras:
        break
    aproximacion = x_nuevo

print("\nParte c)")
print(f"Iteraciones necesarias con x0 = 10: {iteraciones_c}")