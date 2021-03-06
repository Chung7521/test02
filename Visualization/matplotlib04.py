'''
Created on 2021. 4. 9.

@author: user
'''
import matplotlib.pyplot as plt
import numpy as np

def plot_2_1():
    
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot([2, 4, 6, 8], [1, 3, 5, 7], "g>-")
    
    plt.subplot(2, 1, 2)
    plt.plot([20, 40, 60, 80], [-10, -30, -50, -70], "r<-.")
    
    plt.show()
    
    
from matplotlib03 import x_data, y_data 

def plot_2_2():
    
    fig = plt.figure()
    s1 = fig.add_subplot(2, 2, 1)
    s2 = fig.add_subplot(2, 2, 2)
    s3 = fig.add_subplot(2, 2, 3)
    s4 = fig.add_subplot(2, 2, 4)
    
    data = np.random.randint(1, 100, 100)
    
    s1.hist(data)
    
    s2.scatter(x_data, y_data)
    
    s3.plot(np.arange(50))
    
    s4.plot(np.random.rand(100), "g-", drawstyle="steps-mid")
    
    plt.show()


if __name__ == "__main__":
    #plot_2_1()
    plot_2_2()