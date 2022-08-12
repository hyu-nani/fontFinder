# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cube_\OneDrive\Github\fontFinder\screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 973)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.indicateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.indicateBtn.setGeometry(QtCore.QRect(10, 10, 84, 51))
        self.indicateBtn.setObjectName("indicateBtn")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 10, 561, 51))
        self.textEdit.setObjectName("textEdit")
        self.sizeupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sizeupBtn.setGeometry(QtCore.QRect(670, 10, 41, 25))
        self.sizeupBtn.setObjectName("sizeupBtn")
        self.sizedownBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sizedownBtn.setGeometry(QtCore.QRect(670, 40, 41, 25))
        self.sizedownBtn.setObjectName("sizedownBtn")
        self.fontSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.fontSizeLabel.setGeometry(QtCore.QRect(720, 10, 61, 51))
        self.fontSizeLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.fontSizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.prevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.prevBtn.setGeometry(QtCore.QRect(790, 10, 121, 51))
        self.prevBtn.setObjectName("prevBtn")
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(950, 10, 121, 51))
        self.nextBtn.setObjectName("nextBtn")
        self.pageLabel = QtWidgets.QLabel(self.centralwidget)
        self.pageLabel.setGeometry(QtCore.QRect(910, 10, 41, 51))
        self.pageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pageLabel.setObjectName("pageLabel")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 1061, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1059, 869))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.labelBtn3_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.labelBtn3_1.setGeometry(QtCore.QRect(720, 0, 341, 71))
        self.labelBtn3_1.setText("")
        self.labelBtn3_1.setObjectName("labelBtn3_1")
        self.labelBtn1_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.labelBtn1_1.setGeometry(QtCore.QRect(0, 0, 341, 71))
        self.labelBtn1_1.setText("")
        self.labelBtn1_1.setObjectName("labelBtn1_1")
        self.labelBtn2_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.labelBtn2_1.setGeometry(QtCore.QRect(360, 0, 341, 71))
        self.labelBtn2_1.setText("")
        self.labelBtn2_1.setObjectName("labelBtn2_1")
        self.labelBtn3_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.labelBtn3_5.setGeometry(QtCore.QRect(720, 1000, 341, 71))
        self.labelBtn3_5.setText("")
        self.labelBtn3_5.setObjectName("labelBtn3_1")
        self.labelBtn1_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.labelBtn1_5.setGeometry(QtCore.QRect(0, 1000, 341, 71))
        self.labelBtn1_5.setText("")
        self.labelBtn1_5.setObjectName("labelBtn1_1")
        self.labelBtn2_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.labelBtn2_5.setGeometry(QtCore.QRect(360, 1000, 341, 71))
        self.labelBtn2_5.setText("")
        self.labelBtn2_5.setObjectName("labelBtn2_1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

