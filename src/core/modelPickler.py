import sys, os
import pickle

# Adds the 'src' directory to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.Classifier import ourMLPClassifier, ourDTClassifier,ourSVMClassifier

def initialise_models():
	SVMClf = ourSVMClassifier()
	MLPClf = ourMLPClassifier()
	DTClf = ourDTClassifier()
	
	print("----- Beginning to Pickle: SVM Model! -----")
	SVMClf.trainModel()
	SVMClf.accuracyCheck()
	SVMClf.dumpPickle()
	print("Done: SVM Model!\n")
	
	# print("Beginning to Pickle MLP Model!")
	# MLPClf.trainModel()
	# MLPClf.accuracyCheck()
	# MLPClf.dumpPickle()
	# print("Done: MLP Model!\n")

	print("----- Beginning to Pickle: DT Model! -----")
	DTClf.trainModel()
	DTClf.accuracyCheck()
	DTClf.dumpPickle()
	print("Done: DT Model!\n")

if __name__ == '__main__':
	initialise_models()

	
	
	
	
