#form1.py
#form1.ui + form1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#화면로딩
form_class = uic.loadUiType("form1.ui")[0]

class DemoForm(QDialog,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lblTitle.setText("테스트 ui")
        self.pushButton.clicked.connect(self.functionStart)
        
    def functionStart(self): 
        self.progressBar.setRange(0, 19) 
        #progressbar 초기 설정(100을 0~19, 20단계로 나눔) 
        for i in range(0, 20): 
            print("출력 : ",str(i)) 
            self.progressBar.setValue(i) 
            #progress bar 진행률 올리기 
            self.txtLog.append("출력 : "+str(i)) 
            #text browser 문자열 추가하기




if __name__ =="__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()