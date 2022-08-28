import json
import math
from app.untils import ComplexEncoder
from flask import Blueprint, render_template, session, request

from mysql.mysqlldb import *
admin = Blueprint('admin',__name__)

@admin.route('/')
def login():  # put application's code here
    rs=sel_data("*","members","Type='user'")
    userlist = []
    for i in rs:
        userlist.append({"value":f"{i['FirstName']} {i['LastName']} "})
    return render_template('admin/login.html',userlist=userlist)

@admin.route('/index')
def index():
    return render_template('admin/index.html',title="Athlete Management System")

@admin.route('/welcome')
def welcome():
    if session['userinfo']['Type'] == "admin":
        count_event = sel_sql("SELECT COUNT(0) as num FROM Events")
        count_user = sel_sql("SELECT COUNT(0) as num FROM members")
        rs = [
            {'name': 'Events', 'num': count_event[0]['num']},
            {'name': 'Members', 'num': count_user[0]['num']}
        ]

        return render_template('admin/welcome.html', datas=rs)
    else:
        teamid=session['userinfo']['TeamID']
        memberid=session['userinfo']['MemberID']
        eventlist=sel_data("eventname","event_stage_view",f"PointsToQualify is null and NZTeam={teamid}","GROUP BY eventname")
        events=[]
        if len(eventlist)>0:
            for i in eventlist:
                item={}
                rs=sel_data("StageName,Location,StageDate","event_stage_view",f'EventName="{i["EventName"]}"',"order by StageDate")
                item["EventName"]=i["EventName"]
                item["data"]=rs
                events.append(item)
        result=[]
        rslist = sel_data("eventname", "event_stage_results_view", f"MemberID={memberid}",
                             "GROUP BY eventname")
        if len(rslist)>0:
            for i in rslist:
                item={}
                rs=sel_data("StageName,StageDate,PointsScored","event_stage_results_view",f'EventName="{i["EventName"]}" and MemberID={memberid}',"order by StageDate")
                item["EventName"]=i["EventName"]
                item["data"]=rs
                result.append(item)

        return render_template('admin/welcome.html',events=events,result=result)

