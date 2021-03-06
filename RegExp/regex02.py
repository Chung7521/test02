'''
Created on 2021. 4. 8.

@author: user
'''
import re

s = "ABC bca abc cab abc ABC BAC"
p = re.compile("(abc)", re.IGNORECASE)
print(p.match(s).group())
print(p.search(s).group())
print()

for m in p.finditer(s):
    print(m.group())
print()

for m in p.finditer(s):
    print(m.span())
print()

st = """regexp-1 정규 표현식 기초
정규 표현식은 문자열에서 지정한 패턴에 해당하는... regexp-2 정규 표현식 활용 
정규 표현식에서 그룹을 지정하면 ABC...
RegExp-3 정규 표현식 실습
Regexp-4"""

p1 = re.compile("^regexp-[0-9]\s\w+", re.MULTILINE | re.I)
print(p1.findall(st))
print()