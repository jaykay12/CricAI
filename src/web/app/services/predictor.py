import logging
import sys
import os

# Adds the 'src' directory to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.Classifier import ourMLPClassifier,ourDTClassifier,ourSVMClassifier
from core import dataInputFormat, modelPickler

# Global initialization: Models load ONCE when the app starts
logger.info("Loading Pickled Models into memory...!")
SVMClf = ourSVMClassifier()
MLPClf = ourMLPClassifier()
DTClf = ourDTClassifier()

logger.info("Loading Pickled Models...!")
SVMClf.loadPickle()
DTClf.loadPickle()
MLPClf.loadPickle()


dIF = dataInputFormat.DataInput_Categorical()
dIF.hashAll()


def predict_match_outcome(ground, innings, venue, team1, team2, choice):
	ground=ground[1:-1]
	team1=team1[1:-1]
	team2=team2[1:-1]

	inputPrediction = [0]*217
	if innings == 1:
		inningsTeam1 = "Team1_1Inning"
		inningsTeam2 = "Team2_2Inning"
	elif innings == 2:
		inningsTeam1 = "Team1_2Inning"
		inningsTeam2 = "Team2_1Inning"

	if venue == 1:
		venueTeam1 = "Team1_Home"
		venueTeam2 = "Team2_Away"
	elif venue == 2:
		venueTeam1 = "Team1_Away"
		venueTeam2 = "Team2_Home"
	elif venue == 3:
		venueTeam1 = "Team1_Neutral"
		venueTeam2 = "Team2_Neutral"

	inputPrediction[dIF.ourTeams_1[team1]] = 1
	inputPrediction[dIF.ourTeams_2[team2]] = 1
	inputPrediction[dIF.ourGrounds[ground]] = 1
	inputPrediction[dIF.ourInnings[inningsTeam1]] = 1
	inputPrediction[dIF.ourInnings[inningsTeam2]] = 1
	inputPrediction[dIF.ourVenues[venueTeam1]] = 1
	inputPrediction[dIF.ourVenues[venueTeam2]] = 1
	
	if choice==1:
		return SVMClf.runModel(inputPrediction,team1,team2)
	elif choice==2:
		return DTClf.runModel(inputPrediction,team1,team2)
	elif choice==3:
		return MLPClf.runModel(inputPrediction,team1,team2)