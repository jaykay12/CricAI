import sys
from Classifier import ourMLPClassifier,ourDTClassifier,ourSVMClassifier
import dataInputFormat
from flask import *

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
	
	if request.method == "POST":
		first = request.form['First']
		opponent = request.form['opponent']
		innings= request.form['innings']
		venue= request.form['venue']
		ground= request.form['Ground']
		
		print( first, opponent, innings, venue, ground, file=sys.stderr)
		return render_template('result.html',result = main1(ground,int(innings), int(venue), first,opponent))
	else:
		return render_template('index.html')

@app.route('/result', methods = ["GET","POST"])
def result():
	if request.method == "POST":
		a = request.form['First']
		print("dsdsfdsafdsfdsfdsfaadfsdfsadsfdfs", a, file=sys.stderr)
		

def main1(ground, innings, venue, t1,t2):
	ground=ground[1:-1]
	t1=t1[1:-1]
	t2=t2[1:-1]

	SVMClf = ourSVMClassifier()
	
	dIF = dataInputFormat.DataInput()

	print("Starting Up..!\n\nLoading Pickled Models")
	
	SVMClf.loadPickle()
	print("SVM Classifier:\tDone!")
	dIF.hashAll()

	#choice = int(input("\n\nHit 0 to Exit & Hit 1 to proceed: "))
	choice = 3


	inputPrediction = [0]*217


	
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

	print("Menu:\n1- MLPClassifier\n2- DTClassifier\n3- SVMClassifier\n4- Exit")
	
	if choice==1:
		MLPClf.runModel(inputPrediction,t1,t2)
	elif choice==2:
		DTClf.runModel(inputPrediction,t1,t2)
	elif choice==3:
		return SVMClf.runModel(inputPrediction,t1,t2)
	elif choice==4:
		sys.exit()
	else:
		print("Don't You Dare to CRASH the system!")
		sys.exit()

if __name__ =='__main__':
	app.run(debug=True)
