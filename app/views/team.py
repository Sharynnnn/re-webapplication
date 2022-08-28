from app.admin import *


'''
队伍管理
'''
# 列表
@admin.route('/team_list')
def team_list():

    page = int(request.args.get('page'))

    rs = sel_data("*", "teams", "", f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", "teams")


    pages = math.ceil(len(rsall) / 10)
    return render_template("admin/team/list.html",
        datas=rs, title="teams", tb=json.dumps(rs,cls=ComplexEncoder), rsall= json.dumps(rsall,cls=ComplexEncoder), pages=pages,
        cur=page, total= len(rsall)
                  )

#列表json
@admin.route('/teamlistjson',methods=['post'])
def teamlistjson():

    postdata = request.json
    page = int(postdata['page'])

    rs = sel_data("*", "teams",
                  "(FirstName LIKE '%{0}%' or LastName LIKE '%{0}%') and Type !='admin' ".format(postdata['keywords']),
                  f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", "teams", "(FirstName LIKE '%{0}%' or LastName LIKE '%{0}%') and Type !='admin' ".format(postdata['keywords']))

    pages = math.ceil(len(rsall) / 10)

    result = {'pages': pages, 'cur': int(page), 'total': len(rsall), "rs": rs, "rsall": rsall}

    return json.dumps(result,cls=ComplexEncoder), 200, {"Content-Type": "application/json"}

# 编辑
@admin.route('/team_edit')
def team_edit():
    id = request.args.get('id')
    rs = sel_data("*", "teams", "TeamID=" + id)
    datas=rs[0]

    team = sel_data("*", "teams")
    return render_template("admin/team/edit.html", datas=datas, team=team,title="edit team")

# 增加
@admin.route('/team_add')
def team_add():
    team=sel_data("*","teams")
    return render_template("admin/team/add.html", title="add team",team=team)

