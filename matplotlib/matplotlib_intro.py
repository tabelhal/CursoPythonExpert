from matplotlib import pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
y = x**2
print(y)
plt.title('Gráfico dos primeiros 15 números')
plt.xlabel('Número')
plt.ylabel('Quadrado do número')
plt.plot(x,y, color='purple', marker='o')
plt.grid(True)
plt.show()