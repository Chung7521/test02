'''
Created on 2021. 4. 9.

@author: user
'''
import csv
import matplotlib.pyplot as plt
import numpy as np
plt.rc("font", family="Malgun Gothic")

with open("temperature.csv", "r") as a:    
    tem = csv.reader(a)
    next(tem)
    
    birth = []
    max = []
    min = []
    
    for row in tem:
        #print(row[0])
        
        date = row[0].split("-")
        #print(date)
        
        if int(date[0]) >= 1998:
            
            if date[1] == "02" and date[2] == "24":
                
                birth.append(row[0])
                #print(birth)
                max.append(float(row[4]))
                min.append(float(row[3]))
                
                
plt.plot(birth, min, color="purple", label="최저기온(℃)", linestyle="solid",
         linewidth="1")
plt.plot(birth, max, color="y", label="최고기온(℃)", linestyle="solid",
         linewidth="1")

plt.xticks(rotation=-45)
#plt.ylim([-7, 11])

plt.title("년도별 생일 기온")
plt.xlabel("날짜")
plt.ylabel("기온")
plt.legend(loc=0)
plt.grid()

plt.show()
                
                