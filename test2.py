from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys
class Window(QWidget):
    def __init__(self, val):
        super().__init__()
        self.title = "PyQt5 Scroll Bar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout =QFormLayout()
        groupBox = QGroupBox("This Is Group Box")
        labelLis = []
        comboList1 = []
        comboList2 = []
        comboList3 = []
        for i in  range(val):
            labelLis.append(QLabel("Label"))
            comboList1.append(QPushButton("Click Me"))
            comboList1[i].setFont(QtGui.QFont("Helvetica", 24))
            comboList2.append(QPushButton("Click Me"))
            comboList3.append(QPushButton("Click Me"))
            data = formLayout.addRow(comboList2[i],comboList3[i])
            formLayout.addRow( comboList1[i], data)
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        #scroll.setFixedHeight(800)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()
App = QApplication(sys.argv)
window = Window(30)
sys.exit(App.exec())