import os
import pickle

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


from core.datasetRead import Dataset
from core.dataInputFormat import DataInput_Categorical, DataInput_Labelled

d = Dataset()
dIFLabelled = DataInput_Labelled()
dIFCategorical = DataInput_Categorical()

BASE_OUTPUT_PKL_PATH = "/data/"


class ourSVMClassifier:
	def trainModel(self):
		d.ReadLabelledDataSet()
		self.TrainedSVMclf = SVC(kernel="linear")
		self.TrainedSVMclf.fit(d.X_train, d.Y_train)

	def dumpPickle(self):
		SVMPickleFile = "svm_classifier.pkl"
		SVMPickledModel = open(BASE_DIR + BASE_OUTPUT_PKL_PATH + SVMPickleFile,'wb')
		pickle.dump(self.TrainedSVMclf,SVMPickledModel)
		SVMPickledModel.close()

	def loadPickle(self):
		SVMPickleFile = "svm_classifier.pkl"
		SVMPickledModel = open(BASE_DIR + BASE_OUTPUT_PKL_PATH + SVMPickleFile,'rb')
		self.SVMclf = pickle.load(SVMPickledModel)

	def accuracyCheck(self):
		d.ReadLabelledDataSet()
		print("\nSVM Classifier:")
		test_predicted = self.TrainedSVMclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.TrainedSVMclf.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		winnerTeam = self.SVMclf.predict([inputPrediction])
		print(winnerTeam[0])

		return winnerTeam[0]

		
class ourMLPClassifier:
	def trainModel(self):
		d.ReadCategoricalDataSet()
		self.TrainedMLPclf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 32), random_state=1)
		self.TrainedMLPclf.fit(d.X_train, d.Y_train)
		self.accuracyCheck(self.TrainedMLPclf)

	def dumpPickle(self):
		MLPPickleFile = "mlp_classifier.pkl"
		MLPPickledModel = open(BASE_DIR + BASE_OUTPUT_PKL_PATH + MLPPickleFile,'wb')
		pickle.dump(self.TrainedMLPclf,MLPPickledModel)
		MLPPickledModel.close()

	def loadPickle(self):
		MLPPickleFile = "mlp_classifier.pkl"
		MLPPickledModel = open(BASE_DIR + BASE_OUTPUT_PKL_PATH + MLPPickleFile,'rb')
		self.MLPclf = pickle.load(MLPPickledModel)

	def accuracyCheck(self):
		d.ReadCategoricalDataSet()
		print("\nMulti Layer Perceptron Classifer:")
		test_predicted = self.TrainedMLPclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.TrainedMLPclf.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.MLPclf.predict_proba([inputPrediction])

		print(ourPrediction)

		dIFCategorical.hashingTargetWinners()
		print(dIFCategorical.winnerIndex)
		
		totalPrediction = ourPrediction[0][dIFCategorical.winnerIndex[t1]] + ourPrediction[0][dIFCategorical.winnerIndex[t2]]
		self.predictionT1 = (ourPrediction[0][dIFCategorical.winnerIndex[t1]]/totalPrediction) * 100
		self.predictionT2 = (ourPrediction[0][dIFCategorical.winnerIndex[t2]]/totalPrediction) * 100

		if dIFCategorical.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(self.predictionT1) < 10.0:
			self.predictionT1 = float(self.predictionT1) + 20
			self.predictionT2 = float(self.predictionT2) - 20
		elif dIFCategorical.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(self.predictionT1) < 20.0:
			self.predictionT1 = float(self.predictionT1) + 10
			self.predictionT2 = float(self.predictionT2) - 10

		if dIFCategorical.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(self.predictionT2) < 10.0:
			self.predictionT2 = float(self.predictionT2) + 20
			self.predictionT1 = float(self.predictionT1) - 20
		elif dIFCategorical.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(self.predictionT2) < 20.0:
			self.predictionT2 = float(self.predictionT2) + 10
			self.predictionT1 = float(self.predictionT1) - 10

		self.predictionT1 = format(float(self.predictionT1), '.4f')
		self.predictionT2 = format(float(self.predictionT2), '.4f')

		print("\n")
		print(t1,":",self.predictionT1,"%")
		print(t2,":",self.predictionT2,"%")

		winnerTeam=""
		if self.predictionT1>self.predictionT2:
			winnerTeam=t1
		else:
			winnerTeam=t2
		

		return winnerTeam


class ourDTClassifier:
	def trainModel(self):
		d.ReadCategoricalDataSet()
		self.TrainedDTclf = DecisionTreeClassifier()
		self.TrainedDTclf.fit(d.X_train, d.Y_train)

	def dumpPickle(self):
		DTPickleFile = "dt_classifier.pkl"
		DTPickledModel = open(BASE_DIR + BASE_OUTPUT_PKL_PATH + DTPickleFile,'wb')
		pickle.dump(self.TrainedDTclf,DTPickledModel)
		DTPickledModel.close()

	def loadPickle(self):
		DTPickleFile = "dt_classifier.pkl"
		DTPickledModel = open(BASE_DIR + BASE_OUTPUT_PKL_PATH + DTPickleFile,'rb')
		self.DTclf = pickle.load(DTPickledModel)

	def accuracyCheck(self):
		d.ReadCategoricalDataSet()
		print("\nDecision Tree Classifier:")
		test_predicted = self.TrainedDTclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.TrainedDTclf.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.DTclf.predict([inputPrediction])

		dIFCategorical.hashingTargetWinners()
		indexTeam1 = dIFCategorical.winnerIndex[t1]
		indexTeam2 = dIFCategorical.winnerIndex[t2]
		
		winnerTeam = ""
		if ourPrediction[0][indexTeam1] == 1:
			winnerTeam = t1
			print("Winner:",t1)
		elif ourPrediction[0][indexTeam2] == 1:
			winnerTeam = t2
			print("Winner:",t2)
		else:
			winnerTeam = "Decision Tree Classifier Can't Predict for this match reliably!"
			print("Decision Tree Classifier Can't Predict for this match reliably!")

		self.winner = winnerTeam
		return winnerTeam