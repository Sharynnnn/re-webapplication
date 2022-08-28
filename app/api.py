import json

from flask import Blueprint, session,request
from app.untils import ComplexEncoder
from mysql.mysqlldb import *
api = Blueprint('api',__name__)

@api.route('/login', methods=['POST'])
def login():
    json_data = request.json
    username=json_data['username']
    if username=="admin":
        rs=sel_data("*","members","LastName='admin'")
        session['userinfo'] = rs[0]

    else:
        username=username.split(" ")
        rs=sel_data("*","members",f"FirstName ='{username[0]}' and LastName='{username[1]}'")
        session['userinfo']=rs[0]
    data = {
        'code': 1
    }
    response = json.dumps(data)
    return response, 200, {"Content-Type": "application/json"}

# search
@api.route('/select_data', methods=['GET','POST'])
def select_data():
    obj = request.json  # request.POST get post data
    parm=obj.split("|")

    rs = sel_data(parm[0],parm[1])

    if rs :
        data = {'code': 1, 'msg': '成功！','datas':json.dumps(rs,cls=ComplexEncoder)}
    else:
        data = {'code': -1, 'msg': '失败！'}
    return data, 200, {"Content-Type": "application/json"}



# add
@api.route('/add_one', methods=['POST'])
def add_one():
    obj = request.json  # get post data
    tablename = obj["tablename"]
    arr=obj["data"]

    key=["Birthdate","StageDate"]

    for i in key:
        if i in arr.keys():
            arr[i]=arr[i][:10]


    rs = ins_data(tablename,arr)

    if rs == 1:
        data = {'code': 1, 'msg': 'success！'}
    else:
        data = {'code': 0, 'msg': 'fail！'}
    return data, 200, {"Content-Type": "application/json"}


#delete
@api.route('/del_one', methods=['POST'])
def del_one():

    obj=request.json
    tablename = obj["tablename"]
    idname=obj['idname']
    id = obj["id"]

    n = del_data(tablename, "{}={}".format(idname, id))
    if n == 1:
        data = {'code': 1, 'msg': 'success！'}
    else:
        data = {'code': 0, 'msg': 'fail！'}
    return data, 200, {"Content-Type": "application/json"}

#modify
@api.route('/edit_one', methods=['POST'])
def edit_one():
    obj = request.json
    tablename = obj["tablename"]
    idname = obj['idname']
    id = obj["id"]
    data = obj["data"]
    del data[idname]
    key = ["Birthdate", "StageDate"]

    for i in key:
        if i in data.keys():
            data[i] = data[i][:10]
    print()
    try:
        n = save_data(tablename, data, f"{idname}={id}")
        result = {"code": n}
    except:
        result = {"code": 0}
    return result, 200, {"Content-Type": "application/json"}