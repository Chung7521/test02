'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

nums1 = np.array(range(1, 11), copy=True)
nums2 = np.array([10, 20, 30])
print(nums1, " - ", type(nums1))
print(nums2, " - ", type(nums2))
print()

print(nums1[5], " - ", nums1[-1])
print(nums1[2:9])
print()

ones = np.ones([2, 4], dtype=np.float64)
zeros = np.zeros([2, 4], dtype=np.float64)
empty = np.empty([2, 4], dtype=np.float64)
print(ones)
print(zeros)
print(empty)
print()

print(ones.ndim)
print(ones.shape)
print(ones.dtype)
print()

nums = np.arange(1, 10, 0.5)
print(nums)
