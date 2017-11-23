import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import CricAI_Basic,Loader,Result_MLP,Result_DT
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
		self.uiWindow = CricAI_Basic.Ui_MainWindow()
		self.uiMLPResult = Result_MLP.Ui_MainWindow()
		self.uiDTResult = Result_DT.Ui_MainWindow()

		self.uiLoader.setupUi(self)
		self.uiLoader.progressBar.setValue(0)
		self.uiLoader.pBContinue.clicked.connect(self.startUILoader);


	def startUILoader(self):
		MLPClf.loadPickle()
		DTClf.loadPickle()
		dIF.hashAll()
		self.startProgressBar()
		

	def startProgressBar(self):
		self.uiLoader.labelCurrentStatus.setText("Loading . . .")

		self.completed = 0
		while self.completed < 100:
			self.completed += 0.00008
			self.uiLoader.progressBar.setValue(self.completed)
			if self.completed > 95:
				self.uiLoader.labelCurrentStatus.setText("Finalising Stuffs . . .")
			elif self.completed > 90:
				self.uiLoader.labelCurrentStatus.setText("Generating Hashes . . .")
			elif self.completed > 80:
				self.uiLoader.labelCurrentStatus.setText("Training DT Classifier. . .")
			elif self.completed > 70:
				self.uiLoader.labelCurrentStatus.setText("Initialising DT Classifier . . .")
			elif self.completed > 50:
				self.uiLoader.labelCurrentStatus.setText("Training MLP Classifier . . .")
			elif self.completed > 20:
				self.uiLoader.labelCurrentStatus.setText("Initialising MLP Classifier . . .")
			elif self.completed > 10:
				self.uiLoader.labelCurrentStatus.setText("Waking Up Kernels . . .")
			elif self.completed > 2:
				self.uiLoader.labelCurrentStatus.setText("Reading Dataset Files . . .")

		if self.completed >= 100:
			self.startUIWindow()

		

	def startUIWindow(self):
		self.uiWindow.setupUi(self)
		self.uiWindow.buttonRunMLP.clicked.connect(self.runCLFClassifier)
		self.uiWindow.buttonRunDT.clicked.connect(self.runDTClassifier)
		
		self.uiWindow.comboBoxTeam1.clear()
		self.uiWindow.comboBoxTeam2.clear()
		self.uiWindow.comboBoxGround.clear()

		self.uiWindow.comboBoxTeam1.addItems(dIF.teamNames)
		self.uiWindow.comboBoxTeam2.addItems(dIF.teamNames)
		self.uiWindow.comboBoxGround.addItems(dIF.groundNames)

		self.uiWindow.comboBoxTeam1.setCurrentText("India")
		self.uiWindow.comboBoxTeam2.setCurrentText("Australia")
		self.uiWindow.comboBoxGround.setCurrentText("Mumbai")

		self.uiWindow.comboBoxTeam1.currentTextChanged.connect(lambda: self.updateFlagTeams(self.uiWindow.labelFlagT1,self.uiWindow.comboBoxTeam1.currentText()))
		self.uiWindow.comboBoxTeam2.currentTextChanged.connect(lambda: self.updateFlagTeams(self.uiWindow.labelFlagT2,self.uiWindow.comboBoxTeam2.currentText()))


		self.uiWindow.rbTeam1_Innings.setChecked(True)
		self.uiWindow.rbTeam1_Home.setChecked(True)

	def startUIMLPResult(self):
		self.uiMLPResult.setupUi(self)
		self.uiMLPResult.labelT1Name.setText(self.t1)
		self.uiMLPResult.labelT2Name.setText(self.t2)
		str1 = str(MLPClf.predictionT1)+"%"
		str2 = str(MLPClf.predictionT2)+"%"
		self.uiMLPResult.labelT1Percent.setText(str1)
		self.uiMLPResult.labelT2Percent.setText(str2)

		if MLPClf.predictionT1 > MLPClf.predictionT2:
			self.uiMLPResult.labelT1Verdict.setText("Winner")
			self.uiMLPResult.labelT2Verdict.setText("Loser")
		else:
			self.uiMLPResult.labelT1Verdict.setText("Loser")
			self.uiMLPResult.labelT2Verdict.setText("Winner")

	
	def startUIDTResult(self):
		self.uiDTResult.setupUi(self)
		self.uiDTResult.labelWinner.setText(DTClf.winner)

	def updateFlagTeams(self,currentLabel,currentValueName):
		currentPath = "/home/jaykay12/Downloads/cricAI/desktopApp/BasicUIApp/images/flags/"+str(currentValueName)+".jpg"
		pixmap = QtGui.QPixmap(currentPath)
		currentLabel.setPixmap(pixmap)

	def grabAndSetInput(self):
		self.t1 = str(self.uiWindow.comboBoxTeam1.currentText())
		self.t2 = str(self.uiWindow.comboBoxTeam2.currentText())

		ground = str(self.uiWindow.comboBoxGround.currentText())

		if self.uiWindow.rbTeam1_Innings.isChecked() == True:
			inningsTeam1 = "Team1_1Inning"
			inningsTeam2 = "Team2_2Inning"
		elif self.uiWindow.rbTeam2_Innings.isChecked() == True:
			inningsTeam1 = "Team1_2Inning"
			inningsTeam2 = "Team2_1Inning"

		if self.uiWindow.rbTeam1_Home.isChecked() == True:
			venueTeam1 = "Team1_Home"
			venueTeam2 = "Team2_Away"
		elif self.uiWindow.rbTeam2_Home.isChecked() == True:
			venueTeam1 = "Team1_Away"
			venueTeam2 = "Team2_Home"
		elif self.uiWindow.rb_Neutral.isChecked() == True:
			venueTeam1 = "Team1_Neutral"
			venueTeam2 = "Team2_Neutral"

		self.inputPrediction = [0]*217

		self.inputPrediction[dIF.ourTeams_1[self.t1]] = 1
		self.inputPrediction[dIF.ourTeams_2[self.t2]] = 1
		self.inputPrediction[dIF.ourGrounds[ground]] = 1
		self.inputPrediction[dIF.ourInnings[inningsTeam1]] = 1
		self.inputPrediction[dIF.ourInnings[inningsTeam2]] = 1
		self.inputPrediction[dIF.ourVenues[venueTeam1]] = 1
		self.inputPrediction[dIF.ourVenues[venueTeam2]] = 1


	def runCLFClassifier(self):
		self.grabAndSetInput()
		MLPClf.runModel(self.inputPrediction,self.t1,self.t2)
		self.startUIMLPResult()

	def runDTClassifier(self):
		self.grabAndSetInput()
		DTClf.runModel(self.inputPrediction,self.t1,self.t2)
		self.startUIDTResult()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())