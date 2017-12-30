import random
import Data,Block,InitPeople
import InitPeople
import math

def PeopleInCome(p,allPeople):
    isdistanceIncome(p,allPeople)


def isdistanceIncome(p,allPeople):
        xexit=20
        yexit=Data.ROOM_N
        # for peo in allPeople:
            # p.nextCrowded = {1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7: 0.0,8:0.0,9: 0.0}
            # if p.x - 1 == peo.x and p.y - 1 == peo.y:
            #        p.nextCrowded[1] =-1000
            # elif p.x - 1 == peo.x:
            #        p.nextCrowded[4] =-1000
            # elif p.x - 1 == peo.x and p.y + 1 == peo.y:
            #        p.nextCrowded[7] =-1000
            # elif p.y - 1 == peo.y:
            #        p.nextCrowded[2] =-1000
            # elif p.y + 1 == peo.y:
            #        p.nextCrowded[8] =-1000
            # elif p.x + 1 == peo.x and p.y - 1 == peo.y:
            #        p.nextCrowded[3] =-1000
            # elif p.x + 1 == peo.x:
            #        p.nextCrowded[6] =-1000
            # elif p.x + 1 == peo.x and p.y + 1 == peo.y:
            #        p.nextCrowded[9] =-1000
            # else:
        if p.x>=1 and p.x<=(Data.ROOM_N-1) and p.y>=1 and p.y<=(Data.ROOM_M-1):
                   p.distanceIncome[1]=math.sqrt((p.x-1-xexit)**2+(p.y-1-yexit)**2)
                   p.distanceIncome[2]=math.sqrt((p.x-1-xexit)**2+(p.y-yexit)**2)
                   p.distanceIncome[3]=math.sqrt((p.x-1-xexit)**2+(p.y+1-yexit)**2)
                   p.distanceIncome[4]=math.sqrt((p.x-xexit)**2+(p.y-1-yexit)**2)
                   p.distanceIncome[5]=math.sqrt((p.x-xexit)**2+(p.y-yexit)**2)
                   p.distanceIncome[6]=math.sqrt((p.x-xexit)**2+(p.y+1-yexit)**2)
                   p.distanceIncome[7]=math.sqrt((p.x+1-xexit)**2+(p.y-1-yexit)**2)
                   p.distanceIncome[8]=math.sqrt((p.x+1-xexit)**2+(p.y-yexit)**2)
                   p.distanceIncome[9]=math.sqrt((p.x+1-xexit)**2+(p.y+1-yexit)**2)
        else:
                   pass




    # '''拥挤雏形'''
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
