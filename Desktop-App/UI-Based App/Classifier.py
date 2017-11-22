import datasetRead
import dataInputFormat
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

d = datasetRead.Dataset()
dIF = dataInputFormat.DataInput()

class ourMLPClassifier:
	def trainModel(self):
		d.ReadDataSet()
		self.MLPclf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 32), random_state=1)
		self.MLPclf.fit(d.X_train, d.Y_train)

	def accuracyCheck(self):
		print("\nMulti Layer Perceptron Classifer:")
		test_predicted = self.MLPclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.MLPclf.predict(d.X_train)
		print("Accuracy for Training Dataset:",accuracy_score(d.Y_train, train_predicted))

	def runModel(self,inputPrediction,t1,t2):
		ourPrediction = self.MLPclf.predict_proba([inputPrediction])

		dIF.hashingTargetWinners()
		totalPrediction = ourPrediction[0][dIF.winnerIndex[t1]] + ourPrediction[0][dIF.winnerIndex[t2]]
		self.predictionT1 = (ourPrediction[0][dIF.winnerIndex[t1]]/totalPrediction) * 100
		self.predictionT2 = (ourPrediction[0][dIF.winnerIndex[t2]]/totalPrediction) * 100
		print("\n")
		print(t1,":",self.predictionT1,"%")
		print(t2,":",self.predictionT2,"%")


class ourDTClassifier:
	def trainModel(self):
		d.ReadDataSet()
		self.DTclf = tree.DecisionTreeClassifier()
		self.DTclf.fit(d.X_train, d.Y_train)

	def accuracyCheck(self):
		print("\nDecision Tree Classifier:")
		test_predicted = self.DTclf.predict(d.X_test)
		print("Accuracy for Testing Dataset:",accuracy_score(d.Y_test, test_predicted))
		train_predicted = self.DTclf.predict(d.X_train)
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
		    self.winner = "UnPredictable"