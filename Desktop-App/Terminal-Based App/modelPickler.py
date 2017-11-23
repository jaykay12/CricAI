import sys
import pickle
from Classifier import ourMLPClassifier, ourDTClassifier

if __name__ == '__main__':

	MLPClf = ourMLPClassifier()
	DTClf = ourDTClassifier()

	print("Beginning to Pickle MLP Model!")
	MLPClf.trainModel()
	MLPClf.accuracyCheck()
	MLPClf.dumpPickle()

	print("Done: MLP Model!")

	print("Beginning to Pickle DT Model!")
	DTClf.trainModel()
	DTClf.accuracyCheck()
	DTClf.dumpPickle()
	print("Done: DT Model!\n")