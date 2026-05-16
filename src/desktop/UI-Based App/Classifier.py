import datasetRead
import dataInputFormat
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

d = datasetRead.Dataset()
dIF = dataInputFormat.DataInput()

class ourMLPClassifier:
	def trainModel(self):
		d.ReadDataSet()
		self.TrainedMLPclf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 32), random_state=1)
		self.TrainedMLPclf.fit(d.X_train, d.Y_train)

		self.accuracyCheck(self.TrainedMLPclf)

	def dumpPickle(self):
		MLPPickleFile = "Pickle_MLPClf.pkl"
		MLPPickledModel = open(MLPPickleFile,'wb')
		pickle.dump(self.TrainedMLPclf,MLPPickledModel)
		MLPPickledModel.close()

	def loadPickle(self):
		MLPPickleFile = "Pickle_MLPClf.pkl"
		MLPPickledModel = open(MLPPickleFile,'rb')
		self.MLPclf = pickle.load(MLPPickledModel)

	def accuracyCheck(self,model):
		d.ReadDataSet()
		print("\nMulti Layer Perceptron Classifer:")
		test_predicted = model.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = model.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.MLPclf.predict_proba([inputPrediction])

		dIF.hashingTargetWinners()

		print(ourPrediction)

		print(ourPrediction[0][dIF.winnerIndex[t1]])
		print(ourPrediction[0][dIF.winnerIndex[t2]])

		print(float(ourPrediction[0][dIF.winnerIndex[t1]]))
		print(float(ourPrediction[0][dIF.winnerIndex[t2]]))



		totalPrediction = ourPrediction[0][dIF.winnerIndex[t1]] + ourPrediction[0][dIF.winnerIndex[t2]]

		print(totalPrediction)

		self.predictionT1 = (ourPrediction[0][dIF.winnerIndex[t1]]/totalPrediction) * 100
		self.predictionT2 = (ourPrediction[0][dIF.winnerIndex[t2]]/totalPrediction) * 100

		print(self.predictionT1)
		print(self.predictionT2)

#		self.predictionT1 = format(self.predictionT1, '.2f')
#		self.predictionT2 = format(self.predictionT2, '.2f')

		if dIF.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(self.predictionT1) < 10.0:
			self.predictionT1 = float(self.predictionT1) + 25
			self.predictionT2 = float(self.predictionT2) - 25
		elif dIF.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(self.predictionT1) < 20.0:
			self.predictionT1 = float(self.predictionT1) + 15
			self.predictionT2 = float(self.predictionT2) - 15
		elif dIF.winnerIndex[t1] in [1,6,8,13,15,17,18,21] and float(self.predictionT1) < 30.0:
			self.predictionT1 = float(self.predictionT1) + 5
			self.predictionT2 = float(self.predictionT2) - 5


		if dIF.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(self.predictionT2) < 10.0:
			self.predictionT2 = float(self.predictionT2) + 25
			self.predictionT1 = float(self.predictionT1) - 25
		elif dIF.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(self.predictionT2) < 20.0:
			self.predictionT2 = float(self.predictionT2) + 15
			self.predictionT1 = float(self.predictionT1) - 15
		elif dIF.winnerIndex[t2] in [1,6,8,13,15,17,18,21] and float(self.predictionT2) < 30.0:
			self.predictionT2 = float(self.predictionT2) + 5
			self.predictionT1 = float(self.predictionT1) - 5


		self.predictionT1 = format(self.predictionT1, '.4f')
		self.predictionT2 = format(self.predictionT2, '.4f')

		print("\n")
		print(t1,":",self.predictionT1,"%")
		print(t2,":",self.predictionT2,"%")


class ourDTClassifier:
	def trainModel(self):
		d.ReadDataSet()
		self.TrainedDTclf = tree.DecisionTreeClassifier()
		self.TrainedDTclf.fit(d.X_train, d.Y_train)

		self.accuracyCheck(self.TrainedDTclf)

	def dumpPickle(self):
		DTPickleFile = "Pickle_DTClf.pkl"
		DTPickledModel = open(DTPickleFile,'wb')
		pickle.dump(self.TrainedDTclf,DTPickledModel)
		DTPickledModel.close()

	def loadPickle(self):
		DTPickleFile = "Pickle_DTClf.pkl"
		DTPickledModel = open(DTPickleFile,'rb')
		self.DTclf = pickle.load(DTPickledModel)

	def accuracyCheck(self,model):
		d.ReadDataSet()
		print("\nDecision Tree Classifier:")
		test_predicted = model.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = model.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.DTclf.predict([inputPrediction])

		dIF.hashingTargetWinners()
		indexTeam1 = dIF.winnerIndex[t1]
		indexTeam2 = dIF.winnerIndex[t2]
		if ourPrediction[0][indexTeam1] == 1:
		    print("Winner:",t1)
		    self.winner = t1
		elif ourPrediction[0][indexTeam2] == 1:
		    print("Winner:",t2)
		    self.winner = t2
		else:
		    print("Decision Tree Classifier Can't Predict for this match reliably!")
		    self.winner = 1