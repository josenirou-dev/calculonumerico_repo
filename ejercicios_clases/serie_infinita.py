## hacer la sumatoria de 1/i a la cuarta 
import math 
sumas_parciales = []

n = int(input("Ingrese el número de términos para la sumatoria: "))

for i in range(1, n + 1):
    sumatoria = sum(1 / (j ** 4) for j in range(1, i + 1))
    sumas_parciales.append(sumatoria)

print("La sumatoria de 1/i^4 hasta", n, "términos es:", sumas_parciales[-1])

constante = (math.pi ** 4) / 90

error_absoluto = abs(constante - sumas_parciales[-1])
error_relativo = error_absoluto / constante
error_porcentual = error_relativo * 100

print(f"El error porcentual para {n} términos es: {error_porcentual}%")
print(f"El valor de la sumatoria es: {sumas_parciales[-1]} y el valor de la constante es: {constante}")
print(f"El error absoluto es: {error_absoluto} y el error relativo es: {error_relativo}")

## calcular lo mismo pero a la inversa 
serie_infinita_inversa = []

for a in range(n, 0,-1):
    sumatoria_inversa = sum(1 / (j ** 4) for j in range(1, a + 1))
    serie_infinita_inversa.append(sumatoria_inversa) 
print("La sumatoria inversa de 1/i^4 hasta", n, "términos es:", serie_infinita_inversa[0])

error_absoluto_inverso = abs(constante - serie_infinita_inversa[0])
error_relativo_inverso = error_absoluto_inverso / constante
error_porcentual_inverso = error_relativo_inverso * 100

print(f"El error porcentual para {n} términos es (inverso): {error_porcentual_inverso}%")
print(f"El valor de la sumatoria es (inverso): {serie_infinita_inversa[0]} y el valor de la constante es: {constante}")
print(f"El error absoluto es (inverso): {error_absoluto_inverso} y el error relativo es (inverso): {error_relativo_inverso}")