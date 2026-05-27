import sys
from flask import request, render_template, Blueprint

main = Blueprint('main', __name__)

from app.services.predictor import predict_match_outcome

@main.route('/', methods = ["GET","POST"])
def home():
	if request.method == "POST":
		team1 = request.form['team1']
		team2 = request.form['team2']
		innings_t1 = request.form['innings_t1']
		venue_t1 = request.form['venue_t1']
		ground= request.form['ground']
		choice = request.form['choice']
		
		#print(team1, team2, innings_t1, venue_t1, ground, choice, file=sys.stderr)
		return render_template('result.html', result = predict_match_outcome(
            ground, int(innings_t1), int(venue_t1), team1, team2, int(choice)
        ))
	else:
		return render_template('index.html')

@main.route('/health', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "healthy",
        "message": "CricAI is running smoothly ⚡"
    }), 200