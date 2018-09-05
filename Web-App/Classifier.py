import datasetRead
import dataInputFormat
import pickle
import datasetLabelled
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import svm

d = datasetRead.Dataset()
e = datasetLabelled.LabelledDataset()
dIF = dataInputFormat.DataInput()


class ourSVMClassifier:
	def trainModel(self):
		e.ReadLabelledDataset()
		self.TrainedSVMclf = svm.SVC(kernel="linear")
		self.TrainedSVMclf.fit(	e.X_train, e.Y_train)

	def dumpPickle(self):
		SVMPickleFile = "Pickle_SVMClf.pkl"
		SVMPickledModel = open(SVMPickleFile,'wb')
		pickle.dump(self.TrainedSVMclf,SVMPickledModel)
		SVMPickledModel.close()

	def loadPickle(self):
		SVMPickleFile = "Pickle_SVMClf.pkl"
		SVMPickledModel = open(SVMPickleFile,'rb')
		self.SVMclf = pickle.load(SVMPickledModel)

	def accuracyCheck(self):
		e.ReadLabelledDataset()
		print("\nSVM Classifier:")
		test_predicted = self.TrainedSVMclf.predict(e.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(e.Y_test, test_predicted))
		train_predicted = self.TrainedSVMclf.predict(e.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(e.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.SVMclf.predict([inputPrediction])
		return ourPrediction[0]

		
class ourMLPClassifier:
	def trainModel(self):
		d.ReadDataSet()
		self.TrainedMLPclf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 32), random_state=1)
		self.TrainedMLPclf.fit(d.X_train, d.Y_train)

	def dumpPickle(self):
		MLPPickleFile = "Pickle_MLPClf.pkl"
		MLPPickledModel = open(MLPPickleFile,'wb')
		pickle.dump(self.TrainedMLPclf,MLPPickledModel)
		MLPPickledModel.close()

	def loadPickle(self):
		MLPPickleFile = "Pickle_MLPClf.pkl"
		MLPPickledModel = open(MLPPickleFile,'rb')
		self.MLPclf = pickle.load(MLPPickledModel)

	def accuracyCheck(self):
		d.ReadDataSet()
		print("\nMulti Layer Perceptron Classifer:")
		test_predicted = self.TrainedMLPclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.TrainedMLPclf.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.MLPclf.predict_proba([inputPrediction])

		#print(ourPrediction)

		dIF.hashingTargetWinners()
		#print(dIF.winnerIndex)
		totalPrediction = ourPrediction[0][dIF.winnerIndex[t1]] + ourPrediction[0][dIF.winnerIndex[t2]]
		predictionT1 = (ourPrediction[0][dIF.winnerIndex[t1]]/totalPrediction) * 100
		predictionT2 = (ourPrediction[0][dIF.winnerIndex[t2]]/totalPrediction) * 100

		predictionT1 = format(float(predictionT1), '.4f')
		predictionT2 = format(float(predictionT2), '.4f')

		if dIF.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(predictionT1) < 10.0:
			predictionT1 = float(predictionT1) + 20
			predictionT2 = float(predictionT2) - 20
		elif dIF.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(predictionT1) < 20.0:
			predictionT1 = float(predictionT1) + 10
			predictionT2 = float(predictionT2) - 10

		if dIF.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(predictionT2) < 10.0:
			predictionT2 = float(predictionT2) + 20
			predictionT1 = float(predictionT1) - 20
		elif dIF.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(predictionT2) < 20.0:
			predictionT2 = float(predictionT2) + 10
			predictionT1 = float(predictionT1) - 10


		print("\n")
		print(t1,":",predictionT1,"%")
		print(t2,":",predictionT2,"%")


class ourDTClassifier:
	def trainModel(self):
		d.ReadDataSet()
		self.TrainedDTclf = tree.DecisionTreeClassifier()
		self.TrainedDTclf.fit(d.X_train, d.Y_train)

	def dumpPickle(self):
		DTPickleFile = "Pickle_DTClf.pkl"
		DTPickledModel = open(DTPickleFile,'wb')
		pickle.dump(self.TrainedDTclf,DTPickledModel)
		DTPickledModel.close()

	def loadPickle(self):
		DTPickleFile = "Pickle_DTClf.pkl"
		DTPickledModel = open(DTPickleFile,'rb')
		self.DTclf = pickle.load(DTPickledModel)

	def accuracyCheck(self):
		d.ReadDataSet()
		print("\nDecision Tree Classifier:")
		test_predicted = self.TrainedDTclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.TrainedDTclf.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.DTclf.predict([inputPrediction])

		dIF.hashingTargetWinners()
		indexTeam1 = dIF.winnerIndex[t1]
		indexTeam2 = dIF.winnerIndex[t2]
		if ourPrediction[0][indexTeam1] == 1:
		    print("Winner:",t1)
		elif ourPrediction[0][indexTeam2] == 1:
		    print("Winner:",t2)
		else:
		    print("Decision Tree Classifier Can't Predict for this match reliably!")
