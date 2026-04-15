from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-20, 21)

y = np.where(x < 0, -(x**2), np.where(x > 0, x**3, 0))

colors = np.where(y < 0, 'red', np.where(y > 0, 'green', 'black'))

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y, color='darkblue', marker='d')
plt.title('Quadrados (Negativos) e Cubos (Positivos)')
plt.xlabel('Número Original')
plt.ylabel('Valor Calculado')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.bar(x, y, color='magenta')
plt.title('Gráfico de Barras')
plt.axhline(0, color='black')

plt.subplot(1, 3, 3)
plt.scatter(x, y, c=colors)
plt.title('Dispersão')
plt.axhline(0, color='black')

plt.tight_layout()
plt.show()