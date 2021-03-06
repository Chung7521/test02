'''
Created on 2021. 4. 6.

@author: user
'''

import numpy as np

nums1 = np.array(range(1, 11), copy=True)
nums2 = np.array([10, 20, 30])

print(nums1, " - ", nums2) 
print(nums1, " - ", type(nums1))
print(nums2, " - ", type(nums2))
print(list(range(1, 11)))

print(nums1[5], " - ", nums1[-1])
print(nums1[2:9])

ones = np.ones([2, 4], dtype=np.float64)
zeros = np.zeros([2, 4], dtype=np.float64)
empty = np.empty([2, 4], dtype=np.float64)

print("ones :", ones)
print("zeros :", zeros)
print("empty :", empty)


print("ndim :", ones.ndim)

print("shape :", zeros.shape)

print("dtype :", empty.dtype)

nums = np.arange(1, 10, 0.5)
print(nums)












