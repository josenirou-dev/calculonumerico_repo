import math

x = 5 # -x = -5 / x= 5
n_terminos = 20
val_verdadero = math.exp(-5)   # Calcular el valor verdadero de e^-5 usando la función exp de la biblioteca math

# Variables para guardar las sumas acumuladas
suma_serie_alternada = 0
suma_serie_positiva = 0

for i in range(n_terminos): # Primera forma de calcular e^-x usando la serie de Maclaurin
    termino_m1 = ((-1)**i) * (x**i) / math.factorial(i) # -1 elevado a i, multiplicado por x elvado a i y debido por el factorial de i c: 
    suma_serie_alternada += termino_m1  # Se acumula el primer método.
    
    # Segunda forma de calcular e^-x usando la serie de Maclaurin
    termino_m2 = (x**i) / math.factorial(i) # lo mismo que arriba pero en positivo 
    suma_serie_positiva += termino_m2  # Se acumula el denominador del segundo método.
    resultado_m2 = 1 / suma_serie_positiva
    
    # Calcular los errores 
    error_m1 = abs((val_verdadero - suma_serie_alternada) / val_verdadero) * 100
    error_m2 = abs((val_verdadero - resultado_m2) / val_verdadero) * 100
    
    print(f"Término {i+1}:")
    print(f"  Método 1 = {suma_serie_alternada} | Error = {error_m1}%")
    print(f"  Método 2 = {resultado_m2} | Error = {error_m2}%")