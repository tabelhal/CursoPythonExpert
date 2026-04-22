from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize=(18,5))

normal = np.random.normal(2, 1, 600)
potencias = []
x = np.random.uniform(0, 1, 150)
y = np.random.uniform(0, 1, 150)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1,11):
    potencias.append(2**i)

plt.subplot(1, 3, 1)
plt.title('Histograma Normal')
plt.hist(normal, color='coral', edgecolor='gray', bins=25)

plt.subplot(1, 3, 2)
plt.title('Potências de 2')
plt.bar(lista, potencias, color='navy')

plt.subplot(1, 3, 3)
plt.title('Scatter aleatório')
plt.scatter(x, y, color='limegreen')

plt.tight_layout()
plt.show()