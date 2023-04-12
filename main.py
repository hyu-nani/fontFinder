from sqlite3 import Row
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
from pathlib import Path
import clipboard

CURRENT_DIRECTORY = Path(__file__).resolve().parent

text = 'ABab12가나'
fontSize = 30
choise = 0
FontListLine = []
fileList = os.listdir(str(CURRENT_DIRECTORY)+'/fonts')
familiesList = []
RowNum = 6
def load_fonts_from_dir(directory):
    global familiesList
    print()
    
    families = set()
    fileList_TTF = QDir(directory).entryInfoList(["*.ttf"])
    fileList_TTC = QDir(directory).entryInfoList(["*.ttc"])
    fileList_OTF = QDir(directory).entryInfoList(["*.otf"])
    familiesList = []
    for file in fileList_TTF:
        _id = QFontDatabase.addApplicationFont(file.absoluteFilePath())
        data = set(QFontDatabase.applicationFontFamilies(_id))
        families |= data
        data = str(data)
        familiesList.append(str(data).replace("{'",'').replace("'}",''))
    print()
    for file in fileList_TTC:
        _id = QFontDatabase.addApplicationFont(file.absoluteFilePath())
        data = set(QFontDatabase.applicationFontFamilies(_id))
        families |= data
        data = str(data).replace("{'",'').replace("'}",'').split("', '")
        for i in range(len(data)):
            familiesList.append(str(data[i]))
    print()
    for file in fileList_OTF:
        _id = QFontDatabase.addApplicationFont(file.absoluteFilePath())
        data = set(QFontDatabase.applicationFontFamilies(_id))
        families |= data
        data = str(data)
        familiesList.append(str(data).replace("{'",'').replace("'}",''))
    return familiesList


class Window(QWidget):

    def __init__(self):
        global FontListLine
        global choise
        super().__init__()
        self.title = "폰트 검색기 made by.Hyu-nani V1.6"
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">ABab12가나</span></p></body></html>"))
        self.textEdit.setMaximumWidth(1000)
        self.textEdit.setMaximumHeight(100)

        self.sizeupBtn = QPushButton(self.centralwidget)
        self.sizeupBtn.setObjectName("sizeupBtn")
        self.sizeupBtn.setText("+")
        self.sizeupBtn.setFont(db.font("Normal", "Regular", 20))
        self.sizeupBtn.setMaximumWidth(100)

        self.sizedownBtn = QPushButton(self.centralwidget)
        self.sizedownBtn.setObjectName("sizedownBtn")
        self.sizedownBtn.setText("-")
        self.sizedownBtn.setFont(db.font("Normal", "Regular", 20))
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

        
        for i in  range(len(families)):
            FontListLine.append(QPushButton(text))
            #FontListLine[i].setFont(db.font(familiesList[i], "Regular", fontSize))
            FontListLine[i].setFont(QFont(families[i], fontSize))
            FontListLine[i].setMaximumHeight(150)
            FontListLine[i].setMaximumWidth(600)
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
        #print(num)
        name = familiesList[num]
        #print(name)
        clipboard.copy(name)
        QMessageBox.question(self, '알림', '이름이 복사되었습니다.', QMessageBox.Yes)


    def indicate(self):
        global RowNum
         # 글자 가져오기
        text = self.textEdit.toPlainText()
        if len(text) < 1:
            QMessageBox.question(self, '알림', '한글자 이상 입력해주세요.', QMessageBox.Yes)
            return False
        # 폰트 폴어 안에 내용 이름 가져오기
        font_dir = CURRENT_DIRECTORY / "fonts"
        families = load_fonts_from_dir(os.fspath(font_dir))
        db = QFontDatabase()
        for i in  range(len(families)):
            FontListLine[i].setText(text)
            FontListLine[i].setFont(QFont(families[i], fontSize))
        
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
