import random
import Data,Block
import InitPeople
import math

def allIncome(self,p,allPeople):
    self.addIncome(p)
    self.wallIncome(p)
    self.distanceIncome(p)
    self.sortDic(p)
    self.kindIncome(p)
    self.isnextCrowded(p,allPeople)
    self.jamIncome(p)

def addIncome(self,p):
    v1=[]
    v2=[]
    v3=[]
    v4=[]
    v5=[]
    v6=[]
    '''计算每个收益将其存入v1,v2,......中'''
    for i in p.addIncome.value():
        v1.append(i)
    for i in p.wallIncome.value():
        v2.append(i)
    for i in p.distanceIncome.value():
        v3.append(i)
    for i in p.kindIncome.value():
        v4.append(i)
    for i in p.nextCrowded.value():
        v5.append(i)
    for i in p.jamIncome.value():
        v6.append(i)

    income=list(map(lambda x,y,z,q:[x + y + z + q],v1,v2,v3,v4))
def sortDic(self,p):
    '''对字典的值进行排序'''
    dic=sorted(p.allInCome.items(),key=lambda d:d[1],reverse=True)
    '''由于dic的type为 ([],[],[],[])需要将其转换为字典'''
    k=[]  #存放key的列表
    v=[]  #存放vule的列表
    for i in dic:  #遍历dic
        k.append(i[0])  #将key存入
        v.append(i[1])  #将value存入
    fin = dict(map(lambda x,y:[x, y],k,v))  #转化为字典
    p.allInComeBySort=fin  #将其存入p

'''---------------------------------------------------------------------------------------------'''
def wallIncome(self,p):
    '''墙壁收益'''
    if p.x-1==0:
        p.wallIncome[1]=-1000
        p.wallIncome[4]=-1000
        p.wallIncome[7]=-1000
    elif p.x+1==Data.ROOM_M:
        p.wallIncome[3]=-1000
        p.wallIncome[6]=-1000
        p.wallIncome[9]=-1000

    if p.y-1==0:
        p.wallIncome[1]=-1000
        p.wallIncome[2]=-1000
        p.wallIncome[3]=-1000
    elif p.y+1==Data.ROOM_N  and (p.x<8 or p.x>12):
        p.wallIncome[7]=-1000
        p.wallIncome[8]=-1000
        p.wallIncome[9]=-1000

    '''出口收益'''
    if p.y+1==Data.ROOM_N and (p.x>=8 and p.x<=12):
        p.wallIncome[8]=800
        if p.x>8:
            p.wallIncome[7]=800
        elif p.x<12:
            p.wallIncome[9]=800
        elif p.x>8 and p.x<12:
            p.wallIncome[7]=800
            p.wallIncome[9]=800
# def distanceIncome(self,p):
#     p_x=p.x
#     p_y=p.y
#     xexit=0
#     yexit=10
#     if p.x>=1 and p.x<=(Data.ROOM_N-1) and p.y>=1 and p.y<=(Data.ROOM_M-1):
        # p.distanceIncome[1]=math.sqrt((p_x-1-xexit)**2+(p_y-1-yexit)**2)
        # p.distanceIncome[2]=math.sqrt((p_x-1-xexit)**2+(p_y-yexit)**2)
        # p.distanceIncome[3]=math.sqrt((p_x-1-xexit)**2+(p_y+1-yexit)**2)
        # p.distanceIncome[4]=math.sqrt((p_x-xexit)**2+(p_y-1-yexit)**2)
        # p.distanceIncome[5]=math.sqrt((p_x-xexit)**2+(p_y-yexit)**2)
        # p.distanceIncome[6]=math.sqrt((p_x-xexit)**2+(p_y+1-yexit)**2)
        # p.distanceIncome[7]=math.sqrt((p_x+1-xexit)**2+(p_y-1-yexit)**2)
        # p.distanceIncome[8]=math.sqrt((p_x+1-xexit)**2+(p_y-yexit)**2)
        # p.distanceIncome[9]=math.sqrt((p_x+1-xexit)**2+(p_y+1-yexit)**2)

# def randomIncome(self,p):
#     '''计算随机方向收益'''
#     for i in range(1,10):
#         p.randomIncome[i]=random.random()

def isnextCrowded(self,p,allPeople):
    for peo in allPeople:
        p.nextCrowded={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        if p.x-1==peo.x and p.y-1==peo.y:
            p.nextCrowded[1]=1000
        elif p.x-1==peo.x:
            p.nextCrowded[4]=1000
        elif p.x-1==peo.x and p.y+1==peo.y:
            p.nextCrowded[7]=1000
        elif p.y-1==peo.y:
            p.nextCrowded[2]=1000
        elif p.y+1==peo.y:
            p.nextCrowded[8]=1000
        elif p.x+1==peo.x and p.y-1==peo.y:
            p.nextCrowded[3]=1000
        elif p.x+1==peo.x:
            p.nextCrowded[6]=1000
        elif p.x+1==peo.x and p.y+1==peo.y:
            p.nextCrowded[9]=1000










