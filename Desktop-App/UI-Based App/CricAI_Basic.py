# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CricAI_Basic.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.teTeam1 = QtWidgets.QTextEdit(self.centralwidget)
        self.teTeam1.setGeometry(QtCore.QRect(90, 60, 221, 51))
        self.teTeam1.setObjectName("teTeam1")
        self.teTeam2 = QtWidgets.QTextEdit(self.centralwidget)
        self.teTeam2.setGeometry(QtCore.QRect(440, 60, 221, 51))
        self.teTeam2.setObjectName("teTeam2")
        self.teGround = QtWidgets.QTextEdit(self.centralwidget)
        self.teGround.setGeometry(QtCore.QRect(273, 160, 211, 31))
        self.teGround.setObjectName("teGround")
        self.labelTeam1 = QtWidgets.QLabel(self.centralwidget)
        self.labelTeam1.setGeometry(QtCore.QRect(180, 40, 49, 12))
        self.labelTeam1.setObjectName("labelTeam1")
        self.labelTeam2 = QtWidgets.QLabel(self.centralwidget)
        self.labelTeam2.setGeometry(QtCore.QRect(530, 40, 49, 12))
        self.labelTeam2.setObjectName("labelTeam2")
        self.labelGround = QtWidgets.QLabel(self.centralwidget)
        self.labelGround.setGeometry(QtCore.QRect(360, 140, 49, 12))
        self.labelGround.setObjectName("labelGround")
        self.buttonRunMLP = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRunMLP.setGeometry(QtCore.QRect(310, 400, 151, 41))
        self.buttonRunMLP.setObjectName("buttonRunMLP")
        self.dbInnings = QtWidgets.QGroupBox(self.centralwidget)
        self.dbInnings.setGeometry(QtCore.QRect(230, 220, 311, 80))
        self.dbInnings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dbInnings.setTitle("")
        self.dbInnings.setObjectName("dbInnings")
        self.labelInnings = QtWidgets.QLabel(self.dbInnings)
        self.labelInnings.setGeometry(QtCore.QRect(120, 10, 71, 20))
        self.labelInnings.setObjectName("labelInnings")
        self.rbTeam1_Innings = QtWidgets.QRadioButton(self.dbInnings)
        self.rbTeam1_Innings.setGeometry(QtCore.QRect(30, 40, 92, 21))
        self.rbTeam1_Innings.setObjectName("rbTeam1_Innings")
        self.rbTeam2_Innings = QtWidgets.QRadioButton(self.dbInnings)
        self.rbTeam2_Innings.setGeometry(QtCore.QRect(200, 40, 92, 21))
        self.rbTeam2_Innings.setObjectName("rbTeam2_Innings")
        self.dbVenue = QtWidgets.QGroupBox(self.centralwidget)
        self.dbVenue.setGeometry(QtCore.QRect(220, 290, 331, 80))
        self.dbVenue.setTitle("")
        self.dbVenue.setObjectName("dbVenue")
        self.labelVenue = QtWidgets.QLabel(self.dbVenue)
        self.labelVenue.setGeometry(QtCore.QRect(150, 10, 49, 12))
        self.labelVenue.setObjectName("labelVenue")
        self.rbTeam1_Home = QtWidgets.QRadioButton(self.dbVenue)
        self.rbTeam1_Home.setGeometry(QtCore.QRect(10, 40, 92, 21))
        self.rbTeam1_Home.setObjectName("rbTeam1_Home")
        self.rbTeam2_Home = QtWidgets.QRadioButton(self.dbVenue)
        self.rbTeam2_Home.setGeometry(QtCore.QRect(130, 40, 111, 21))
        self.rbTeam2_Home.setObjectName("rbTeam2_Home")
        self.rb_Neutral = QtWidgets.QRadioButton(self.dbVenue)
        self.rb_Neutral.setGeometry(QtCore.QRect(240, 40, 92, 21))
        self.rb_Neutral.setObjectName("rb_Neutral")
        self.buttonRunDT = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRunDT.setGeometry(QtCore.QRect(310, 460, 151, 41))
        self.buttonRunDT.setObjectName("buttonRunDT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CricAI_Basic"))
        self.labelTeam1.setText(_translate("MainWindow", "Team 1"))
        self.labelTeam2.setText(_translate("MainWindow", "Team 2"))
        self.labelGround.setText(_translate("MainWindow", "Ground"))
        self.buttonRunMLP.setText(_translate("MainWindow", "RUN : MLPClassifier"))
        self.labelInnings.setText(_translate("MainWindow", "First Innings"))
        self.rbTeam1_Innings.setText(_translate("MainWindow", "Team 1"))
        self.rbTeam2_Innings.setText(_translate("MainWindow", "Team 2"))
        self.labelVenue.setText(_translate("MainWindow", "Venue"))
        self.rbTeam1_Home.setText(_translate("MainWindow", "Home: Team 1"))
        self.rbTeam2_Home.setText(_translate("MainWindow", "Home: Team 2"))
        self.rb_Neutral.setText(_translate("MainWindow", "Neutral"))
        self.buttonRunDT.setText(_translate("MainWindow", "RUN : DTClassifier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

