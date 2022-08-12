import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time
from PySide2.QtUiTools import loadUiType
import os
from pathlib import Path
import clipboard

CURRENT_DIRECTORY = Path(__file__).resolve().parent

text = 'ABCabc123가나다'
fontSize = 11
choise = 0
FontListLine = []

familiesList = []

def load_fonts_from_dir(directory):
    global familiesList
    families = set()
    familiesList = []
    for fi in QDir(directory).entryInfoList(["*.ttf"]):
        _id = QFontDatabase.addApplicationFont(fi.absoluteFilePath())
        data = set(QFontDatabase.applicationFontFamilies(_id))
        families |= data
        familiesList.append(str(data).replace("{'",'').replace("'}",''))
    return familiesList


class Window(QWidget):

    def __init__(self):
        global FontListLine
        global choise
        super().__init__()
        self.title = "폰트 검색기 made by.Hyu-nani V1.5"
        self.top = 200
        self.left = 500
        self.width = 1000
        self.height = 800
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 폰트 폴어 안에 내용 이름 가져오기
        font_dir = CURRENT_DIRECTORY / "fonts"
        families = load_fonts_from_dir(os.fspath(font_dir))
        db = QFontDatabase()

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.indicateBtn = QPushButton(self.centralwidget)
        self.indicateBtn.setText("변환")
        self.indicateBtn.setMaximumWidth(100)
        self.indicateBtn.setMaximumHeight(100)
        self.indicateBtn.setObjectName("indicateBtn")

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">ABCabc123가나다</span></p></body></html>"))
        self.textEdit.setMaximumWidth(1000)
        self.textEdit.setMaximumHeight(100)

        self.sizeupBtn = QPushButton(self.centralwidget)
        self.sizeupBtn.setObjectName("sizeupBtn")
        self.sizeupBtn.setText("+")
        self.sizeupBtn.setFont(db.font("Normal", "Medium Italic", 20))
        self.sizeupBtn.setMaximumWidth(100)

        self.sizedownBtn = QPushButton(self.centralwidget)
        self.sizedownBtn.setObjectName("sizedownBtn")
        self.sizedownBtn.setText("-")
        self.sizedownBtn.setFont(db.font("Normal", "Medium Italic", 20))
        self.sizedownBtn.setMaximumWidth(100)

        self.fontSizeLabel = QLabel(self.centralwidget)
        self.fontSizeLabel.setFrameShape(QFrame.WinPanel)
        self.fontSizeLabel.setAlignment(Qt.AlignCenter)
        self.fontSizeLabel.setText(str(fontSize))
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.fontSizeLabel.setMaximumHeight(100)
        self.fontSizeLabel.setFixedWidth(100)
        self.fontSizeLabel.setMinimumHeight

        layout_size = QVBoxLayout()
        layout_size.addWidget(self.sizeupBtn)
        layout_size.addWidget(self.sizedownBtn)
        layout_upper = QHBoxLayout()
        layout_upper.addWidget(self.indicateBtn)
        layout_upper.addWidget(self.textEdit)
        layout_upper.addLayout(layout_size)
        layout_upper.addWidget(self.fontSizeLabel)

        layout_lower = QGridLayout()
        groupBox = QGroupBox("This Is Font Box")

        RowNum = 4
        for i in  range(len(families)):
            FontListLine.append(QPushButton(text))
            FontListLine[i].setFont(db.font(families[i], "Medium Italic", fontSize))
            FontListLine[i].setMaximumHeight(100)
            layout_lower.addWidget(FontListLine[i], i // RowNum, i % RowNum)
    
        groupBox.setLayout(layout_lower)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addLayout(layout_upper)
        layout.addWidget(scroll)
        self.show()

        #버튼 작동
        for i , name in enumerate(familiesList):
            FontListLine[i].clicked.connect(lambda stat=False, idx=i: self.copy(stat, idx))
        self.sizeupBtn.clicked.connect(self.fontSizeUp)
        self.sizedownBtn.clicked.connect(self.fontSizeDown)
        self.indicateBtn.clicked.connect(self.indicate)

    def copy(self, stat, choice):
        num = int(choice)
        print(num)
        name = familiesList[num]
        print(name)
        clipboard.copy(name)
        QMessageBox.question(self, '알림', '이름이 복사되었습니다.', QMessageBox.Yes)


    def indicate(self):
         # 글자 가져오기
        text = self.textEdit.toPlainText()
        # 폰트 폴어 안에 내용 이름 가져오기
        font_dir = CURRENT_DIRECTORY / "fonts"
        families = load_fonts_from_dir(os.fspath(font_dir))
        db = QFontDatabase()
        for i in  range(len(families)):
            FontListLine[i].setText(text)
            FontListLine[i].setFont(db.font(families[i], "Medium Italic", fontSize))
        
    def fontSizeUp(self):
        global fontSize
        fontSize = fontSize + 1
        self.fontSizeLabel.setText(str(fontSize))

    def fontSizeDown(self):
        global fontSize
        fontSize = fontSize - 1
        self.fontSizeLabel.setText(str(fontSize))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    MainWindow = QMainWindow()
    window = Window()
    sys.exit(App.exec())
