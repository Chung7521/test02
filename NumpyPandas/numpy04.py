'''
Created on 2021. 4. 7.

@author: user
'''
# 브로드 캐스팅 - 벡터 연산
import numpy as np

n1 = list(range(1, 11))
n2 = list(range(11, 21))
n3 = n1 + n2
print(n3)

n = []
for i, v in enumerate(n1):
    n.append(n1[i] + n2[i])
print("n :", n)

l = [n1[i] + n2[i] for i, v in enumerate(n1)]
print(l)

n1 = np.array(n1)
n2 = np.array(n2)

n3 = n1 + n2
print("n3 :", n3)
print(l * 2)
print(n3 * 2)