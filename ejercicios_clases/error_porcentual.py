import math

# numero aureo
num_aureo = (1 + math.sqrt(5)) / 2

# listas principales 
lista_fibonacci = [1, 1]
lista_de_limites = []

# Bucle que genera la secuencia hasta que la división sea idéntica al numero aureo
while (lista_fibonacci[-1] / lista_fibonacci[-2]) != num_aureo:
    siguiente_num = lista_fibonacci[-1] + lista_fibonacci[-2]
    lista_fibonacci.append(siguiente_num)

# lista de límites (division entre cada termino c:)
for i in range(1, len(lista_fibonacci)):
    limite = lista_fibonacci[i] / lista_fibonacci[i - 1]
    lista_de_limites.append(limite)

# error porcentual c: 
## Ea= x-xm (xm valor medido) Er= Ea/x (error relativo) Ep= Er*100 (error porcentual)
errores_absolutos = []
errores_relativos = []
errores_porcentuales = []
for i in range(len(lista_de_limites)):
    Ea = abs(num_aureo - lista_de_limites[i])
    Er = Ea / num_aureo
    Ep = Er * 100
    errores_absolutos.append(Ea)
    errores_relativos.append(Er)
    errores_porcentuales.append(Ep)

# ingresar un porcentaje de error para determinar el número de términos necesarios
porcentaje_error = float(input("Ingrese el porcentaje de error deseado: "))

for i in range(len(errores_porcentuales)):
    if errores_porcentuales[i] <= porcentaje_error:
        print(f"El error porcentual alcanzado es: {errores_porcentuales[i]}%")
        print(f"El límite alcanzado es: {lista_de_limites[i]}")
        print(f"El número de términos necesarios para alcanzar el error deseado es: {i + 1}")
        break
else:
    print("No se alcanzó el error deseado con la secuencia generada.")
