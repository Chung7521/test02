'''
Created on 2021. 4. 7.

@author: user
'''
import numpy as np

# 유니버셜 함수
nums = np.random.randint(1, 10, size=(4, 5))
print("nums :", nums)
print()

print("sum : ", np.sum(nums))
print("sum-axis=0 :", np.sum(nums, 0))
print("sum-axis=1 :", np.sum(nums, 1))
print("mean :", np.mean(nums))
print("mean-axis=0 :", np.mean(nums, 0))
print("mean-axis=1 :", np.mean(nums, 1))
print()

print(np.std(nums))
print(np.std(nums, 0))

# 이렇게도 사용 가능 =print("sum-axis=1 :", np.sum(nums, 1))
print(nums.sum(axis=1))



