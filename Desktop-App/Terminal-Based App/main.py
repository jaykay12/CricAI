import sys
from Classifier import ourMLPClassifier,ourDTClassifier
import dataInputFormat

if __name__ == '__main__':

	MLPClf = ourMLPClassifier()
	DTClf = ourDTClassifier()
	dIF = dataInputFormat.DataInput()

	print("Starting Up..!\n\nLoading Pickled Models")
	MLPClf.loadPickle()
	print("MLP Model:\tDone!")
	DTClf.loadPickle()
	print("Decision Tree Classifier:\tDone!")
	dIF.hashAll()

	while True:
		choice = int(input("\n\nHit 0 to Exit & Hit 1 to proceed: "))
		if choice == 0:
			break

		inputPrediction = [0]*217

		t1 = input("Input Team 1: ")
		t2 = input("Input Team 2: ")
		ground = input("Input Ground: ")
		innings = int(input("First Innings By\t[Team 1:1] [Team 2:2]: "))
		venue = int(input("Venue\t[Home of Team 1:1] [Home of Team 2:2] [Neutral:3]: "))

		if innings == 1:
			inningsTeam1 = "Team1_1Inning"
			inningsTeam2 = "Team2_2Inning"
		elif innings == 2:
			inningsTeam1 = "Team1_2Inning"
			inningsTeam2 = "Team2_1Inning"
		else:
			print("Don't You Dare to CRASH the system!")
			sys.exit()

		if venue == 1:
			venueTeam1 = "Team1_Home"
			venueTeam2 = "Team2_Away"
		elif venue == 2:
			venueTeam1 = "Team1_Away"
			venueTeam2 = "Team2_Home"
		elif venue == 3:
			venueTeam1 = "Team1_Neutral"
			venueTeam2 = "Team2_Neutral"
		else:
			print("Don't You Dare to CRASH the system!")
			sys.exit()	
	
		inputPrediction[dIF.ourTeams_1[t1]] = 1
		inputPrediction[dIF.ourTeams_2[t2]] = 1
		inputPrediction[dIF.ourGrounds[ground]] = 1
		inputPrediction[dIF.ourInnings[inningsTeam1]] = 1
		inputPrediction[dIF.ourInnings[inningsTeam2]] = 1
		inputPrediction[dIF.ourVenues[venueTeam1]] = 1
		inputPrediction[dIF.ourVenues[venueTeam2]] = 1

		print("Menu:\n1- MLPClassifier\n2- DTClassifier\n3- Exit")
		choice = int(input())
		if choice==1:
			MLPClf.runModel(inputPrediction,t1,t2)
		elif choice==2:
			DTClf.runModel(inputPrediction,t1,t2)
		elif choice==3:
			sys.exit()
		else:
			print("Don't You Dare to CRASH the system!")
			sys.exit()
