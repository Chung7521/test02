'''
Created on 2021. 4. 12.

@author: user
'''

url1 = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
url2 = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

res_data = urllib.request.urlopen(url1).read()

soup = BeautifulSoup(res_data, "html.parser")

title = soup.find("title").string
description = soup.find("description").string
print("{} - {}".format(title, description))
print(soup.find("wf").string)