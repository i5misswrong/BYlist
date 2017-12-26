import random
import Data,Block
import InitPeople
import math

def allIncome(self,p,allPeople):
    self.addIncome(p)
    self.wallIncome(p)
    self.distanceIncome(p)
    self.sortIncome(p)
    self.kindaIncome(p)
    self.kindbIncome(p)
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
    for i in p.kindaIncome.value():
        v4.append(i)
    for i in p.kindbIncome.value():
        v5.append(i)
    for i in p.jamIncome.value():
        v6.append(i)

def wallIncome(self,p):
    '''墙壁收益'''
    if p.x-1==0 and (p.y<8 or p.y>12):
        p.wallIncome[1]=-1000
        p.wallIncome[2]=-1000
        p.wallIncome[3]=-1000
    elif p.x+1==Data.ROOM_N:
        p.wallIncome[7]=-1000
        p.wallIncome[8]=-1000
        p.wallIncome[9]=-1000

    if p.y-1==0:
        p.wallIncome[1]=-1000
        p.wallIncome[4]=-1000
        p.wallIncome[7]=-1000
    elif p.y+1==Data.ROOM_M:
        p.wallIncome[3]=-1000
        p.wallIncome[6]=-1000
        p.wallIncome[9]=-1000

    '''出口收益'''
    if p.x-1==0 and (p.y>=8 and p.y<=12):
        p.wallIncome[2]=800
        if p.y>8:
            p.wallIncome[1]=800
        elif p.y<12:
            p.wallIncome[3]=800
        elif p.y>8 and p.y<12:
            p.wallIncome[1]=800
            p.wallIncome[3]=800
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

def randomIncome(self,p):
    '''计算随机方向收益'''
    for i in range(1,10):
        p.randomIncome[i]=random.random()





