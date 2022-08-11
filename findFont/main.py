import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import time
import os

UI_class = uic.loadUiType("screen.ui")[0]

class MyWindow(QMainWindow, UI_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.indicate)
        '''
        self.initUI()
        # 도화지 코드의 이 위치에 아래 코드 한 줄을 추가할 것
        self.setWindowTitle("폰트 검색기")
        # 크기 ( 시작X,Y 가로 세로 )
        self.setGeometry(100,100,1920,1080)
        # 아이콘
        self.setWindowIcon(QIcon("icon.png"))
       
    def initUI(self):
        btn = QPushButton("누르세요",self)
        btn.clicked.connect(self.surprise)

    def surprise(self):
        print("!!!!")
        '''
    def indicate(self):
        text = self.textEdit.toPlainText()
        print(text)
        print(self.label.setText(text))

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = MyWindow()
        window.show()
        app.exec_()
    except KeyboardInterrupt:
        pass

app.exec_()

