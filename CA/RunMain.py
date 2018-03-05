import InitPeople,Rule,Data,DrawFirst,InCome,pymysql
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time,random

def run_f(case_s,location):
    '''此方法为运行方法，带相关参数的接受和返回'''
    '-----------------------初始设置(行人、静态场)-----------------------------'
    allPeople=InitPeople.creatAppointPeo()#初始化行人
    # allPeople=InitPeople.creatOnePeople()
    allTable=InitPeople.creatTable()#初始化障碍物
    if case_s==0:
        Data.STATIC_FIELD = Data.STATIC_FIELD1()  # 静态场的植入
    elif case_s==1:
        Data.STATIC_FIELD = Data.STATIC_FIELD2()  # 静态场的植入
    '-------------------------------------------------------------------------'
    # resultData=[]    #返回总列表
    # T=[] #时间
    # V=[] #速度
    # Q=[] #出口流量
    # S=[] #行人速度
    # Q.append(0)
    evac_time=0 #疏散时间

    while Data.flag:#循环开始
        # locomotive_num=0#本次时间步移动的人
        # static_num=0    #本次时间步静止的人
        # vector=0        #本次时间步行人速度
        random.shuffle(allPeople)
        for p in allPeople:
            d=0
            # if p.dbg==1:
            #     d = Rule.bottomMove2(p, d, allPeople)
            # else:
            if location==0:
                InCome.PeopleInCome(p, allPeople, allTable)
                d = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]
            elif location==1:
                if p.y<22:
                    d=Rule.bottomMove(p,d,allPeople)
                else:
                    InCome.PeopleInCome(p, allPeople, allTable)
                    d = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]
            # if d==5:
            #     static_num=static_num+1
            # else:
            #     locomotive_num=locomotive_num+1

            # if Rule.checkoutPeople(p):
            '--------------------------------行人移动规则---------------------------------------'
            Rule.peopleGatherMove(p, d, allPeople)     # 挤压
            Rule.peopleScatterMove(p,d,allPeople)      #挤压消除
            Rule.PeopleMove(p,d)                       #普通
            Rule.checkoutPeople(p,allPeople)           #移出系统
            # direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]
            # Rule.checkoutPeople(p,allPeople)
            # direction=8
            # Rule.PeopleMove(p,direction)
            # print(p.allIncomeBySort)
            # print(qq)
        evac_time=evac_time+1  # 疏散时间更新
        '---------------------------图像和即时数据-----------------------------------'
        DrawFirst.drawPeople(allPeople,allTable)
        print(len(allPeople))

        if len(allPeople)==0:
            # vector=1
            Data.flag=False
        # else:
        #     vector=locomotive_num/len(allPeople)
        # if vector>1:
        #     vector=1.0
        #
        # T.append(evac_time)#将疏散时间添加到T
        # S.append(len(allPeople))#将剩余行人添加到S
        # V.append(vector)#将行人速度添加到V


    # for i in range(len(S) - 1):#遍历行人
    #     quar = S[i] - S[i + 1]#出口流量=上一步的行人总数-下一步的行人总数
    #     Q.append(quar)#将出口流量添加到Q
    '''将各种参数返回列表'''
    return evac_time
    # resultData.append(case_s)
    # resultData.append(P)
    # resultData.append(R)
    # resultData.append(steps)
    # resultData.append(T)
    # resultData.append(S)
    # resultData.append(V)
    # resultData.append(Q)
def insertDB():
    connect = pymysql.connect(host='localhost', user='root', password='1234', db='people')
    print('connect')
    '''设置循环参数'''
    list_steps =[0,1,2,3]
    list_case=[0,1]  #静态场分类
    list_location=[0,1] #疏散策略分类  0代表普通  1代表下部
    try:
        with connect.cursor() as cursor:  # 打开游标
            for l_c in list_case:
                for l_s in list_steps:
                    for l_l in list_location:
                        evac_time=run_f(l_c,l_l)
                        # evac_time=100
                        # allData = []
                        # allData = run_f(l_s)
                        # '''接受参数'''
                        # case_s = allData[0]
                        # steps = allData[1]
                        # time_s = allData[2]
                        # veocity = allData[3]
                        # quantity = allData[4]
                        # print('当前case=',case_s,'---', '执行到第',steps,'步')
                        # Data.flag = True  # 设置循环标识符
                        '''设置sql语句'''
                        sql = 'insert into people.by_test (case_s,steps,evacuate_time,location) VALUES (%s,%s,%s,%s)'
                        # for i in range(len(time_s)):  # 循环将其写入数据库
                        cursor.execute(sql, [l_c,l_s,evac_time,l_l])
                        connect.commit()  # 数据库执行
                        Data.flag=True
                        # print("steps:",l_s,"---当前时间",evac_time)
    finally:  # 如果发生异常，关闭数据库
        connect.close()

if __name__=='__main__':
    # run_f()
    insertDB()