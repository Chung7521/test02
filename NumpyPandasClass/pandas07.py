'''
Created on 2021. 4. 8.

@author: user
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({"a":np.random.rand(5),
                            "b":np.random.rand(5)})
print(df)
print()

df1 = pd.DataFrame({"key": ["a", "b", "c", "a", "b", "c"],
                    "data": range(6)}, columns=["key", "data"])
print(df1)
print()

print(df1.groupby("key").sum())
print(df1.groupby("key"))
print()

np.random.seed(0)
df2 = pd.DataFrame({"key":["a", "b", "c", "a", "b", "c"],
                                "data1":range(6),
                                "data2":np.random.randint(0, 10, 6)},
                                columns=["key", "data1", "data2"])
print(df2)
print(df2.groupby("key").sum())
print()

print(df2.groupby("key").transform(lambda x:x-x.mean()))
print()

def norm_0(x):
    x["data1"] /= x["data2"].sum()
    return x
print(df2.groupby("key").apply(norm_0))