'''
Created on 2021. 4. 8.

@author: user
'''
import pandas as pd

pop = pd.Series({"강서구": 445200, "구로구": 418700, "양천구": 466900, "관악구": 492600})
area = pd.Series({"강서구": 3830, "구로구": 3370, "양천구": 3520, "동작구": 3280})
states = pd.DataFrame({"population":pop, "area":area})
print(states)
print()

states.columns = ["pop", "area"]
print(states)
print()
print(states["pop"])
print()
print(states["pop"].values)
print()

print(pop.index)
print(states.index)
print(states["pop"].index)
print()

states.index.values[1] = "테스트"
print(states.index)
print()

print(states.keys())
print()

mem = [{'age': i * 10, 'income': i * 70} for i in range(2, 5)]
df_mem = pd.DataFrame(mem)
print(df_mem)
print()
print(df_mem["age"])
print(df_mem["age"][1], " - ", df_mem["age"].values)
print()

print(type(states["pop"]))
print(type(df_mem["age"]))
print(type(states))
print()

print(type(pop.values), " - ", type(states["pop"].values), " - ", type(states.values))
print(pop.values, " - ", states["pop"].values, " - ", states.values)