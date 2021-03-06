'''
Created on 2021. 4. 7.

@author: user
'''
import pandas as pd

se = pd.Series((4.1, 3.4, 3.8, 3.3, 3.5))
print(se)
print("len(se) :", len(se), se[1:4])
print(se[1], " - ", se.values, " - ", se.values[2:], " - ", se.index)
print("se.size :", se.size, " - ", se.ndim, " - ", se.shape, " - ", se.dtype)
print()

s = pd.Series([0.52, 0.56, 0.61, 0.49, 0.64], index=["a", "b", "c", "d", "e"])
print(s)
print(s[0], " = ", s["a"])
print()
print(s[["b", "a", "d"]].values)
print("\n\ns : {}\n\n".format(s))

print("s[(s >0.5) & (s < 0.6)] : {}\n".format(s[(s >0.5) & (s < 0.6)]))

s1 = s * 3
print("s1 : {}\n".format(s1))
s2 = s.values * 3
print("s2 : {}\n".format(s2))

ds = pd.Series({10:"a", 20:"b", 30:"c"})
print(ds.values)
print(ds[20])
ds.index = ["가", "나", "다"]
print(ds[1], ds["나"])
print(ds.index, " = ", ds.keys())
print()
ds = pd.Series(["a", "b", "c", "d"], index=[1, 3, 5, 7])
print(ds.loc[3:7], " = ", ds.iloc[1:3])

