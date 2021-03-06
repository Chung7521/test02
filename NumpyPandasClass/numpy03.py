'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

np.random.seed(0)
age = np.random.randint(1, 100, size=10)
print(age)
print()

age_mask = (age >= 20) & (age <= 60)
print(age_mask)
print()

age2 = age[age_mask]
print(age2)
print()

print([age[1], age[3], age[-2]])
print()

print(age[[1, 3, -2]])
print()

ind = np.array([[2, 5], [9, 1]])
print(age[ind])
print()

x = np.arange(12).reshape((3, 4))
print(x)
print()

row = np.array([0, 1, 2])
col = np.array([3, 1, 0])
print(x[row, col])
print()

print(x[2, [3, 1, 2]])
print()

print(x[1:, [3, 1]])
print()

data = np.random.randint(1, 10, (3, 4))
print(data)
print()

print(data[:, 2])
print(data[:, [2]])