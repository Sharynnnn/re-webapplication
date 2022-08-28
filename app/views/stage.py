from app.admin import *

'''
阶段管理
'''
# 列表
@admin.route('/stage_list')
def stage_list():
    tablename="event_stage_view"
    page = int(request.args.get('page'))
    rs = sel_data("*", tablename, "", f"order by StageDate LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", tablename)


    pages = math.ceil(len(rsall) / 10)
    return render_template("admin/stage/list.html",
        datas=rs, title="stages", tb=json.dumps(rs,cls=ComplexEncoder), rsall= json.dumps(rsall,cls=ComplexEncoder), pages=pages,
        cur=page, total= len(rsall)
                  )

#列表json
@admin.route('/stagelistjson',methods=['post'])
def stagelistjson():
    tablename = "event_stage_view"
    postdata = request.json
    page = int(postdata['page'])
    where=f"EventName LIKE '%{postdata['keywords']}%' or TeamName like '%{postdata['keywords']}%'"
    rs = sel_data("*", tablename,
                  where,
                  f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", tablename, where)
    pages = math.ceil(len(rsall) / 10)
    result = {'pages': pages, 'cur': int(page), 'total': len(rsall), "rs": rs, "rsall": rsall}

    return json.dumps(result,cls=ComplexEncoder), 200, {"Content-Type": "application/json"}

# 编辑
@admin.route('/stage_edit')
def stage_edit():
    tablename="event_stage"
    id = request.args.get('id')
    rs = sel_data("*", tablename, "StageID=" + id)
    datas=rs[0]
    datas["StageDate"]=str(datas["StageDate"])[:10]
    if datas["Qualifying"]==1:
        datas["Qualifying"]=True
    else:
        datas["Qualifying"]=False
    event=sel_data("EventID,EventName","events")
    return render_template("admin/stage/edit.html", datas=json.dumps(datas),event=event,title="edit stage")

# 增加
@admin.route('/stage_add')
def stage_add():
    event=sel_data("EventID,EventName","events")
    return render_template("admin/stage/add.html", title="add stage",event=event)

