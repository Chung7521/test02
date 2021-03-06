'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

x = np.arange(4)
print(x + 3, " - ", x % 3)
print()

print(np.add(x, 3), " - ", np.mod(x, 3))
print()

np.random.seed()
a = np.random.randint(1, 10, 10)
b = np.random.randint(1, 10, 10)
print(a)
print(b)
print()

mask = np.greater(a, b)
print(a, " - ", b)
print(mask)
print()
print(a[mask])
print()

n1 = np.random.rand(3, 10)
ind = np.array([[0, 3], [1, 5], [2, 9]])
row = np.array([0, 1, 2])
col = np.array([3, 5, 9])
n1[row, col] = np.nan

print(n1, " - ", np.isnan(n1))
print()

n1[np.isnan(n1)] = 0
print(n1, " - ", n1[n1 > 0])
print()

x = np.random.randint(1, 100, size=(3, 5))
print(x)
print()

print(np.argmax(x))
print(np.argmin(x))
print()
print(np.argmax(x, axis=0))
print(np.argmin(x, axis=0))
print()

print(np.max(x), "-", np.min(x))
print(np.max(x, axis=0), "-", np.min(x, 0))