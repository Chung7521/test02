'''
Created on 2021. 4. 12.

@author: user
'''
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

res_data = req.urlopen(url).read()

soup = BeautifulSoup(res_data, "html.parser")

kospi = soup.select_one("span#KOSPI_now").string
temp_span = soup.select_one("span#KOSPI_change > span")
kospi_change = temp_span.next_sibling
print(kospi, " - ", kospi_change)

span_list = soup.select("li > a.mnu2 span")
for span in span_list:
    #print(span)
    if "id" in span.attrs:
        if span.attrs["id"] == "KOSDAQ_now":
            print(span.string, end=" - ")
        else:
            print(list(span.children)[2])
