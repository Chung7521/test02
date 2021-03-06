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
    
def multiBarChart(names, score):
    plt.plot(names, score, "ro--")
    
    plt.plot([1, 2, 3], [70, 80, 90], "bo:")
    plt.plot([1, 1, 1], [10, 20, 30], "r>--", [4, 4, 4], [40, 50, 60], "y*-.")
    
    plt.text(3, 96, "평균 : {}".format(np.mean(score)))
    plt.grid(True)
    
    plt.xlabel("이름")
    plt.ylabel("점수")
    plt.title("국어 점수")
    plt.show()


if __name__=="__main__":
    names = ["홍길동", "이순신", "강감찬", "김유신", "임꺽정"]
    score = [89, 86, 97, 77, 92]
    
    #scoreBarChart(names, score)
    multiBarChart(names, score)