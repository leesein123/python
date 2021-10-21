# coding:utf-8
from os import times
from bs4 import BeautifulSoup
import urllib.request
#검색을 위한 정규표현식 
import re 
import time
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,10):
        #클리앙의 중고장터 주소 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        # print( data )
        time.sleep(2)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #혹시 한글이 깨지면 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

    #    <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=446600&amp;s_no=446600&amp;page=1" target="_top">오징어게임 오일남이 깐부치킨광고 거절한 이유</a><span class="list_memo_count_span"> [27]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>
        #위 태그를 아래 find_all 에서 찾는다.  td 중 class 가 subject 인것만 가져옴
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        title = item.find("a").text
                        # print( title.strip() )
                        if (re.search('오징어', title)):
                                print(title.strip())
                except:
                        pass

    