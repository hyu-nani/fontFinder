import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time
from PySide2.QtUiTools import loadUiType
import os

page = 1
fontSize = 11
fontList = os.listdir('./fonts/')
# QFont 데이터 베이스 입력
#for i in range(len(fontList)):
#    QFontDatabase.addApplicationFont('fonts/'+fontList[i])


UI_class = uic.loadUiType("screen.ui")[0]

class MyWindow(QMainWindow, UI_class):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("폰트 검색기 made by.Hyu-nani")
        self.fontSizeLabel.setText(str(fontSize))
        self.pageLabel.setText(str(page))

        #버튼
        self.nextBtn.clicked.connect(self.pageNext)
        self.prevBtn.clicked.connect(self.pagePrev)
        self.indicateBtn.clicked.connect(self.indicate)
        self.sizeupBtn.clicked.connect(self.fontSizeUp)
        self.sizedownBtn.clicked.connect(self.fontSizeDown)
        
    def pageNext(self):
        global page
        page = page + 1
        self.pageLabel.setText(str(page))
        self.indicate()

    def pagePrev(self):
        global page
        if page > 1:
            page = page - 1
        self.pageLabel.setText(str(page))
        self.indicate()

    def fontSizeUp(self):
        global fontSize
        fontSize = fontSize + 1
        self.fontSizeLabel.setText(str(fontSize))
        self.indicate()

    def fontSizeDown(self):
        global fontSize
        fontSize = fontSize - 1
        self.fontSizeLabel.setText(str(fontSize))
        self.indicate()

    def indicate(self):
        # 글자 가져오기
        text = self.textEdit.toPlainText()
        # 폰트 폴어 안에 내용 이름 가져오기
       
        #for i in range(len(fontList)):    
        #    print('./fonts/' + fontList[i])
        id = QFontDatabase.addApplicationFont('./arialbi.ttf')

        font = QFont('./arialbi.ttf', fontSize)
        
        #self.pushButton = QFont('./arialbi.ttf', fontSize)
        self.labelBtn1_1.setText(text)
        self.labelBtn2_1.setText(text)
        self.labelBtn3_1.setText(text)

        self.labelBtn1_1.setFont(QFont('./arialbi.ttf', fontSize))
        self.labelBtn2_1.setFont(QFont("Helvetica", fontSize))
        self.labelBtn3_1.setFont(QFont("Helvetica", fontSize)) 
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


