##generar números factoriales 
import math 

valores_factoriales = []
n= int(input("Ingrese euler elevado a que potencia desea calcular: "))

for i in range(1, n +1):  # Generamos los primeros 10 números factoriales
    factorial = math.factorial(i)
    valores_factoriales.append(factorial)


