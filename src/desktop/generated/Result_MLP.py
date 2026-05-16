# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result_MLP.ui'
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
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(180, 40, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelT1Name = QtWidgets.QLabel(self.centralwidget)
        self.labelT1Name.setGeometry(QtCore.QRect(130, 170, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelT1Name.setFont(font)
        self.labelT1Name.setAlignment(QtCore.Qt.AlignCenter)
        self.labelT1Name.setObjectName("labelT1Name")
        self.labelT1Percent = QtWidgets.QLabel(self.centralwidget)
        self.labelT1Percent.setGeometry(QtCore.QRect(130, 300, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.labelT1Percent.setFont(font)
        self.labelT1Percent.setAlignment(QtCore.Qt.AlignCenter)
        self.labelT1Percent.setObjectName("labelT1Percent")
        self.labelT2Name = QtWidgets.QLabel(self.centralwidget)
        self.labelT2Name.setGeometry(QtCore.QRect(480, 170, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelT2Name.setFont(font)
        self.labelT2Name.setAlignment(QtCore.Qt.AlignCenter)
        self.labelT2Name.setObjectName("labelT2Name")
        self.labelT2Percent = QtWidgets.QLabel(self.centralwidget)
        self.labelT2Percent.setGeometry(QtCore.QRect(480, 300, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.labelT2Percent.setFont(font)
        self.labelT2Percent.setAlignment(QtCore.Qt.AlignCenter)
        self.labelT2Percent.setObjectName("labelT2Percent")
        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(370, 450, 85, 27))
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(370, 490, 85, 27))
        self.pushButtonExit.setObjectName("pushButtonExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
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
        self.labelTitle.setText(_translate("MainWindow", "Multi Level Perceptron Classifier"))
        self.labelT1Name.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/flags/images/flags/India.jpg\"/></p></body></html>"))
        self.labelT1Percent.setText(_translate("MainWindow", "60 %"))
        self.labelT2Name.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/flags/images/flags/Pakistan.jpg\"/></p></body></html>"))
        self.labelT2Percent.setText(_translate("MainWindow", "40 %"))
        self.pushButtonHome.setText(_translate("MainWindow", "Home"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))

import CricAI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

