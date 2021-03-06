'''
Created on 2021. 4. 8.

@author: user
'''
import pandas as pd
import numpy as np

nums1 = [10, np.nan, 30]
print(1 + np.nan, " - ", 0*np.nan, " - ", sum(nums1))
print()

nums2 = pd.DataFrame([10, None, 30])
print(nums2.sum())
print(nums2.multiply(2))
print()

print(nums2.isnull())
print(nums2.notnull())
print()

print(nums2.dropna())
print(nums2.fillna(0))
print()

print(nums2.fillna(method="ffill"))
print(nums2.fillna(method="bfill"))
print()