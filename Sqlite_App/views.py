from flask import render_template,request,redirect,url_for,flash
from Sqlite_App import app,db,making_db
from Sqlite_App.models import Emm,CorpIT,Result,Outlook,Idam,Map
import pandas as pd
import sqlalchemy
from datetime import datetime
app.secret_key="secret key"
@app.route("/")
@app.route("/home")
def home():
    data = Result.query.filter_by().all()
    return render_template("index.html",data =data, team="home")

@app.route('/dropdown', methods=['GET'])
def dropdown():
    month = ['may', 'june', 'july']
    return render_template('test.html', month=month)

@app.route("/test")
def test():
    # print("This is type ",Result.Date.between('2019-05-26 00:00:00','2019-05-31 00:00:00'))
    data = Result.query.filter(Result.Date.between('2019-05-26 00:00:00','2019-05-31 00:00:00')).all()

    return render_template("index.html", data=data,team="home")

@app.route("/corp")
def corp():
    data = CorpIT.query.filter_by().all()
    return render_template("team.html", data=data, team="corp")

@app.route("/map")
def MapT():
    data = Map.query.filter_by().all()
    return render_template("team.html", data=data, team="map")

@app.route("/outlook")
def Out():
    data=Outlook.query.filter_by().all()
    return render_template("team.html",data=data,team="outlook")

@app.route("/idam")
def IdamT():
    data=Idam.query.filter_by().all()
    return render_template("team.html",data=data,team = "idam")

@app.route("/emm")
def EmmT():
    data=Emm.query.filter_by().all()
    return render_template("team.html",data=data,team="emm")

@app.route("/refresh/<team>")
def refresh(team):
    if team=='corp':
        making_db()
        data = CorpIT.query.filter_by().all()
        return render_template("team.html",data=data,team="corp")
    elif team=='outlook':
        making_db()
        data = Outlook.query.filter_by().all()
        return render_template("team.html",data=data,team=team)
    elif team=='idam':
        making_db()
        data = Idam.query.filter_by().all()
        return render_template("team.html",data=data,team=team)
    elif team=='emm':
        making_db()
        data = Emm.query.filter_by().all()
        return render_template("team.html",data=data,team=team)
    elif team=='map':
        making_db()
        data = Map.query.filter_by().all()
        return render_template("team.html",data=data,team=team)
    elif team == 'home':
        data = Result.query.filter_by().all()
        return render_template("index.html",data=data,team="home")
from datetime import datetime
# @app.route("home/<month>")
# def filtermonth(month):
#     data = Result.query.filter(datetime(Result.Date)).





