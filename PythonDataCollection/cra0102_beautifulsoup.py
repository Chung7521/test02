'''
Created on 2021. 4. 12.

@author: user
'''
from bs4 import BeautifulSoup 
html = """ 
<html>
     <body>
         <h1 id='title'>스크레이핑(Scraping)</h1>
         <p>웹 페이지에서 특정 정보를 추출하는 것</p>
         <p>스크레이핑 할 때 주로 BeautifulSoup을 사용</p>
         <div id='content'>
             <p class='sub_content'>
                 BeautifulSoup 라이브러리는 다운로드 기능은 없음
             </p>
             <p class='sub_content'>
                 BeautifulSoup 라이브러리를 사용하면 간편하게 데이터를 추출할 수 있음
             </p>
         </div>
     </body>
 </html>
"""
soup = BeautifulSoup(html, "html.parser")
print("h1 : {}".format(soup.html.h1.string))
print("p : {}".format(soup.html.p.string))
print("p : {}".format(soup.html.p))

print("title : {}".format(soup.find(id = "title").string))
print()

print(soup.find(name="div"))
print(soup.find(attrs={"class":"sub_content"}).string)
print()

print(soup.find_all(attrs={"class":"sub_content"}))
p_list = soup.find_all("p")

with open("web_scraping01.txt", "wt") as fout:
    for p in p_list:
        fout.write(p.string)
print("web_scraping01.txt 쓰기 완료")











