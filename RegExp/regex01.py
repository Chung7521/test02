'''
Created on 2021. 4. 8.

@author: user
'''
import re

pat = re.compile("[가-힣]{2,5}")
s = "안녕하세요 우리 my schooll 오늘은 날씨가 별로네요"
print(pat)
print(type(pat))
print(pat.match(s))
print(pat.search(s))
print(pat.findall(s))
print()

print(pat.finditer(s))
for s in pat.finditer(s):
    print(s)
print()

s2 = "spython"
pat2 = re.compile("python")
print(pat2.match(s2))
print(pat2.search(s2))