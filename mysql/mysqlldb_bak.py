
from app import db



def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]


# search
def sel_data(filed="*", tablename="", wheres="", other=""):
    cursor = db.cursor()
    if wheres=="":
        sqls='select {0} from {1} {2}'.format(filed,tablename,other)
    else:
        sqls='select {0} from {1} where {2} {3}'.format(filed,tablename,wheres,other)

    cursor.execute(sqls)
    #rs = cursor.fetchall()
    rs = dictfetchall(cursor)
    cursor.close()
    return rs


# insert
def ins_data(tablename,dicts):
    cursor = db.cursor()
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

    cursor.close()
    return rs


# update
def save_data(tablename,dicts,wheres):
    cursor = db.cursor()
   # sqls="INSERT INTO {0} VALUES ({2})".format(tablename,values)
    val = ""
    for k, v in dicts.items():
        if type(v) == str:
            val += k + "=" + "'" + str(v) + "',"
        else:
            val += k + "=" + str(v) + ","

    sqls="UPDATE {0} SET {1} WHERE {2}".format(tablename,val[:-1],wheres)
    try:
        cursor.execute(sqls)
        rs = 1
    except Exception as e:
        rs = 0

    cursor.close()
    return rs


# delete
def del_data(tablename,wheres):
    cursor = db.cursor()
    sqls = "DELETE FROM {0} WHERE {1}".format(tablename,wheres)
    try:
        cursor.execute(sqls)
        rs = 1
    except Exception as e:
        rs = 0

    cursor.close()
    return rs


# search
def sel_sql(sqlstr):
    cursor = db.cursor()
    sqls = sqlstr
    cursor.execute(sqls)
    #rs = cursor.fetchall()
    rs=dictfetchall(cursor)
    cursor.close()
    return rs


#get sql
def sel_field(tablename):
    cursor = db.cursor()
    sqls = "select * from {} limit 1".format(tablename)
    cursor.execute(sqls)
    desc = cursor.description
    result = []
    for i in desc:
        result.append(i[0])
    cursor.close()
    return result


#get table
def table_stru(tablename):
    cursor = db.cursor()
    sqls = "SELECT	column_name,data_type FROM information_schema.`COLUMNS` WHERE table_name = '{}' ORDER BY ordinal_position".format(tablename)
    cursor.execute(sqls)
    rs = {}
    for row in cursor.fetchall():
        rs[row[0]]=row[1]
    cursor.close()
    return rs