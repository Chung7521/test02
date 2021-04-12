'''
Created on 2021. 4. 8.

@author: user
'''
import re

p = re.compile("안녕|하이")
m = p.match("하이안녕")
m2 = p.findall("하이안녕")
print(m.group(), " - ", m2)
print()

s = """python.hwp
java.json.hwp
print.pdf
spring_프린트.hwp
자바스크립트.ajax.hw0
"""

p = re.compile("\w+[.]*\w+.hwp$", re.MULTILINE)
m = p.findall(s)
print(m)
print()

p1 = re.compile(r"\bclass\b")
m1 = p1.search("subclass")
m2 = p1.search("no class at")
print(m1, " - ", m2)
print()

p1 = re.compile(r"\Bclass\B")
m1 = p1.search("subclass1")
m2 = p1.search("no class at")
print(m1, " - ", m2)
