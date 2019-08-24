from Sqlite_App import db,app

class Emm(db.Model):
    ID = db.Column('index',db.Integer,primary_key=True)
    Date =db.Column('Date',db.DateTime, default=db.func.current_timestamp())
    Incident_Inflow =db.Column('Incident_Inflow',db.Integer)
    Incident_Resolved = db.Column('Incident_Resolved', db.Integer)
    Incident_Backlog = db.Column('Incident_Backlog', db.Integer)
    Request_Inflow = db.Column('Request_Inflow', db.Integer)
    Request_Resolved = db.Column('Request_Resolved', db.Integer)
    Request_Backlog = db.Column('Request_Backlog', db.Integer)



class CorpIT(db.Model):
    ID = db.Column('index',db.Integer,primary_key=True)
    Date =db.Column('Date',db.DateTime, default=db.func.current_timestamp())
    Incident_Inflow = db.Column('Incident_Inflow', db.Integer)
    Incident_Resolved = db.Column('Incident_Resolved', db.Integer)
    Incident_Backlog = db.Column('Incident_Backlog', db.Integer)
    Request_Inflow = db.Column('Request_Inflow', db.Integer)
    Request_Resolved = db.Column('Request_Resolved', db.Integer)
    Request_Backlog = db.Column('Request_Backlog', db.Integer)

class Idam(db.Model):
    ID = db.Column('index',db.Integer,primary_key=True)
    Date =db.Column('Date',db.DateTime, default=db.func.current_timestamp())
    Incident_Inflow = db.Column('Incident_Inflow', db.Integer)
    Incident_Resolved = db.Column('Incident_Resolved', db.Integer)
    Incident_Backlog = db.Column('Incident_Backlog', db.Integer)
    Request_Inflow = db.Column('Request_Inflow', db.Integer)
    Request_Resolved = db.Column('Request_Resolved', db.Integer)
    Request_Backlog = db.Column('Request_Backlog', db.Integer)

class Map(db.Model):
    ID = db.Column('index',db.Integer,primary_key=True)
    Date =db.Column('Date',db.DateTime, default=db.func.current_timestamp())
    Incident_Inflow = db.Column('Incident_Inflow', db.Integer)
    Incident_Resolved = db.Column('Incident_Resolved', db.Integer)
    Incident_Backlog = db.Column('Incident_Backlog', db.Integer)
    Request_Inflow = db.Column('Request_Inflow', db.Integer)
    Request_Resolved = db.Column('Request_Resolved', db.Integer)
    Request_Backlog = db.Column('Request_Backlog', db.Integer)

class Outlook(db.Model):
    ID = db.Column('index',db.Integer,primary_key=True)
    Date =db.Column('Date',db.DateTime, default=db.func.current_timestamp())
    Incident_Inflow = db.Column('Incident_Inflow', db.Integer)
    Incident_Resolved = db.Column('Incident_Resolved', db.Integer)
    Incident_Backlog = db.Column('Incident_Backlog', db.Integer)
    Request_Inflow = db.Column('Request_Inflow', db.Integer)
    Request_Resolved = db.Column('Request_Resolved', db.Integer)
    Request_Backlog = db.Column('Request_Backlog', db.Integer)

class Result(db.Model):
    ID = db.Column('index',db.Integer,primary_key=True)
    Date =db.Column('Date',db.DateTime, default=db.func.current_timestamp())
    Total_Inc_Inflow = db.Column('Total_Inc_Inflow', db.Integer)
    Total_Inc_Resolved = db.Column('Total_Inc_Resolved', db.Integer)
    Total_Inc_Backlog = db.Column('Total_Inc_Backlog', db.Integer)
    Total_Req_Inflow = db.Column('Total_Req_Inflow', db.Integer)
    Total_Req_Resolved = db.Column('Total_Req_Resolved', db.Integer)
    Total_Req_Backlog = db.Column('Total_Req_Backlog', db.Integer)
    Total_Backlog = db.Column('Total_Backlog', db.Integer)
