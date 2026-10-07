import numpy as np
import matplotlib.pyplot as plt
def f(coeficiente):
    g, m, t, v = 9.8, 68.1, 10, 40
    return (g*m/coeficiente)*(1-np.exp(-(coeficiente/m)*t))-v
coeficientes = np.linspace(1, 25, 400)
plt.plot(coeficientes, f(coeficientes), color='#065A82')
plt.axhline(0, color='gray', lw=0.8)
plt.xlabel('c'); plt.ylabel('f(c)')
plt.grid(alpha=0.3)
plt.show()
# Reto: repita con sen(10x)+cos(3x)

