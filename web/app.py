from flask import Flask, render_template, request, redirect, url_for
from models import Table, Team
from datetime import date


def create_app(t):
    app = Flask(__name__, template_folder='templates')

    @app.route("/")
    def index():
        standings = t.return_table()
        fixtureList = t.return_fixtures()
        
        teams_alphabetical = sorted(
                t.teams.values(),
                key=lambda team: team.name
            )
        return render_template("index.html", standings=standings, fixtureList=fixtureList,
                               teams=teams_alphabetical)
    
#To access the createFixture() function from the Website    
    @app.route("/addFixture", methods=['GET', 'POST'])
    def addFixture():
        
        print("addFixture called")
        print("method:", request.method)
        print(request.form)
       
        if request.method == "POST":
            
            homeTeam = request.form["homeTeam"]
            awayTeam = request.form["awayTeam"]
            
            if homeTeam == awayTeam:
                return("Home and away have to be different!")
            
            
            fixtureDate = request.form["date"]
            
            d = date.fromisoformat(fixtureDate)
            
            t.createFixture(homeTeam, awayTeam, d)
            
            return redirect(url_for("index"))
       
        return redirect(url_for("index"))
    
    @app.route("/addResult", methods=['GET', 'POST'])
    def addResult():
        
        if request.method == "GET":
            fcode = request.args["fcode"]
            fixture = t.fixtures[fcode]
            return render_template("addResult.html", fixture=fixture)
        
        if request.method == "POST":
            fcode = request.form["fcode"]
            homeScore = int(request.form["homeScore"])
            awayScore = int(request.form["awayScore"])
            
            print("fcode: ",fcode,"| homeScore: ",homeScore,"| awayScore: ", awayScore)
            
            t.addResults(fcode, homeScore, awayScore)
                     
            #t.addResults(fcode, homeScore, awayScore)
        return redirect(url_for("index"))
        
    return app

def run_web(t):
    app = create_app(t)
    app.run(debug=True)