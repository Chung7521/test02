'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

n1 = range(1, 11)
n2 = range(11, 21)
print(n1)
print(n2)
print()

n = []
for i, v in enumerate(n1):
    n.append(n1[i] + n2[i])
print(n)
print()

l = [n1[i] + n2[i] for i, v in enumerate(n1)]
print(l)
print()

n1 = np.array(n1)
n2 = np.array(n2)
n3 = n1 + n2
print(n3)
print()

print(n * 2)
print(n3 * 2)