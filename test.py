from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import time
import sys
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).resolve().parent

page = 1
fontSize = 11


def load_fonts_from_dir(directory):
    families = set()
    familiesList = []
    for fi in QDir(directory).entryInfoList(["*.ttf"]):
        _id = QFontDatabase.addApplicationFont(fi.absoluteFilePath())
        data = set(QFontDatabase.applicationFontFamilies(_id))
        families |= data
        familiesList.append(str(data).replace("{'",'').replace("'}",''))
    return familiesList



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 973)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.indicateBtn = QPushButton(self.centralwidget)
        self.indicateBtn.setGeometry(QRect(10, 10, 84, 51))
        self.indicateBtn.setObjectName("indicateBtn")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(100, 10, 561, 51))
        self.textEdit.setObjectName("textEdit")
        self.sizeupBtn = QPushButton(self.centralwidget)
        self.sizeupBtn.setGeometry(QRect(670, 10, 41, 25))
        self.sizeupBtn.setObjectName("sizeupBtn")
        self.sizedownBtn = QPushButton(self.centralwidget)
        self.sizedownBtn.setGeometry(QRect(670, 40, 41, 25))
        self.sizedownBtn.setObjectName("sizedownBtn")
        self.fontSizeLabel = QLabel(self.centralwidget)
        self.fontSizeLabel.setGeometry(QRect(720, 10, 61, 51))
        self.fontSizeLabel.setFrameShape(QFrame.WinPanel)
        self.fontSizeLabel.setAlignment(Qt.AlignCenter)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.labelBtn3_9 = QPushButton(self.centralwidget)
        self.labelBtn3_9.setGeometry(QRect(730, 550, 341, 71))
        self.labelBtn3_9.setText("")
        self.labelBtn3_9.setObjectName("labelBtn3_9")
        self.labelBtn3_5 = QPushButton(self.centralwidget)
        self.labelBtn3_5.setGeometry(QRect(730, 230, 341, 71))
        self.labelBtn3_5.setText("")
        self.labelBtn3_5.setObjectName("labelBtn3_5")
        self.labelBtn2_9 = QPushButton(self.centralwidget)
        self.labelBtn2_9.setGeometry(QRect(370, 550, 341, 71))
        self.labelBtn2_9.setText("")
        self.labelBtn2_9.setObjectName("labelBtn2_9")
        self.labelBtn1_2 = QPushButton(self.centralwidget)
        self.labelBtn1_2.setGeometry(QRect(10, 150, 341, 71))
        self.labelBtn1_2.setText("")
        self.labelBtn1_2.setObjectName("labelBtn1_2")
        self.labelBtn1_8 = QPushButton(self.centralwidget)
        self.labelBtn1_8.setGeometry(QRect(10, 470, 341, 71))
        self.labelBtn1_8.setText("")
        self.labelBtn1_8.setObjectName("labelBtn1_8")
        self.labelBtn2_6 = QPushButton(self.centralwidget)
        self.labelBtn2_6.setGeometry(QRect(370, 310, 341, 71))
        self.labelBtn2_6.setText("")
        self.labelBtn2_6.setObjectName("labelBtn2_6")
        self.labelBtn3_2 = QPushButton(self.centralwidget)
        self.labelBtn3_2.setGeometry(QRect(730, 150, 341, 71))
        self.labelBtn3_2.setText("")
        self.labelBtn3_2.setObjectName("labelBtn3_2")
        self.labelBtn3_7 = QPushButton(self.centralwidget)
        self.labelBtn3_7.setGeometry(QRect(730, 390, 341, 71))
        self.labelBtn3_7.setText("")
        self.labelBtn3_7.setObjectName("labelBtn3_7")
        self.labelBtn1_6 = QPushButton(self.centralwidget)
        self.labelBtn1_6.setGeometry(QRect(10, 310, 341, 71))
        self.labelBtn1_6.setText("")
        self.labelBtn1_6.setObjectName("labelBtn1_6")
        self.labelBtn2_8 = QPushButton(self.centralwidget)
        self.labelBtn2_8.setGeometry(QRect(370, 470, 341, 71))
        self.labelBtn2_8.setText("")
        self.labelBtn2_8.setObjectName("labelBtn2_8")
        self.labelBtn2_2 = QPushButton(self.centralwidget)
        self.labelBtn2_2.setGeometry(QRect(370, 150, 341, 71))
        self.labelBtn2_2.setText("")
        self.labelBtn2_2.setObjectName("labelBtn2_2")
        self.labelBtn3_6 = QPushButton(self.centralwidget)
        self.labelBtn3_6.setGeometry(QRect(730, 310, 341, 71))
        self.labelBtn3_6.setText("")
        self.labelBtn3_6.setObjectName("labelBtn3_6")
        self.labelBtn1_9 = QPushButton(self.centralwidget)
        self.labelBtn1_9.setGeometry(QRect(10, 550, 341, 71))
        self.labelBtn1_9.setText("")
        self.labelBtn1_9.setObjectName("labelBtn1_9")
        self.labelBtn2_1 = QPushButton(self.centralwidget)
        self.labelBtn2_1.setGeometry(QRect(370, 70, 341, 71))
        self.labelBtn2_1.setText("")
        self.labelBtn2_1.setFont(QFont("Helvetica", fontSize))
        self.labelBtn2_1.setObjectName("labelBtn2_1")
        self.labelBtn3_8 = QPushButton(self.centralwidget)
        self.labelBtn3_8.setGeometry(QRect(730, 470, 341, 71))
        self.labelBtn3_8.setText("")
        self.labelBtn3_8.setObjectName("labelBtn3_8")
        self.labelBtn1_1 = QPushButton(self.centralwidget)
        self.labelBtn1_1.setGeometry(QRect(10, 70, 341, 71))
        self.labelBtn1_1.setText("")
        self.labelBtn1_1.setObjectName("labelBtn1_1")
        self.labelBtn1_5 = QPushButton(self.centralwidget)
        self.labelBtn1_5.setGeometry(QRect(10, 230, 341, 71))
        self.labelBtn1_5.setText("")
        self.labelBtn1_5.setObjectName("labelBtn1_5")
        self.labelBtn2_7 = QPushButton(self.centralwidget)
        self.labelBtn2_7.setGeometry(QRect(370, 390, 341, 71))
        self.labelBtn2_7.setText("")
        self.labelBtn2_7.setObjectName("labelBtn2_7")
        self.labelBtn3_1 = QPushButton(self.centralwidget)
        self.labelBtn3_1.setGeometry(QRect(730, 70, 341, 71))
        self.labelBtn3_1.setText("")
        self.labelBtn3_1.setObjectName("labelBtn3_1")
        self.labelBtn1_7 = QPushButton(self.centralwidget)
        self.labelBtn1_7.setGeometry(QRect(10, 390, 341, 71))
        self.labelBtn1_7.setText("")
        self.labelBtn1_7.setObjectName("labelBtn1_7")
        self.labelBtn2_5 = QPushButton(self.centralwidget)
        self.labelBtn2_5.setGeometry(QRect(370, 230, 341, 71))
        self.labelBtn2_5.setText("")
        self.labelBtn2_5.setObjectName("labelBtn2_5")
        self.labelBtn1_10 = QPushButton(self.centralwidget)
        self.labelBtn1_10.setGeometry(QRect(10, 630, 341, 71))
        self.labelBtn1_10.setText("")
        self.labelBtn1_10.setObjectName("labelBtn1_10")
        self.labelBtn1_11 = QPushButton(self.centralwidget)
        self.labelBtn1_11.setGeometry(QRect(10, 710, 341, 71))
        self.labelBtn1_11.setText("")
        self.labelBtn1_11.setObjectName("labelBtn1_11")
        self.labelBtn1_12 = QPushButton(self.centralwidget)
        self.labelBtn1_12.setGeometry(QRect(10, 790, 341, 71))
        self.labelBtn1_12.setText("")
        self.labelBtn1_12.setObjectName("labelBtn1_12")
        self.labelBtn1_13 = QPushButton(self.centralwidget)
        self.labelBtn1_13.setGeometry(QRect(10, 870, 341, 71))
        self.labelBtn1_13.setText("")
        self.labelBtn1_13.setObjectName("labelBtn1_13")
        self.labelBtn2_10 = QPushButton(self.centralwidget)
        self.labelBtn2_10.setGeometry(QRect(370, 630, 341, 71))
        self.labelBtn2_10.setText("")
        self.labelBtn2_10.setObjectName("labelBtn2_10")
        self.labelBtn2_11 = QPushButton(self.centralwidget)
        self.labelBtn2_11.setGeometry(QRect(370, 710, 341, 71))
        self.labelBtn2_11.setText("")
        self.labelBtn2_11.setObjectName("labelBtn2_11")
        self.labelBtn2_12 = QPushButton(self.centralwidget)
        self.labelBtn2_12.setGeometry(QRect(370, 790, 341, 71))
        self.labelBtn2_12.setText("")
        self.labelBtn2_12.setObjectName("labelBtn2_12")
        self.labelBtn2_13 = QPushButton(self.centralwidget)
        self.labelBtn2_13.setGeometry(QRect(370, 870, 341, 71))
        self.labelBtn2_13.setText("")
        self.labelBtn2_13.setObjectName("labelBtn2_13")
        self.labelBtn3_10 = QPushButton(self.centralwidget)
        self.labelBtn3_10.setGeometry(QRect(730, 630, 341, 71))
        self.labelBtn3_10.setText("")
        self.labelBtn3_10.setObjectName("labelBtn3_10")
        self.labelBtn3_11 = QPushButton(self.centralwidget)
        self.labelBtn3_11.setGeometry(QRect(730, 710, 341, 71))
        self.labelBtn3_11.setText("")
        self.labelBtn3_11.setObjectName("labelBtn3_11")
        self.labelBtn3_12 = QPushButton(self.centralwidget)
        self.labelBtn3_12.setGeometry(QRect(730, 790, 341, 71))
        self.labelBtn3_12.setText("")
        self.labelBtn3_12.setObjectName("labelBtn3_12")
        self.labelBtn3_13 = QPushButton(self.centralwidget)
        self.labelBtn3_13.setGeometry(QRect(730, 870, 341, 71))
        self.labelBtn3_13.setText("")
        self.labelBtn3_13.setObjectName("labelBtn3_13")
        self.prevBtn = QPushButton(self.centralwidget)
        self.prevBtn.setGeometry(QRect(790, 10, 121, 51))
        self.prevBtn.setObjectName("prevBtn")
        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QRect(950, 10, 121, 51))
        self.nextBtn.setObjectName("nextBtn")
        self.pageLabel = QLabel(self.centralwidget)
        self.pageLabel.setGeometry(QRect(910, 10, 41, 51))
        self.pageLabel.setAlignment(Qt.AlignCenter)
        self.pageLabel.setObjectName("pageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        font_dir = CURRENT_DIRECTORY / "fonts"
        families = load_fonts_from_dir(os.fspath(font_dir))

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        #버튼 작동
        self.sizeupBtn.clicked.connect(self.fontSizeUp)
        self.sizedownBtn.clicked.connect(self.fontSizeDown)
        self.nextBtn.clicked.connect(self.pageNext)
        self.prevBtn.clicked.connect(self.pagePrev)
        self.indicateBtn.clicked.connect(self.indicate)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "폰트 검색기 made by.Hyu-nani"))
        self.indicateBtn.setText(_translate("MainWindow", "변환"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Test테스트123</span></p></body></html>"))
        self.sizeupBtn.setText(_translate("MainWindow", "+"))
        self.sizedownBtn.setText(_translate("MainWindow", "-"))
        self.fontSizeLabel.setText(_translate("MainWindow", "Size"))
        self.prevBtn.setText(_translate("MainWindow", "이전"))
        self.nextBtn.setText(_translate("MainWindow", "다음"))
        self.pageLabel.setText(_translate("MainWindow", "Page"))

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
        font_dir = CURRENT_DIRECTORY / "fonts"
        families = load_fonts_from_dir(os.fspath(font_dir))
        print(len(families))
        db = QFontDatabase()
        styles = db.styles(families[2])
        print(styles)
        font = db.font(families[2], "Medium Italic", fontSize)
        
        #self.pushButton = QFont('./arialbi.ttf', fontSize)
        self.labelBtn1_1.setFont(db.font(families[1+page*3], "Medium Italic", fontSize))
        self.labelBtn2_1.setFont(db.font(families[2+page*3], "Medium Italic", fontSize))
        self.labelBtn3_1.setFont(db.font(families[3+page*3], "Medium Italic", fontSize)) 
        self.labelBtn1_1.setText(text)
        self.labelBtn2_1.setText(text)
        self.labelBtn3_1.setText(text)
        self.labelBtn3_1.show()
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

