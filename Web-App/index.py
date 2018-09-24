import sys, os
from Classifier import ourMLPClassifier,ourDTClassifier,ourSVMClassifier
import dataInputFormat
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
	if request.method == "POST":
		team1 = request.form['team1']
		team2 = request.form['team2']
		innings_t1 = request.form['innings_t1']
		venue_t1 = request.form['venue_t1']
		ground= request.form['ground']
		choice = request.form['choice']
		
		#print(team1, team2, innings_t1, venue_t1, ground, choice, file=sys.stderr)
		return render_template('result.html',result = getResults(ground, int(innings_t1), int(venue_t1), team1, team2, int(choice)))
	else:
		return render_template('index.html')

@app.route('/result', methods = ["GET","POST"])
def result():
	if request.method == "POST":
		a = request.form['team1']
		#print("Hellooo...!", a, file=sys.stderr)
		

def getResults(ground, innings, venue, team1, team2, choice):
	ground=ground[1:-1]
	team1=team1[1:-1]
	team2=team2[1:-1]

	SVMClf = ourSVMClassifier()
	MLPClf = ourMLPClassifier()
	DTClf = ourDTClassifier()
	
	dIF = dataInputFormat.DataInput_Categorical()

	print("Starting Up..!\n\nLoading Pickled Models")
	SVMClf.loadPickle()
	DTClf.loadPickle()
	MLPClf.loadPickle()

	dIF.hashAll()

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
		

if __name__ =='__main__':
	app.run(debug=True)
