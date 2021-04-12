'''
Created on 2021. 4. 12.

@author: user
'''
import json

with open("student.json", "rt", encoding="utf-8") as f:
    txt = f.read()
    
#print(txt)
  
s_loads = json.loads(txt)
print(s_loads)
print()
s_dumps = json.dumps(s_loads, ensure_ascii=False)
print(s_dumps)
print()

print(type(txt))
print(txt)
print()
print(type(s_loads))
print(s_loads)
print()
print(type(s_dumps))
print(s_dumps)