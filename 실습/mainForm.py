import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import urllib.request
from bs4 import BeautifulSoup

#화면로딩
form_class = uic.loadUiType("C:\\python_work\\mainForm.ui")[0]

class DemoForm(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("메인화면")

    def firstClick(self):
        f = open("c:\\python_work\\webtoon.txt", "wt", encoding="utf-8")
        #파일에 저장하기        
        for i in range(1,6):
            #기본 주소
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            #self.txtLog.append("조립한주소:", url) 
            #웹사이트에서 검색한 결과를 문자열로 받기
            data = urllib.request.urlopen(url)
            #검색이 용이한 객체 생성
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text
                self.txtLog.append("출력 : "+ title.strip()) 
                f.write(title.strip() + "\n")
        f.close()
        self.label.setText("웹 크롤링 종료")  
    def secondClick(self):
        self.label.setText("두번째")   
    def thirdClick(self):
        self.label.setText("세번째")   
    def fourthClick(self): 
        self.txtLog.setText("")#로그창 초기화
        for i in range(0, 20): 
            self.progressBar.setValue(i) 
            self.txtLog.append("로그창출력 : "+str(i)) 

#프로그램 실행
if __name__ =="__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
    