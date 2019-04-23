import pymysql

connect=pymysql.connect(host='localhost',user='root',password='1234',db='pedestrian')
print('connect')

'''设置循环参数'''
list_case=[0,1]
list_steps=[0,1,2,3,4]


try:
    with connect.cursor() as cursor:  # 打开游标
        for l_c in list_case:
            for l_s in list_steps:
                allData=[]
                allData=run_f(steps)
                '''接受参数'''
                case_s=allData[0]
                steps = allData[1]
                time_s = allData[2]
                veocity = allData[3]
                quantity = allData[4]
                print('当前case=', case_s, '---','执行到第', steps, '步')
                Data.flag = True  # 设置循环标识符
                '''设置sql语句'''
                sql = 'insert into pedestrian.danger_one (case_s, P, R, steps, time_s, surplus, V, Q) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                for i in range(len(time_s)):  # 循环将其写入数据库
                    cursor.execute(sql, [case_s, steps, time_s[i], veocity[i], quantity[i]])
                connect.commit()  # 数据库执行



