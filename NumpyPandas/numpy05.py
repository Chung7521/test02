'''
Created on 2021. 4. 7.

@author: user
'''
# 유니버셜 함수
import numpy as np

x = np.arange(4)
print(x)
print(x + 3, " = ", x % 3)
print(np.add(x, 3), "--", np.mod(x, 3))
print()

np.random.seed(0)
a = np.random.randint(1, 10, 10)
b = np.random.randint(1, 10, 10)

mask = np.greater(a, b)
print(a, " - ", b)
print(mask)
print(a[mask])
print()

n1 = np.random.rand(3, 10)
# n1의 특정 요소가 nan이라고 가정
ind = np.array([[0, 3], [1, 5], [2, 9]])
row = np.array([0, 1, 2])
col = np.array([3, 5, 9])
n1[row, col] = np.nan
# isnan() 함수는 지정한 배열의 요소가 nan 이면 True를 반환
print("before : ", n1, " - ", np.isnan(n1))
# nan인 데이터를 모두 0으로 설정
n1[np.isnan(n1)] = 0
print("after : ", n1, " - ", n1[n1 > 0])
print()

x = np.random.randint(1, 100, size=(3, 5))
print(x)
print(np.argmax(x), " - ", np.argmin(x))
print(np.argmax(x, axis=0), " - ", np.argmin(x, axis=1))
