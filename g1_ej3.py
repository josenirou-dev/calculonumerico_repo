import math
## error con cifras significativas 
cifras = 8
es = 0.5 * (10 ** (2 - cifras))  
angulo = 0.3 * math.pi  ## valor real           


suma = 0 ## iniciar las variables necesarias 
suma_anterior = 0
i = 0
ea = 100.0 ## inicia en 100 para que el programa corra c: 
print(f"Meta de error (es): {es}%\n") ## el error que hay que alcanzar 

## mientras ea sea mayor que es :
while ea > es:
    termino = ((-1)**i) * (angulo**(2*i)) / math.factorial(2*i) ## formula matemática para calcular cada término
     
    suma_anterior = suma
    suma += termino ## sumamos cada término al total de la suma 
    
    if i > 0:
        ea = abs((suma - suma_anterior) / suma) * 100 ## calculamos el error de cada suma (osea si le sumo un nuevo numero es que error me queda)
    
    i += 1  ## avanzamos la iteración c: 

print(f"Número de términos necesarios: {i}")
print(f"Aproximación alcanzada: {suma:.8f}") ## todo con 8 cifras significativas 
print(f"Valor real (math.cos):  {math.cos(angulo):.8f}")
print(f"Error aproximado final: {ea:.8e}%")