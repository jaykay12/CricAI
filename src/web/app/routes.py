import sys
from flask import request, render_template
from index import app

from app.services.predictor import predict_match_outcome

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        team1 = request.form['team1']
        team2 = request.form['team2']
        innings_t1 = request.form['innings_t1']
        venue_t1 = request.form['venue_t1']
        ground = request.form['ground']
        choice = request.form['choice']
        
        return render_template(
            'result.html',
            result=predict_match_outcome(ground, int(innings_t1), int(venue_t1), team1, team2, int(choice))
        )
    else:
        return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        a = request.form['team1']
        # Flask routes must always return something, so we return a dummy string here
        return f"Result received for team: {a}" 
    return "Result GET route"