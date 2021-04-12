'''
Created on 2021. 4. 7.

@author: user
'''
import pandas as pd
import numpy as np

#누락된 데이터 처리
nums1 = [10, np.nan, 30]
print(1 + np.nan, " - ", 0*np.nan, " - ", sum(nums1))
print()

nums2 = pd.DataFrame([10, None, 30])
print(nums2)
print()
print("sum : ", nums2.sum(), "\n multiply :", nums2.multiply(2))
print()
print(nums2.isnull(), nums2.notnull())
print()
print("dropna() ", nums2.dropna(), "\n fillna() ", nums2.fillna(0))
print()
print("ffill : ", nums2.fillna(method="ffill"), "\nbfill : ", nums2.fillna(method="bfill"))

















