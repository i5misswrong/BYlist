import InitPeople,Rule,Data,DrawFirst,InCome,pymysql
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time,random

def run_f(steps):
    allPeople=InitPeople.creatAppointPeo()#初始化行人
    # allPeople=InitPeople.creatOnePeople()
    print(len(allPeople))
    allTable=InitPeople.creatTable()#初始化障碍物
    Data.STATIC_FIELD=Data.STATIC_FIELD()#静态场的植入
    '-------------------------------------------------------------------------'
    resultData=[]             #返回总列表
    T=[] #时间
    V=[] #速度
    Q=[] #出口流量
    S=[] #行人速度
    Q.append(0)

    evac_time=0 #疏散时间

    while Data.flag:#循环开始
        locomotive_num=0#本次时间步移动的人
        static_num=0    #本次时间步静止的人
        vector=0        #本次时间步行人速度
        random.shuffle(allPeople)
        for p in allPeople:
            d=InCome.PeopleInCome(p,allPeople,allTable)
            d = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]
            if d==5:
                static_num=static_num+1
            else:
                locomotive_num=locomotive_num+1


            # if Rule.checkoutPeople(p):
            Rule.peopleGatherMove(p, d, allPeople)     # 挤压
            Rule.peopleScatterMove(p,d,allPeople)      #挤压消除
            Rule.PeopleMove(p,d)                     #普通
            Rule.checkoutPeople(p,allPeople)         #移出系统
            # direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]
            # Rule.checkoutPeople(p,allPeople)
            # direction=8
            # Rule.PeopleMove(p,direction)
            # print(p.allIncomeBySort)
            # print(qq)
        DrawFirst.drawPeople(allPeople,allTable)
        print(len(allPeople))
        if len(allPeople)==0:
            vector=1
            Data.flag=False
        else:
            vector=locomotive_num/len(allPeople)
        if vector>1:
            vector=1.0

        T.append(evac_time)#将疏散时间添加到T
        S.append(len(allPeople))#将剩余行人添加到S
        V.append(vector)#将行人速度添加到V

        evac_time=evac_time+1 #疏散时间更新

    for i in range(len(S) - 1):#遍历行人
        quar = S[i] - S[i + 1]#出口流量=上一步的行人总数-下一步的行人总数
        Q.append(quar)#将出口流量添加到Q
    '''将各种参数返回列表'''
    # resultData.append(case_s)
    # resultData.append(P)
    # resultData.append(R)
    resultData.append(steps)
    resultData.append(T)
    resultData.append(S)
    resultData.append(V)
    resultData.append(Q)

if __name__=='__main__':
    connect = pymysql.connect(host='3306', user='root', password='1234', db='pedestrian')
    print('connect')

    '''设置循环参数'''
    list_case = [0, 1]
    list_steps = [0, 1, 2, 3, 4]

    try:
        with connect.cursor() as cursor:  # 打开游标
            for l_c in list_case:
                for l_s in list_steps:
                    allData = []
                    allData = run_f(l_s)
                    '''接受参数'''
                    case_s = allData[0]
                    steps = allData[1]
                    time_s = allData[2]
                    veocity = allData[3]
                    quantity = allData[4]
                    print('当前case=',case_s,'---', '执行到第',steps,'步')
                    Data.flag = True  # 设置循环标识符
                    '''设置sql语句'''
                    sql = 'insert into pedestrian.danger_one (case_s,steps, time_s) VALUES (%s,%s,%s)'
                    for i in range(len(time_s)):  # 循环将其写入数据库
                        cursor.execute(sql, [case_s, steps, time_s[i], veocity[i], quantity[i]])
                    connect.commit()  # 数据库执行
    finally:  # 如果发生异常，关闭数据库
        connect.close()