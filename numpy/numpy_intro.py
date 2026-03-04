import numpy as np

a = np.array([1, 2, 3, 4])
b = a * 2
m = np.array([[1, 2], [3, 4]]) #matriz
print(a)
print(b)
print(m)
print(np.mean(a)) #média
print(np.sum(a)) #soma
print(np.sqrt(a)) #raiz quadrada

x = np.array([[1, 2, 3], [4, 5 ,6], [7, 8, 9]])
soma = np.sum(x, axis=1)
x2 = x/soma[:, np.newaxis]
print(x2)

y = np.array([4, 7, 2, 9, 1, 6])
y[y > 5] = 99
y[y < 3] = 0
print(y)