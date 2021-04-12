'''
Created on 2021. 4. 9.

@author: user
'''
from konlpy.tag import Okt
from collections import Counter

import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")

import pytagcloud
import webbrowser

import json
import re

def showBarChart(wordInfo):
    pass


def saveWordCloud(wordInfo, fileName):
    pass


if __name__ == "__main__":
    
    openFileName = "kbsnews_words.json"
    cloudImagePath = openFileName + ".jpg"
    
    readFile = open(openFileName, "r", encoding="utf-8").read()
    
    jsonData = json.loads(readFile)
    print(jsonData)
    
    message=""
    
    for item in jsonData:
        if "message" in item.keys():
            message = message + re.sub(r"[^\w]", "", item["message"])
    print("message : \n", message)
    
    # 품사 클래스의 인스턴스를 생성하고 message에서 명사만 추출
    nlp = Okt()
    nouns = nlp.nouns(message)
    
    # 추출한 명사의 빈도 수 세기
    count = Counter(nouns)
    print("nouns :\n", nouns)
    print("count :\n", count)
    
    