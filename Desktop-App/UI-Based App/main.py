import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import CricAI_Basic,Loader,Result_MLP
from PyQt5 import QtGui
from Classifier import ourMLPClassifier,ourDTClassifier
import dataInputFormat

MLPClf = ourMLPClassifier()
DTClf = ourDTClassifier()
dIF = dataInputFormat.DataInput()

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		
		self.uiLoader = Loader.Ui_MainWindow()
		self.uiLoader.setupUi(self)
		self.uiLoader.progressBar.setValue(0)
		self.uiLoader.pBContinue.clicked.connect(self.startUILoader);
#		self.startProgressBar()
#		self.uiWindow = CricAI_Basic.Ui_MainWindow()
#		self.uiMLPResult = Result_MLP.Ui_MainWindow()


	def startUILoader(self):
#		self.uiLoader.setupUi(self)
#		self.uiLoader.progressBar.setValue(0)

		MLPClf.trainModel()
		DTClf.trainModel()
		dIF.hashAll()
		self.startProgressBar()
		

	def startProgressBar(self):
#		self.uiLoader.labelCurrentStatus.setText("Loading . . .")

		self.completed = 0
		while self.completed < 100:
			self.completed += 0.0001
			self.uiLoader.progressBar.setValue(self.completed)
#			if self.completed > 95:
#				self.uiLoader.labelCurrentStatus.setText("Finalising Stuffs . . .")
#			elif self.completed > 90:
#				self.uiLoader.labelCurrentStatus.setText("Generating Hashes . . .")
#			elif self.completed > 80:
#				self.uiLoader.labelCurrentStatus.setText("Training DT Classifier. . .")
#			elif self.completed > 70:
#				self.uiLoader.labelCurrentStatus.setText("Initialising DT Classifier . . .")
#			elif self.completed > 50:
#				self.uiLoader.labelCurrentStatus.setText("Training MLP Classifier . . .")
#			elif self.completed > 20:
#				self.uiLoader.labelCurrentStatus.setText("Initialising MLP Classifier . . .")
#			elif self.completed > 10:
#				self.uiLoader.labelCurrentStatus.setText("Waking Up Kernels . . .")
#			elif self.completed > 2:
#				self.uiLoader.labelCurrentStatus.setText("Reading Dataset Files . . .")

		#if self.completed >= 100:
		#	self.startUIWindow()

		

	def startUIWindow(self):
		self.uiWindow.setupUi(self)
		self.uiWindow.buttonRunMLP.clicked.connect(self.runCLFClassifier)
		#self.ui.buttonRunDT.clicked.connect(self.runDTClassifier)
		#self.show()

	def startUIMLPResult(self):
		self.uiMLPResult.setupUi(self)
		#self.show()

	def grabAndSetInput(self):
		self.t1 = self.ui.teTeam1.getText()
		self.t2 = self.ui.teTeam2.getText()

#		ground = self.ui.teGround.getText()
#		innings = self.ui.dbInnings.getSelected()
#		venue = self.ui.dbVenue.getSelected()
#
#		if innings == rbTeam1_Innings:
#			inningsTeam1 = "Team1_1Inning"
#			inningsTeam2 = "Team2_2Inning"
#		elif innings == rbTeam2_Innings:
#			inningsTeam1 = "Team1_2Inning"
#			inningsTeam2 = "Team2_1Inning"
#
#		if venue == rbTeam1_Home:
#			venueTeam1 = "Team1_Home"
#			venueTeam2 = "Team2_Away"
#		elif venue == rbTeam2_Home:
#			venueTeam1 = "Team1_Away"
#			venueTeam2 = "Team2_Home"
#		elif venue == rb_Neutral:
#			venueTeam1 = "Team1_Neutral"
#			venueTeam2 = "Team2_Neutral"
#
#		self.inputPrediction = [0]*217
#
#		self.inputPrediction[dIF.ourTeams_1[self.t1]] = 1
#		self.inputPrediction[dIF.ourTeams_2[self.t2]] = 1
#		self.inputPrediction[dIF.ourGrounds[ground]] = 1
#		self.inputPrediction[dIF.ourInnings[inningsTeam1]] = 1
#		self.inputPrediction[dIF.ourInnings[inningsTeam2]] = 1
#		self.inputPrediction[dIF.ourVenues[venueTeam1]] = 1
#		self.inputPrediction[dIF.ourVenues[venueTeam2]] = 1


	def runCLFClassifier(self):
		grabAndSetInput()
		MLPClf.runModel(self.inputPrediction,self.t1,self.t2)

	#def runDTClassifier(self):
		#grabAndSetInput()
		#DTClf.runModel(self.inputPrediction,self.t1,self.t2)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())