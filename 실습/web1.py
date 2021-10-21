# page = open("c:\\work\\test01.html", encoding="utf-8").read()
# #검색이 용이한 객체(html태그 문서를 검색-상수)
# soup = BeautifulSoup(page, "html.parser")
# #soup = BeautifulSoup(page, "lxml")
# #print( soup.prettify() )

# #<p> 몽땅 검색
# print( soup.find_all("p") )
# #print( soup.find_all("p") )
# #<a> 태그 잡아와~~ 
# #print( soup.find_all("a") )
# #<p>태그 하나 검색
# #print( soup.find("p") )

# #검색 조건:<p class='outer-text'>
# #파이썬의 키워드로 class가 제공 그래서 이름 충돌 class_ 
# #print( soup.find_all("p", class_="outer-text") )

# #태그 안쪽에 컨텐츠만 가져오기
# for item in soup.find_all("p"):
#     #태그를 제거하고 컨텐츠만 가져오기 .text 
#     data = item.text.strip()
#     data = data.replace("\n", "")
#     data = data.replace("\t", "")
#     print(data)

from typing import Pattern
from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html",encoding="utf-8").read()


soup = BeautifulSoup(page,"html.parser")
# print(soup.prettify())
# print(soup.find_all("p"))
# print(soup.find("p"))
# print(soup.find_all("p",class_="outer-text"))
# print(soup.text)
for item in soup.find_all("p"):

    data = item.text.strip() #태그 제거하는거 .text ,   strip 은 공백 제거
    data = data.replace("\n","")
    data = data.replace("\t","")
    print(data)