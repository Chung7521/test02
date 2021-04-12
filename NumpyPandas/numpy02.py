'''
Created on 2021. 4. 6.

@author: user
'''
# 난수 생성하기
import numpy as np

np.random.seed(0)
x = np.random.random()
rnd = np.random.random(10)
rnds = np.random.random((3, 3))

print("x :", x)
print("rnd :", rnd)
print("rnds :", rnds)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))
print("x1 : ", x1, " - ", x1.size)
print("x2 : ", x2, " - ", x2.size)
print("x3 : ", x3, " - ", x3.size)

# 균등 분포에서 표본을 추출해 3 x 2의 배열을 생성
r1 = np.random.rand(3, 2)
print("r1 : ", r1)
