import pymysql

connect = pymysql.connect(host='localhost', user='root', password='1234', db='people')

print(connect)
a=[0,1,2]
b=[111,222,333]

try:
    with connect.cursor() as cursor:
        sql='insert into people.test (density,case_s,time) values (%s,%s,%s)'
        for aa in range(3):
            cursor.execute(sql,[a[aa],b[aa]])
        # print(cursor.fetchall())
        connect.commit()

    pass
finally:
    connect.close()