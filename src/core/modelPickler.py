import sys
import pickle
from Classifier import ourMLPClassifier, ourDTClassifier,ourSVMClassifier

if __name__ == '__main__':

	SVMClf = ourSVMClassifier()
	MLPClf = ourMLPClassifier()
	DTClf = ourDTClassifier()
	
	print("Beginning to Pickle SVM Model!")
	SVMClf.trainModel()
	SVMClf.accuracyCheck()
	SVMClf.dumpPickle()
	print("Done: SVM Model!\n")
	
	print("Beginning to Pickle MLP Model!")
	MLPClf.trainModel()
	MLPClf.accuracyCheck()
	MLPClf.dumpPickle()
	print("Done: MLP Model!\n")

	print("Beginning to Pickle DT Model!")
	DTClf.trainModel()
	DTClf.accuracyCheck()
	DTClf.dumpPickle()
	print("Done: DT Model!\n")
	
	
	
