import math

primos = []
numero = 2  # Empezamos a probar desde el primer número primo

# El bucle se detiene cuando alcanzamos los 100 primos
while len(primos) < 100:
    es_primo = True
    
    # Probamos si 'numero' es divisible por algún número anterior
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break  # Encontramos un divisor, no es primo
            
    if es_primo:
        primos.append(numero)  # Lo guardamos en la lista
        
    numero += 1  # Pasamos a evaluar el siguiente número

## print("Los primeros 100 números primos son:")
## print(primos)

## primos de mersene generar los primeros 10 y si son o no primos 

mersenne_primos = []
for p in primos[:10]:  # Tomamos los primeros 10 números primos
    mersenne = 2**p - 1  # Calculamos el número de Mersenne
    es_primo = True
    
    # Comprobamos si 'mersenne' es primo
    for divisor in range(2, math.isqrt(mersenne) + 1):
        if mersenne % divisor == 0: ## Si encuentra un número que lo divida y sea igual a 0 entonces no es primo :D
            es_primo = False
            break
            
    if es_primo:
        mersenne_primos.append(mersenne)  # Guardamos el número de Mersenne primo

print("Números de Mersenne primos generados a partir de los primeros 10 números primos:")
print(mersenne_primos)

## IMPORTANTE NO PROBAR CON UN FOR [:+10] PORQUE LOS NUMEROS CRECEN EXPONENCIALMENTE 