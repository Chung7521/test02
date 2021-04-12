'''
Created on 2021. 4. 8.

@author: user
'''
import re

p = re.compile("(ABC)+")
s = "ABCDEABDABCFABC"
print(p.findall(s))
print()

p = re.compile("(ABC)+")
s = "ABCDEABDABCFABCAACABCABCCCABC"
print(p.findall(s))
print()

p1 = re.compile(r"\w+\s+\d+[-]\d[-]\d+")
p2 = re.compile("\w+\s+\d+[-]\d[-]\d+")
#print(p1.search("홍길동 010-8971-5623").group())
#print(p2.search("홍길동 010-8971-5623").group())
print()

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
print(p.search("홍길동 010-2222-1234").group())
print(p.search("홍길동 010-2222-1234").group(0))
print(p.search("홍길동 010-2222-1234").group(1))
print(p.search("홍길동 010-2222-1234").group(2))
print()

p = re.compile(r"(\b\w+)\s+\1")
print(p.search("우리의 봄에는 봄에는 많은 꽃들이 핀다.").group())
print(p.search("우리의 봄에는 봄에는 많은 꽃들이 핀다. 우리의 여름 여름 그리고 가을...").group())
print(p.findall("우리의 봄에는 봄에는 많은 꽃들이 핀다. 우리의 여름 여름 그리고 가을..."))
print()

for m in p.finditer("우리의 봄에는 봄에는 많은 꽃들이 핀다. 우리의 여름 여름 그리고 가을..."):
    print(m.group())
print()

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m = p.search("홍길동 010-8971-5632")
print("이름 : {}, 전화번호 : {}".format(m.group("name"), m.group("phone")))
