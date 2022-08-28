from app.admin import *

'''
用户管理
'''
# 帐号列表
@admin.route('/member_list')
def member_list():

    page = int(request.args.get('page'))

    rs = sel_data("*", "members", "Type !='admin'", f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", "members","Type !='admin'")


    pages = math.ceil(len(rsall) / 10)
    return render_template("admin/member/list.html",
        datas=rs, title="members", tb=json.dumps(rs,cls=ComplexEncoder), rsall= json.dumps(rsall,cls=ComplexEncoder), pages=pages,
        cur=page, total= len(rsall)
                  )

#帐号列表json
@admin.route('/memberlistjson',methods=['post'])
def memberlistjson():

    postdata = request.json
    page = int(postdata['page'])

    rs = sel_data("*", "members",
                  "(FirstName LIKE '%{0}%' or LastName LIKE '%{0}%') and Type !='admin' ".format(postdata['keywords']),
                  f"LIMIT {(page - 1) * 10},10")
    rsall = sel_data("*", "members", "(FirstName LIKE '%{0}%' or LastName LIKE '%{0}%') and Type !='admin' ".format(postdata['keywords']))

    pages = math.ceil(len(rsall) / 10)

    result = {'pages': pages, 'cur': int(page), 'total': len(rsall), "rs": rs, "rsall": rsall}

    return json.dumps(result,cls=ComplexEncoder), 200, {"Content-Type": "application/json"}

# 帐号编辑
@admin.route('/member_edit')
def member_edit():
    id = request.args.get('id')
    try:
        m=request.args.get('m')
    except:
        pass
    rs = sel_data("*", "members", "memberid=" + id)
    datas=rs[0]
    datas['Birthdate']=str(datas['Birthdate'])
    team = sel_data("*", "teams")
    if m:
        rs = sel_data("*", "members", f"MemberID ={id}")
        session['userinfo'] = rs[0]

    return render_template("admin/member/edit.html", datas=datas, team=team,title="edit member")

# 帐号增加
@admin.route('/member_add')
def member_add():
    team=sel_data("*","teams")
    return render_template("admin/member/add.html", title="add member",team=team)

