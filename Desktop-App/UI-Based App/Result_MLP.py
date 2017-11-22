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
        self.labelTitle.setGeometry(QtCore.QRect(210, 40, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelT1Name = QtWidgets.QLabel(self.centralwidget)
        self.labelT1Name.setGeometry(QtCore.QRect(180, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelT1Name.setFont(font)
        self.labelT1Name.setObjectName("labelT1Name")
        self.labelT1Percent = QtWidgets.QLabel(self.centralwidget)
        self.labelT1Percent.setGeometry(QtCore.QRect(250, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelT1Percent.setFont(font)
        self.labelT1Percent.setObjectName("labelT1Percent")
        self.labelT2Name = QtWidgets.QLabel(self.centralwidget)
        self.labelT2Name.setGeometry(QtCore.QRect(450, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelT2Name.setFont(font)
        self.labelT2Name.setObjectName("labelT2Name")
        self.labelT2Percent = QtWidgets.QLabel(self.centralwidget)
        self.labelT2Percent.setGeometry(QtCore.QRect(550, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelT2Percent.setFont(font)
        self.labelT2Percent.setObjectName("labelT2Percent")
        self.labelT1Verdict = QtWidgets.QLabel(self.centralwidget)
        self.labelT1Verdict.setGeometry(QtCore.QRect(210, 230, 51, 41))
        self.labelT1Verdict.setObjectName("labelT1Verdict")
        self.labelT2Verdict = QtWidgets.QLabel(self.centralwidget)
        self.labelT2Verdict.setGeometry(QtCore.QRect(510, 230, 41, 41))
        self.labelT2Verdict.setObjectName("labelT2Verdict")
        self.teAccuracyMLP = QtWidgets.QTextEdit(self.centralwidget)
        self.teAccuracyMLP.setGeometry(QtCore.QRect(170, 440, 451, 78))
        self.teAccuracyMLP.setObjectName("teAccuracyMLP")
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
        self.labelT1Name.setText(_translate("MainWindow", "India"))
        self.labelT1Percent.setText(_translate("MainWindow", "60 %"))
        self.labelT2Name.setText(_translate("MainWindow", "Pakistan"))
        self.labelT2Percent.setText(_translate("MainWindow", "40 %"))
        self.labelT1Verdict.setText(_translate("MainWindow", "WINNER"))
        self.labelT2Verdict.setText(_translate("MainWindow", "LOSER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

