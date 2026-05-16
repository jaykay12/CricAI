# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result_DT.ui'
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
        self.labelTitle.setGeometry(QtCore.QRect(160, 30, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelWinner = QtWidgets.QLabel(self.centralwidget)
        self.labelWinner.setGeometry(QtCore.QRect(150, 330, 481, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelWinner.setFont(font)
        self.labelWinner.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWinner.setObjectName("labelWinner")
        self.labelTrophy = QtWidgets.QLabel(self.centralwidget)
        self.labelTrophy.setGeometry(QtCore.QRect(140, 90, 501, 221))
        self.labelTrophy.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTrophy.setObjectName("labelTrophy")
        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(350, 480, 85, 27))
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(350, 520, 85, 27))
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
        self.labelTitle.setText(_translate("MainWindow", "Decision Tree Classifier"))
        self.labelWinner.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/flags/images/flags/India.jpg\"/></p></body></html>"))
        self.labelTrophy.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/projectImages/images/winner.jpg\"/></p></body></html>"))
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

