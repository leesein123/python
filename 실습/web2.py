#네이버웹툰리스트.py
#주소: http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri


# <td class="title">
#                 <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
#                         </td>


import urllib.request 
# from urllib.request import * 
from bs4 import BeautifulSoup 

url = 'http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page='
f = open("c:\\work\\web.txt","wt",encoding="utf-8")

def getTitle(page):   
    curl= url+str(page)
    data = urllib.request.urlopen(curl)
    soup = BeautifulSoup(data, 'html.parser')
    cartoons = soup.find_all('td', class_='title')
    
    for item in cartoons:
        title = item.find('a').text
        print(title)
        f.write(title.strip() + "\n")


# getTitle(2)  
for page in range(1,5):
    getTitle(page)    
f.close()

print("크롤링 종료")
