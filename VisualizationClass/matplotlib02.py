'''
Created on 2021. 4. 8.

@author: user
'''
import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", family="Malgun Gothic")

def scoreBarChart(names, score):
    plt.bar(names, score)
    plt.show()
    
def multiChart(names, score):
    plt.plot(names, score, "ro--")

if __name__ == "__main__":
    names=["홍길동", "이순신", "강감찬", "김유신", "임꺽정"]
    score=[89, 86, 97, 77, 92]
    
    scoreBarChart(names, score)