import random
import Data,Block,InitPeople
import InitPeople
import math

def PeopleInCome(p,allPeople,allTable):
    distanceInCome(p,allPeople)    #  距离收益
    tableInCome(p,allTable)        #  课桌收益
    wallInCome(p,allPeople)        #  墙壁收益
    exitInCome(p,allPeople)        #  出口收益
    staticfieldInCome(p,allPeople) #  静态场收益
    jamInCome(p,allPeople)         #  拥挤收益
    addInCome(p, allPeople)        #  将收各益加起来
    sortDic(p)                     #  对各收益进行排序   #注意排列顺序
'''------------------------The Data Processing-----------------------------------------------'''
def addInCome(p,allPeople):
    v1=[]
    v2=[]
    v3=[]
    v4=[]
    v5=[]
    v6=[]
    v7=[]
    for i in p.distanceInCome.values():
        v1.append(i)
    for i in p.wallInCome.values():
        v2.append(i)
    for i in p.tableInCome.values():
        v3.append(i)
    for i in p.exitInCome.values():
        v4.append(i)
    for i in p.crowdedInCome.values():
        v5.append(i)
    for i in p.jamInCome.values():
        v6.append(i)
    for i in p.staticfieldInCome.values():
        v7.append(i)
    income = list(map(lambda x,y,z,q,m,n,o: [x+y+z+q+m+n+o],v1,v2,v3,v4,v5,v6,v7))
    for key in p.allInCome:
        p.allInCome[key] = income[key - 1][0]
def sortDic(p):
    k=[]
    v=[]
    dic = sorted(p.allInCome.items(), key=lambda d: d[1])
    for i in dic:
        k.append(i[0])
        v.append(i[1])
    fin=dict(map(lambda x,y:[x,y],k,v))
    p.allInComeBySort=fin
'''-----------------------The calculation of InCome-------------------------------------------'''
def distanceFormula(d_x,d_y,e_x,e_y):            #距离公式
    des=(math.sqrt((d_x-e_x)**2+(d_y-e_y)**2)*0.00001)
    if des==0:
        des=0.00001
    return 1/des

def distanceInCome(p,allPeople):                 #计算距离收益
    p.distanceInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    p.distanceInCome[1]=distanceFormula(p.x-1,p.y-1,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[2]=distanceFormula(p.x,p.y-1,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[3]=distanceFormula(p.x+1,p.y-1,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[4]=distanceFormula(p.x-1,p.y,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[5]=distanceFormula(p.x,p.y,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[6]=distanceFormula(p.x+1,p.y,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[7]=distanceFormula(p.x-1,p.y+1,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[8]=distanceFormula(p.x,p.y+1,Data.EXIT_X,Data.EXIT_Y)
    p.distanceInCome[9]=distanceFormula(p.x+1,p.y+1,Data.EXIT_X,Data.EXIT_Y)

def tableInCome(p,allTable):                    #桌椅收益
    p.tableInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    for tab in allTable:
        if p.x-1==tab.x and p.y-1==tab.y:
            p.tableInCome[1]=-1000
        elif p.x==tab.x and p.y-1==tab.y:
            p.tableInCome[2]=-1000
        elif p.x+1==tab.x and p.y-1==tab.y:
            p.tableInCome[3]=-1000
        elif p.x-1==tab.x and p.y==tab.y:
            p.tableInCome[4]=-1000
        elif p.x==tab.x and p.y==tab.y:
            p.tableInCome[5]=-1000
        elif p.x+1==tab.x and p.y==tab.y:
            p.tableInCome[6]=-1000
        elif p.x-1==tab.x and p.y+1==tab.y:
            p.tableInCome[7]=-1000
        elif p.x==tab.x and p.y+1==tab.y:
            p.tableInCome[8]=-1000
        elif p.x+1==tab.x and p.y+1==tab.y:
            p.tableInCome[9]=-1000


def wallInCome(p,allPeople):                       #墙壁收益
    p.wallInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    if p.x==1 and p.y==1:
        p.wallInCome[1]=-100000
        p.wallInCome[2]=-100000
        p.wallInCome[3]=-100000
        p.wallInCome[4]=-100000
        p.wallInCome[7]=-100000
    elif p.x==1 and p.y==Data.ROOM_N-1:
        p.wallInCome[1]=-100000
        p.wallInCome[4]=-100000
        p.wallInCome[7]=-100000
        p.wallInCome[8]=-100000
        p.wallInCome[9]=-100000
    elif p.x==Data.ROOM_M-1 and p.y==1:
        p.wallInCome[1]=-100000
        p.wallInCome[2]=-100000
        p.wallInCome[3]=-100000
        p.wallInCome[6]=-100000
        p.wallInCome[9]=-100000
    elif p.x==Data.ROOM_M-1 and p.y==Data.ROOM_N-1:
        p.wallInCome[3]=-100000
        p.wallInCome[6]=-100000
        p.wallInCome[9]=-100000
        p.wallInCome[8]=-100000
        p.wallInCome[7]=-100000
    elif p.y==Data.ROOM_N-1:
        p.wallInCome[7]=-100000
        p.wallInCome[8]=-100000
        p.wallInCome[9]=-100000
    elif p.y==1:
        p.wallInCome[1]=-100000
        p.wallInCome[2]=-100000
        p.wallInCome[3]=-100000
    elif p.x==1:
        p.wallInCome[1]=-100000
        p.wallInCome[4]=-100000
        p.wallInCome[7]=-100000
    elif p.x==Data.ROOM_M-1:
        p.wallInCome[9]=-100000
        p.wallInCome[6]=-100000
        p.wallInCome[3]=-100000


def exitInCome(p,allPeople):                      #出口收益
    p.exitInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    # if p.x==Data.EXIT_X and p.y==Data.EXIT_Y:
    #     p.exitInCome[8]=1500
    # if p.x==Data.EXIT_X and p.y+1==Data.EXIT_Y:
    #     p.exitInCome[8]=10000
    if p.x>=18 and p.x<=22 and p.y+1==Data.EXIT_Y:
        p.exitInCome[7]=9000
        p.exitInCome[8]=10000
        p.exitInCome[9]=9000



def crowdedInCome(p,allPeople):                   #拥挤收益（行人拥挤时isCrowded和type的变化）
    p.crowdedInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    for person in allPeople:
        if p.x-1==person.x and p.y-1==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[1]=-500
                else:
                    p.crowdedInCome[1]=500
        if p.x==person.x and p.y-1==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[2]=-500
                else:
                    p.crowdedInCome[2]=500
        if p.x+1==person.x and p.y-1==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[3]=-500
                else:
                    p.crowdedInCome[3]=500
        if p.x-1==person.x and p.y==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[4]=-500
                else:
                    p.crowdedInCome[4]=500
        if p.x+1==person.x and p.y==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[6]=-500
                else:
                    p.crowdedInCome[6]=500
        if p.x-1==person.x and p.y+1==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[7]=-500
                else:
                    p.crowdedInCome[7]=500
        if person.x==p.x and person.y+1==p.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[8]=-500
                else:
                    p.crowdedInCome[8]=500
        if p.x+1==person.x and p.y+1==person.y:
            if person.type and p.type:
                if person.isCrowded and p.isCrowded:
                    p.crowdedInCome[9]=-500
                else:
                    p.crowdedInCome[9]=500

def jamInCome(p,allPeople):                    #拥挤收益（周围拥挤元胞的影响）
    p.jamInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    for p1 in allPeople:
        if 0<=p.y<=35 and 0<=p1.y<=35 and \
                (p1.x==p.x-1 and p1.y==p.y+1) or (p1.x==p.x and p1.y==p.y+1)\
                or (p1.x==p.x+1 and p1.y==p.y+1) and p1.isCrowded:
            p.jamInCome[1]=-1000
            p.jamInCome[2]=-1000
            p.jamInCome[3]=-1000
            p.jamInCome[4]=-1000
            p.jamInCome[5]=500
            p.jamInCome[6]=-1000
            p.jamInCome[7]=-1000
            p.jamInCome[8]=-1000
            p.jamInCome[9]=-1000

def staticfieldInCome(p,allPeople):            #静态场收益
    p.staticfieldInCome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    if p.x<=38 and p.x>=2 and p.y>=2 and p.y<=38:
        p.staticfieldInCome[1]=Data.STATIC_FIELD[p.x-1][p.y-1]
        p.staticfieldInCome[2]=Data.STATIC_FIELD[p.x][p.y-1]
        p.staticfieldInCome[3]=Data.STATIC_FIELD[p.x+1][p.y-1]
        p.staticfieldInCome[4]=Data.STATIC_FIELD[p.x-1][p.y]
        p.staticfieldInCome[5]=Data.STATIC_FIELD[p.x][p.y]
        p.staticfieldInCome[6]=Data.STATIC_FIELD[p.x+1][p.y]
        p.staticfieldInCome[7]=Data.STATIC_FIELD[p.x-1][p.y+1]
        p.staticfieldInCome[8]=Data.STATIC_FIELD[p.x][p.y+1]
        p.staticfieldInCome[9]=Data.STATIC_FIELD[p.x+1][p.y+1]
    else:
        pass



#'''拥挤雏形'''
#     d=6
#     for pp in allPeople:
#         if p.x+1==pp.x and p.y==pp.y:
#             if pp.isCrow:
#                 d=5
#             else:
#                 p.isCrow=True
#                 pp.isCrow=True
#                 d=6
#     return d
