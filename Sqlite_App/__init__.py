from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np



def making_db():
    xls = pd.ExcelFile(r'F:\Jupyter\may.xlsx')
    emm = pd.read_excel(xls, 'EMM')
    corp = pd.read_excel(xls, 'CorpIT')
    out = pd.read_excel(xls, 'Outlook')
    idam = pd.read_excel(xls, 'Idam')
    map = pd.read_excel(xls, 'Map')
    engine = sqlalchemy.create_engine('sqlite:////database.db', echo=False)
    emm.to_sql('EMM', con=engine, if_exists='replace')
    corp.to_sql('CORPIT', con=engine, if_exists='replace')
    out.to_sql('Outlook', con=engine, if_exists='replace')
    idam.to_sql('Idam', con=engine, if_exists='replace')
    map.to_sql('Map', con=engine, if_exists='replace')

    columns = ['Date', 'Total_Inc_Inflow', 'Total_Inc_Resolved', 'Total_Inc_Backlog', 'Total_Req_Inflow',
               'Total_Req_Resolved', 'Total_Req_Backlog', 'Total_Backlog']

    result = pd.DataFrame(columns=columns)

    def larger_df(df1, df2, df3, df4, df5):
        if len(df2) == max(len(df1), len(df2), len(df3), len(df4), len(df5)):
            return df2
        elif len(df1) == max(len(df1), len(df2), len(df3), len(df4), len(df5)):
            return df1
        elif len(df3) == max(len(df1), len(df2), len(df3), len(df4), len(df5)):
            return df3
        elif len(df4) == max(len(df1), len(df2), len(df3), len(df4), len(df5)):
            return df4
        elif len(df5) == max(len(df1), len(df2), len(df3), len(df4), len(df5)):
            return df5

    large = larger_df(emm, corp, idam, out, map)
    corp = pd.merge(corp,
                    large[['Date']],
                    on='Date',
                    how='right')
    emm = pd.merge(emm,
                   large[['Date']],
                   on='Date',
                   how='right')
    idam = pd.merge(idam,
                    large[['Date']],
                    on='Date',
                    how='right')
    out = pd.merge(out,
                   large[['Date']],
                   on='Date',
                   how='right')
    map = pd.merge(map,
                   large[['Date']],
                   on='Date',
                   how='right')

    map = map.replace(np.nan, 0)
    out = out.replace(np.nan, 0)
    corp = corp.replace(np.nan, 0)
    idam = idam.replace(np.nan, 0)
    emm = emm.replace(np.nan, 0)

    result['Date'] = large['Date']
    result['Total_Inc_Inflow'] = emm['Incident_Inflow'] + corp['Incident_Inflow'] + out['Incident_Inflow'] + idam[
        'Incident_Inflow'] + map['Incident_Inflow']
    result['Total_Inc_Resolved'] = emm['Incident_Resolved'] + corp['Incident_Resolved'] + out['Incident_Resolved'] + \
                                   idam['Incident_Resolved'] + map['Incident_Resolved']
    result['Total_Inc_Backlog'] = emm['Incident_Backlog'] + corp['Incident_Backlog'] + out['Incident_Backlog'] + idam[
        'Incident_Backlog'] + map['Incident_Backlog']
    result['Total_Req_Inflow'] = emm['Request_Inflow'] + corp['Request_Inflow'] + out['Request_Inflow'] + idam[
        'Request_Inflow'] + map['Request_Inflow']
    result['Total_Req_Resolved'] = emm['Request_Resolved'] + corp['Request_Resolved'] + out['Request_Resolved'] + idam[
        'Request_Resolved'] + map['Request_Resolved']
    result['Total_Req_Backlog'] = emm['Request_Backlog'] + corp['Request_Backlog'] + out['Request_Backlog'] + idam[
        'Request_Backlog'] + map['Request_Backlog']
    result['Total_Backlog'] = result['Total_Req_Backlog'] + result['Total_Inc_Backlog']

    result.to_sql('Result', con=engine, if_exists='replace')

making_db()
app = Flask(__name__)
app.config['SECRET_KEY']='45919d4f6d40ac95fbf5d4c200b51be3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
db= SQLAlchemy(app)


from Sqlite_App import views
