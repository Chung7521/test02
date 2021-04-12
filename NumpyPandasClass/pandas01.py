'''
Created on 2021. 4. 7.

@author: user
'''
import pandas as pd

se = pd.Series((4.1, 3.4, 3.8, 3.3, 3.5))
print(se)
print(len(se))
print(se[1], " - ", se.values, " - ", se.values[2:], " - ", se.index)
print()

s = pd.Series([0.52, 0.56, 0.61, 0.49, 0.64], index=["a", "b", "c", "d", "e"])
print(s)
print()

print(s[1], " - ", s["b"], " - ", s.values[2:4], " - ", s[["b", "d", "e"]].values)
print()
print(s[0:2])
print()
print(s[(s > 0.5) & (s < 0.6)])
print()

s1 = s * 3
print(s1)

s2 = s.values * 3
print(s2)
print()

ds = pd.Series({10:"a", 20:"b", 30:"c"})
print(ds)
print(ds[20], ds.values)
print()

ds.index = ["가", "나", "다"]
ds["나"] = "하"
print(ds)
print()

print(ds.index, " - ", ds["나"])
print(ds.keys(), " - ", "가"in ds)
print()

ds = pd.Series(["a", "b", "c", "d"], index=[1, 3, 5, 7])
print(ds.loc[3:7])
print(ds.iloc[1:3])
