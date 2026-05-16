# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loader.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(200, 480, 431, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(350, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelSubTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelSubTitle.setGeometry(QtCore.QRect(310, 60, 191, 20))
        self.labelSubTitle.setObjectName("labelSubTitle")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(160, 120, 481, 251))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("labelImage")
        self.labelCurrentStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelCurrentStatus.setGeometry(QtCore.QRect(390, 510, 231, 20))
        self.labelCurrentStatus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelCurrentStatus.setText("")
        self.labelCurrentStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCurrentStatus.setObjectName("labelCurrentStatus")
        self.pBContinue = QtWidgets.QPushButton(self.centralwidget)
        self.pBContinue.setGeometry(QtCore.QRect(330, 400, 141, 31))
        self.pBContinue.setObjectName("pBContinue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "CricAI"))
        self.labelSubTitle.setText(_translate("MainWindow", "Smart Outcome Prediction for Cricket"))
        self.labelImage.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/projectImages/images/stadium.jpg\"/></p></body></html>"))
        self.pBContinue.setText(_translate("MainWindow", "Continue"))

import CricAI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

