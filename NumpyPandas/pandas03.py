'''
Created on 2021. 4. 7.

@author: user
'''
import pandas as pd
import numpy as np

np_df = pd.DataFrame(np.random.randint(10, 20, size=(3, 3)),
                     columns=["A", "B", "C"],
                     index=[0, 1, 2])
print(np_df)
print()

np_df["D"] = [100, 200, 300]
print("np_df : \n{}\n".format(np_df))

print(np_df.values)
print(np_df.values[0])
print()

print(np_df.T)
print()
print(np_df)
print()

print(np_df.iloc[0:2, 0:2])
print(np_df.iloc[:2, :2])
print()
print(np_df.loc[:1, :"B"])
print()

print(np_df.A, np_df["A"])
print()

np_df.loc[0, "A"] = 100
np_df["A"].values[1] = 200
np_df.values[2, 2] =300
print(np_df)
print()

np_df = np_df * 10
print(np_df)
print()


pop = pd.Series({"강서구": 445200, "구로구": 418700, "양천구": 466900, 
 "관악구": 492600, "동작구": 431700})
area = pd.Series({"강서구": 3830, "구로구": 3370, "양천구": 3520, "관악구": 3960, "동작구": 3280})
states = pd.DataFrame({"pop":pop, "area":area})
print(states)
print()

states["density"] = states["pop"] / states["area"]
print(states)
print()

print(states.loc[states.density > 130, ["pop", "density"]])
print(states.loc["구로구":"관악구", ["pop", "area"]])

print(states.iloc[1:4, 0:2])
print(states.iloc[1:4, [0, 1]])

















