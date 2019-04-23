import pymysql
con=pymysql.connect(host='localhost', user='root', password='1234', db='new_schema')
print(con)
try:
    with con.cursor() as cu:
        sql='drop new_schema'
        cu.execute(sql)
        con.commit()
    pass
finally:
    con.close()