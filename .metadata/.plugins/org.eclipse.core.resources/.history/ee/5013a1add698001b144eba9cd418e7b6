'''
Created on 2021. 4. 9.

@author: user
'''
import matplotlib.pyplot as plt
import numpy as np

def chartLineStyle():
    
    x = np.linspace(0, 10, 1000)
    
    plt.plot(x, np.sin(x - 0), color="blue", label="solid", linestyle="solid", linewidth=3)
    plt.plot(x, np.sin(x - 1), color="g", label="dashed", linestyle="dashed", lw=3)
    
    plt.plot(x, np.sin(x - 2), color="0.75", label="gray solid", linestyle="solid")
    
    plt.plot(x, np.sin(x - 3), color="#FFDD44", label="dotted", linestyle="dotted")
    plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3), label="point dashed", linestyle="-.")
    
    plt.plot(x, np.sin(x - 5),"-g", label="solid green")
    
    plt.axis([0, 10, -1.5, 1.5])
    #plt.axis("off")
    
    plt.legend(loc="upper center", fancybox=True, shadow=True,
               ncol=3, bbox_to_anchor=(0.01, 1.30, 0.98, -0.2))
    
    plt.show()
    #plt.savefig("scatterChart01.png")

def scatterChart(x_data, y_data):
    plt.scatter(x_data, y_data, c="y", edgecolors="r")
    #plt.plot(x_data, y_data, "bo", markeredgecolor="r")
    
    plt.show()

def multiLineChart():
    np.random.seed(0)
    data1 = np.random.randn(50)
    data2 = np.random.randn(50)
    
    plt.plot(data1, color="r", label="step", drawstyle="steps-post")
    plt.plot(data2, color="g", label="line")
    
    plt.title("Multi Line Chart")
    plt.xlabel("stage")
    plt.ylabel("random num")
    plt.legend(loc="best")
    
    plt.show()

def multiSizeScatter():
    
    rng = np.random.RandomState(0)
    
    x = rng.randn(100)
    y = rng.randn(100)
    
    colors = rng.rand(100)
    sizes = 1000 * rng.rand(100)
    
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.3)
    
    plt.colorbar()
    plt.show()


#산점도 데이터
point_list =[]
for i in range(100):
    x = np.random.normal(0, 1)
    y = x * 0.1 + 0.2 + np.random.normal(0, 1)
    
    # [[x, y], [x, y], [x, y], ....]
    point_list.append([x, y])
    
    x_data = [x[0] for x in point_list]
    y_data = [y[1] for y in point_list]
    print(x_data)
    print(y_data)


if __name__ == "__main__":
    #chartLineStyle()
    #scatterChart(x_data, y_data)
    #multiLineChart()
    multiSizeScatter()