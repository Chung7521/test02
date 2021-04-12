'''
Created on 2021. 4. 8.

@author: user
'''
import matplotlib.pyplot as plt

def basicChart01():
    plt.title("line-chart")
    plt.plot([10, 20, 30, 40, 50], [30, 50, 90, 70, 80])
    plt.show()

def basicChart02():
    plt.rc("font", family="Malgun Gothic")
    plt.title("label을 지정해 범례 만들기")
    plt.plot([10, 20, 30, 40, 50], color="purple", label="A-Type", 
             linestyle="dashed", linewidth="2", marker="o", markersize="5")
    plt.plot([1., 2., 3., 4., 5.], [10, 50, 20, 40, 30], "ro:",
             label="B-Type", linewidth="5", markersize="10")
    plt.xlabel("speed")
    plt.ylabel("score")
    
    plt.legend(loc=0)
    plt.show()
    
def basicChart03():
    plt.rc("font", family="Malgun Gothic")
    plt.plot([60, 80, 100, 120, 150], [16.5, 18.0, 14.7, 14.2, 13.8], "g>-.")
    plt.title("속도에 따른 연비")
    plt.xlabel("속도")
    plt.ylabel("연비")
    plt.show()
        
if __name__ == "__main__":
    basicChart03()