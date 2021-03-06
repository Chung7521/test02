'''
Created on 2021. 4. 8.

@author: user
'''
import re

p = re.compile("(빨강|초록|파랑)")
result = p.sub("컬러", "파랑 풍선 검정색 바지 빨강 치마 초록 바지")
print(result)
print()
result = p.sub("컬러", "파랑 풍선 검정색 바지 빨강 치마 초록 바지", count=1)
print(result)
print()

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
result = p.sub("\g<phone> \g<name>", "홍길동 010-8971-5623")
print(result)
print()

result = p.sub("\g<2> \g<1>", "홍길동 010-8971-5623")
print(result)
print()

#########################
