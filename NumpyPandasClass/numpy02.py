'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

np.random.seed(0)
x = np.random.random()
rnd = np.random.random(10)
rnds = np.random.random((3, 3))
print(x)
print(rnd)
print(rnds)
print()

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))
print(x1, x1.size)
print(x2, x2.size)
print(x3, x3.size)
print()

r1 = np.random.rand(3, 2)
print(r1)
print()

b1 = np.random.binomial(10, 0.1, size=(2, 4))
print(b1)
print()

nums = np.array(range(1, 11))
print(nums)
np.random.shuffle(nums)
print(nums)