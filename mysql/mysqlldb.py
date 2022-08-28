
from app import db

cursor=db.session

def dictfetchall(rs):
    "将游标返回的结果保存到一个字典对象中"
    rr = []
    for i in rs:
        rr.append(dict((zip(i.keys(), i))))
    return rr


# search
def sel_data(filed="*", tablename="", wheres="", other=""):

    if wheres=="":
        sqls='select {0} from {1} {2}'.format(filed,tablename,other)
    else:
        sqls='select {0} from {1} where {2} {3}'.format(filed,tablename,wheres,other)
    # print(sqls)
    cursor.execute(sqls)

    rs = dictfetchall(cursor.execute(sqls))

    return rs


# insert
def ins_data(tablename,dicts):

   # sqls="INSERT INTO {0} VALUES ({2})".format(tablename,values)
    col = ""
    val = ""
    for k, v in dicts.items():
        col += k + ","
        if type(v) == str:
            val += "'" + str(v) + "',"
        else:
            val += str(v) + ","

    sqls = "INSERT INTO {0} ({1}) VALUES ({2})".format(tablename, col[:-1], val[:-1])
    sqls=sqls.replace(",name",',`name`').replace(',enable',',`enable`')
    try:
        cursor.execute(sqls)
        rs=1
    except Exception as e:
        print(e)
        rs=0
    return rs


# update
def save_data(tablename,dicts,wheres):


    val = ""
    for k, v in dicts.items():
        if type(v) == str:
            val += k + "=" + "\"" + str(v) + "\","
        else:
            val += k + "=" + str(v) + ","

    sqls="UPDATE {0} SET {1} WHERE {2}".format(tablename,val[:-1],wheres)
    print(sqls)
    try:
        cursor.execute(sqls)
        rs = 1
    except Exception as e:
        rs = 0
    return rs


# delete
def del_data(tablename,wheres):
    sqls = "DELETE FROM {0} WHERE {1}".format(tablename,wheres)
    try:
        cursor.execute(sqls)
        rs = 1
    except Exception as e:
        rs = 0
    return rs


# search
def sel_sql(sqlstr):
    sqls = sqlstr
    rs=dictfetchall(cursor.execute(sqls))
    return rs


#get sql
def sel_field(tablename):
    sqls = "select * from {} limit 1".format(tablename)
    cursor.execute(sqls)
    desc = cursor.description
    result = []
    for i in desc:
        result.append(i[0])
    return result


#get table
def table_stru(tablename):
    sqls = "SELECT	column_name,data_type FROM information_schema.`COLUMNS` WHERE table_name = '{}' ORDER BY ordinal_position".format(tablename)
    cursor.execute(sqls)
    rs = {}
    for row in cursor.fetchall():
        rs[row[0]]=row[1]

    return rs