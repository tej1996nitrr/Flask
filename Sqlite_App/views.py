from flask import render_template,request,redirect,url_for,flash
from Sqlite_App import app,db,making_db
from Sqlite_App.models import Emm,CorpIT,Result,Outlook,Idam,Map
import pandas as pd
import sqlalchemy
app.secret_key="secret key"
@app.route("/")
@app.route("/home")
def home():
    data=Result.query.filter_by().all()
    return render_template("index.html",data=data)


@app.route("/corp")
def corp():
    data=CorpIT.query.filter_by().all()
    return render_template("team.html",data=data)

@app.route("/map")
def MapT():
    data=Map.query.filter_by().all()
    return render_template("team.html",data=data)

@app.route("/outlook")
def Out():
    data=Outlook.query.filter_by().all()
    return render_template("team.html",data=data)

@app.route("/idam")
def IdamT():
    data=Idam.query.filter_by().all()
    return render_template("team.html",data=data)

@app.route("/emm")
def EmmT():
    data=Emm.query.filter_by().all()
    return render_template("team.html",data=data)

@app.route("/refresh")
def refresh():
    # if team=='corp':
    #     making_db()
    #     data = CorpIT.query.filter_by().all()
    #     return redirect("/corp")
    # elif team=='outlook':
    #     making_db()
    #     data = Outlook.query.filter_by().all()
    #     return redirect("/outlook")
    # elif team=='idam':
    #     making_db()
    #     data = Idam.query.filter_by().all()
    #     return redirect("/idam")
    # elif team=='emm':
    #     making_db()
    #     data = Emm.query.filter_by().all()
    #     return redirect("/emm")
    # elif team=='map':
    #     making_db()
    #     data = Map.query.filter_by().all()
    #     return redirect("/map")
    # elif team == 'home':
    #     data = Result.query.filter_by().all()
    #     return redirect("/home")
    pass




