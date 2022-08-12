import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time
from PySide2.QtUiTools import loadUiType
import os
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

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "폰트 검색기 made by.Hyu-nani V1.5"
        self.top = 200
        self.left = 500
        self.width = 1000
        self.height = 800
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        db = QFontDatabase()
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.indicateBtn = QPushButton(self.centralwidget)
        self.indicateBtn.setText("변환")
        self.indicateBtn.setGeometry(QRect(10, 10, 30, 30))
        self.indicateBtn.setObjectName("indicateBtn")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(100, 10, 561, 51))
        self.textEdit.setObjectName("textEdit")
        self.sizeupBtn = QPushButton(self.centralwidget)
        self.sizeupBtn.setGeometry(QRect(670, 10, 41, 25))
        self.sizeupBtn.setObjectName("sizeupBtn")
        self.sizeupBtn.setText("+")
        self.sizeupBtn.setFont(db.font("Helvetica", "Medium Italic", 20))
        self.sizedownBtn = QPushButton(self.centralwidget)
        self.sizedownBtn.setGeometry(QRect(670, 40, 41, 25))
        self.sizedownBtn.setObjectName("sizedownBtn")
        self.sizedownBtn.setText("-")
        self.sizedownBtn.setFont(db.font("Helvetica", "Medium Italic", 20))
        self.fontSizeLabel = QLabel(self.centralwidget)
        self.fontSizeLabel.setGeometry(QRect(720, 10, 61, 51))
        self.fontSizeLabel.setFrameShape(QFrame.WinPanel)
        self.fontSizeLabel.setAlignment(Qt.AlignCenter)
        self.fontSizeLabel.setObjectName("fontSizeLabel")

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

        labelLis = []
        FontListLine1 = []
        FontListLine2 = []
        FontListLine3 = []

        # 폰트 폴어 안에 내용 이름 가져오기
        font_dir = CURRENT_DIRECTORY / "fonts"
        families = load_fonts_from_dir(os.fspath(font_dir))
        db = QFontDatabase()
        #styles = db.styles(families[2])

        for i in  range(len(families)-300):
            labelLis.append(QLabel("Label"))
            FontListLine1.append(QPushButton("Click Me"))
            FontListLine1[i].setFont(db.font(families[1+i*3], "Medium Italic", fontSize))
            FontListLine2.append(QPushButton("Click Me"))
            FontListLine2[i].setFont(db.font(families[2+i*3], "Medium Italic", fontSize))
            FontListLine3.append(QPushButton("Click Me"))
            FontListLine3[i].setFont(db.font(families[3+i*3], "Medium Italic", fontSize))
            #data = formLayout.addRow(comboList2[i],comboList3[i])
            layout_lower.addWidget(FontListLine1[i], i, 0)
            layout_lower.addWidget(FontListLine2[i], i, 1)
            layout_lower.addWidget(FontListLine3[i], i, 2)

        groupBox.setLayout(layout_lower)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addLayout(layout_upper)
        layout.addWidget(scroll)
        self.show()

        #버튼 작동
        self.sizeupBtn.clicked.connect(self.fontSizeUp)
        self.sizedownBtn.clicked.connect(self.fontSizeDown)

    def pageNext(self):
        global page
        page = page + 1
        self.pageLabel.setText(str(page))

    def pagePrev(self):
        global page
        if page > 1:
            page = page - 1
        self.pageLabel.setText(str(page))

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
