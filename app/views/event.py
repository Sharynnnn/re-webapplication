from app.admin import *

'''
事件管理
'''
# 列表
@admin.route('/event_list')
def event_list():
    tablename="events_view"
    page = int(request.args.get('page'))
    rs = sel_data("*", tablename, "", f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", tablename)


    pages = math.ceil(len(rsall) / 10)
    return render_template("admin/event/list.html",
        datas=rs, title="events", tb=json.dumps(rs,cls=ComplexEncoder), rsall= json.dumps(rsall,cls=ComplexEncoder), pages=pages,
        cur=page, total= len(rsall)
                  )

#列表json
@admin.route('/eventlistjson',methods=['post'])
def eventlistjson():
    tablename = "events_view"
    postdata = request.json
    page = int(postdata['page'])
    where=f"EventName LIKE '%{postdata['keywords']}%'"
    rs = sel_data("*", tablename,
                  where,
                  f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", tablename, where)
    pages = math.ceil(len(rsall) / 10)
    result = {'pages': pages, 'cur': int(page), 'total': len(rsall), "rs": rs, "rsall": rsall}

    return json.dumps(result,cls=ComplexEncoder), 200, {"Content-Type": "application/json"}

# 编辑
@admin.route('/event_edit')
def event_edit():
    tablename="events"
    id = request.args.get('id')
    rs = sel_data("*", tablename, "EventID=" + id)
    datas=rs[0]
    team = sel_data("*", "teams")
    return render_template("admin/event/edit.html", datas=datas, team=team,title="edit event")

# 增加
@admin.route('/event_add')
def event_add():
    team=sel_data("*","teams")
    return render_template("admin/event/add.html", title="add event",team=team)

