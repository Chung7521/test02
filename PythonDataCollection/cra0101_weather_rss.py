'''
Created on 2021. 4. 12.

@author: user
'''

url1 = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
url2 = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

import urllib.request
import urllib.parse

res_data = urllib.request.urlopen(url1).read()
#print(res_data[0:100])
text1 = res_data.decode("utf-8")
#print("text1 \n", text1)

req_data = {"stnId":109}
params = urllib.parse.urlencode(req_data)
res_data = urllib.request.urlopen(url2 + "?" + params).read()
text2 = res_data.decode("utf-8")
print("text\n", text2)