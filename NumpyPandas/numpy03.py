'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np
np.random.seed(0)

age = np.random.randint(1, 100, size=10)
print("age :", age)

# 불 마스크(bool mask)
age_mask = (age >= 20) & (age <= 60)
print("age_mask :", age_mask)
print(age[(age >= 20) & (age <= 60)])

# 팬시 인덱싱(스마트 인덱싱)
print("age[[1, 3, -2]] :", age[[1, 3, -2]]) 

ind = np.array([[2, 5], [9, 1]])
print(age[ind])

x = np.arange(12).reshape((3, 4))
print("x :", x)

row = np.array([0, 1, 2])
col = np.array([3, 1, 0])
print(x[row, col])

print(x[2, [3, 1, 2]])

data = np.random.randint(1, 10, (3, 5))
print(data)

print(data[:, 2])
print(data[:, [2]])

