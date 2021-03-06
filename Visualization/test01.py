
import matplotlib.pyplot as plt
import csv

list_data = []
start_year = 2020 - 30
temp = []
year_label = []

#with는 따로 close필요 없음
with open("seoul_temp_20201026.csv", "r") as f:
    csv_read = csv.reader(f)
    header = next(csv_read)
    print(header) #
    
    max_temp = []
    min_temp = []
    date = []
    
    for row in csv_read:
        #print(row)['2020-10-24', '108', '8.7', '3.2', '14']
        #날짜, 최저기온, 최고기온
        #print(row[0], row[3], row[4])
        date = row[0].split("-")
        
        if int(date[0]) > start_year and row[-3] !="":
            
            if date[1] == "01" and date[2] == "01":
                year_label.append(date[0]) #년도만 date[0]
                temp.append(float(row[-3]))
            
plt.rc("font", family="Malgun Gothic")   
plt.title("최근 30년 서울 1월 1일 평균 온도")
plt.figure(figsize=(12, 6))

plt.plot(temp, "darkblue", label="평균기온")
plt.xticks(range(1, 31), year_label, rotation=-45)
plt.xlabel("년도")
plt.ylabel("온도")
plt.legend(loc=0)
plt.grid()


plt.show()

            
    
        