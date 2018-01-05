import random
import Data,Block,InitPeople
import InitPeople
import math

def PeopleInCome(p,allPeople,allTable):
    distanceInCome(p,allPeople)    #  距离收益
    tableInCome(p,allTable)        #  课桌收益
    wallInCome(p,allPeople)        #  墙壁收益
    exitInCome(p,allPeople)        #  出口收益
    addInCome(p, allPeople)        #  将收各益加起来
    sortDic(p)                     #  对各收益进行排序   #注意排列顺序
'''------------------------The Data Processing-----------------------------------------------'''
def addInCome(p,allPeople):
    v1=[]
    v2=[]
    v3=[]
    v4=[]
    v5=[]
    for i in p.distanceInCome.values():
        v1.append(i)
    for i in p.wallInCome.values():
        v2.append(i)
    for i in p.tableInCome.values():
        v3.append(i)
    for i in p.exitInCome.values():
        v4.append(i)
    for i in p.exitInCome.values():
        v5.append(i)
    income = list(map(lambda x,y,z,q,m: [x+y+z+q+m],v1,v2,v3,v4,v5))
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
    des=(math.sqrt((d_x-e_x)**2+(d_y-e_y)**2)*1000)
    if des==0:
        des=0.001
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

def tableInCome(p,allTable):
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


def wallInCome(p,allPeople):
    p.wallInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    if p.x==0 and p.y==0:
        p.wallInCome[1]=-1000
        p.wallInCome[2]=-1000
        p.wallInCome[3]=-1000
        p.wallInCome[4]=-1000
        p.wallInCome[7]=-1000
    elif p.x==0 and p.y==Data.ROOM_N:
        p.wallInCome[1]=-1000
        p.wallInCome[4]=-1000
        p.wallInCome[7]=-1000
        p.wallInCome[8]=-1000
        p.wallInCome[9]=-1000
    elif p.x==Data.ROOM_M and p.y==0:
        p.wallInCome[1]=-1000
        p.wallInCome[2]=-1000
        p.wallInCome[3]=-1000
        p.wallInCome[6]=-1000
        p.wallInCome[9]=-1000
    elif p.x==Data.ROOM_M and p.y==Data.ROOM_N:
        p.wallInCome[3]=-1000
        p.wallInCome[6]=-1000
        p.wallInCome[9]=-1000
        p.wallInCome[8]=-1000
        p.wallInCome[7]=-1000
    elif p.y==Data.ROOM_N:
        p.wallInCome[7]=-1000
        p.wallInCome[8]=-1000
        p.wallInCome[9]=-1000
    elif p.y==0:
        p.wallInCome[1]=-1000
        p.wallInCome[2]=-1000
        p.wallInCome[3]=-1000
    elif p.x==0:
        p.wallInCome[1]=-1000
        p.wallInCome[4]=-1000
        p.wallInCome[7]=-1000
    elif p.x==Data.ROOM_M:
        p.wallInCome[9]=-1000
        p.wallInCome[6]=-1000
        p.wallInCome[3]=-1000


def exitInCome(p,allPeople):
    p.exitInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
    if p.x==Data.EXIT_X and p.y==Data.EXIT_Y:
        p.exitInCome[8]=1500



#
# def crowdedInCome(p,allPeople):
#     p.crowdedInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
#     for person in allPeople:
#         if person.x-1==p.x and person.y-1==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[1]=-500
#                 else:
#                     p.crowdedInCome[1]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x==p.x and person.y-1==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[2]=-500
#                 else:
#                     p.crowdedInCome[2]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x+1==p.x and person.y-1==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[3]=-500
#                 else:
#                     p.crowdedInCome[3]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x-1==p.x and person.y==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[4]=-500
#                 else:
#                     p.crowdedInCome[4]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x+1==p.x and person.y==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[6]=-500
#                 else:
#                     p.crowdedInCome[6]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x-1==p.x and person.y+1==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[7]=-500
#                 else:
#                     p.crowdedInCome[7]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x==p.x and person.y+1==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[8]=-500
#                 else:
#                     p.crowdedInCome[8]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#         if person.x+1==p.x and person.y+1==p.y:
#             if person.type and p.type:
#                 if person.isCrowded and p.isCrowded:
#                     p.crowdedInCome[9]=-500
#                 else:
#                     p.crowdedInCome[9]=500
#                     person.isCrowded=True
#                     p.isCrowded=True
#
#


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
