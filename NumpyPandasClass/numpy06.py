'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

nums = np.random.randint(1, 10, size=(4, 5))
print(nums)
print()

print(np.sum(nums))
print(np.sum(nums, 0))
print(np.sum(nums, 1))
print()

print(np.std(nums))
print(np.std(nums, 0))
print(np.std(nums, 1))