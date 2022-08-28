from app.admin import *

'''
成绩管理
'''
# 列表
@admin.route('/result_list')
def result_list():
    tablename="event_stage_results_view"
    page = int(request.args.get('page'))
    rs = sel_data("*", tablename, "", f"order by StageDate LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", tablename)


    pages = math.ceil(len(rsall) / 10)
    return render_template("admin/results/list.html",
        datas=rs, title="results", tb=json.dumps(rs,cls=ComplexEncoder), rsall= json.dumps(rsall,cls=ComplexEncoder), pages=pages,
        cur=page, total= len(rsall)
                  )

#列表json
@admin.route('/resultlistjson',methods=['post'])
def resultlistjson():
    tablename = "event_stage_results_view"
    postdata = request.json
    page = int(postdata['page'])
    where=f"EventName LIKE '%{postdata['keywords']}%' or TeamName like '%{postdata['keywords']}%' or Name like '%{postdata['keywords']}%'"
    rs = sel_data("*", tablename,
                  where,
                  f"order by StageDate LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", tablename, where)
    pages = math.ceil(len(rsall) / 10)
    result = {'pages': pages, 'cur': int(page), 'total': len(rsall), "rs": rs, "rsall": rsall}

    return json.dumps(result,cls=ComplexEncoder), 200, {"Content-Type": "application/json"}

# 编辑
@admin.route('/result_edit')
def result_edit():
    tablename="event_stage_results"
    id = request.args.get('id')
    rs = sel_data("*", tablename, "ResultID=" + id)
    datas=rs[0]

    if datas["Position"] is None:
        datas["Position"]=""

    stageview = sel_data("StageID,CONCAT(EventName,' ',StageName,' ',StageDate) as Sname", "event_stage_view")
    member = sel_data("MemberID,CONCAT(FirstName,' ',LastName) AS Name", "members", "type != 'admin'")
    return render_template("admin/results/edit.html", datas=datas,stageview=stageview,member=member,title="edit result")

# 增加
@admin.route('/result_add')
def result_add():
    stageview=sel_data("StageID,CONCAT(EventName,' ',StageName,' ',StageDate) as Sname","event_stage_view")
    member = sel_data("MemberID,CONCAT(FirstName,' ',LastName) AS Name", "members","type != 'admin'")

    return render_template("admin/results/add.html", title="add result",stageview=stageview,member=member)

