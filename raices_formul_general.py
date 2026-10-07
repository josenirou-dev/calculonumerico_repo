## encontrar raíces con fórmula general 
 
import cmath
import math


a = int(input("Ingrese A:"))
b = int(input("Ingrese B:"))
c = int(input("Ingrese C:"))

discriminante = b**2 - 4 * a * c

if discriminante >= 0:
    raiz_1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz_2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Raiz 1: ", int(raiz_1))
    print("Raiz 2: ", int(raiz_2))
    print("Raiz 1.2: ", -b, "+ r", "(", discriminante, ")", "/", 2 * a)
    print("Raiz 2.1: ", -b, "- r", "(", discriminante, ")", "/", 2 * a)
else:
    raiz_1_compleja = (-b + cmath.sqrt(discriminante)) / (2 * a)
    raiz_2_compleja = (-b - cmath.sqrt(discriminante)) / (2 * a)
    print("Raiz 1 compleja: ", raiz_1_compleja)
    print("Raiz 2 compleja: ", raiz_2_compleja)
    print("Raiz 1.2 compleja: ", -b, "+ r", "(", discriminante, ")", "/", 2 * a)
    print("Raiz 2.1 compleja: ", -b, "- r", "(", discriminante, ")", "/", 2 * a)

