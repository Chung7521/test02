'''
Created on 2021. 4. 7.

@author: user
'''
#데이터 합치기(결합)
import pandas as pd
import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

arr = np.concatenate([x, y, z])
print("arr : ", arr)
print()

x = [[1, 2], [3, 4]]
arr2 = np.concatenate([x, x], axis=0)
print("arr2 : \n", arr2)
print()
arr3 = np.concatenate([x, x], axis=1)
print("arr3 : \n", arr3)
print()

ser1 = pd.Series(["a", "b", "c"], index=[1, 2, 3])
ser2 = pd.Series(["d", "e"], index=[4, 5])
ser3 = pd.concat([ser1, ser2])
print("ser3 : \n", ser3)
print()

df1 = pd.DataFrame({"col1":[1, 2], "col2":[3, 4]})
df2 = pd.DataFrame({"col1":[5, 6], "col2":[7, 8]})
df3 = pd.concat([df1, df2], axis=0)
print("df3 : \n", df3)
print()

df4 = df1.append(df2)
print("df4 : \n", df4)





