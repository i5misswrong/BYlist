import Block,Data,random
def peopleGatherMove(p,d,allPeople):
    for eve in allPeople:
        if p.isMove==True and p.isCrowded==False and eve.isCrowded==False:
            if d==1 and p.x-1==eve.x and p.y-1==eve.y:
                p.isCrowded=True
                eve.isCrowded=True
                p.isMove=True
                eve.isMove=False
            elif d==2 and p.x==eve.x and p.y-1==eve.y:
                p.isCrowded=True
                eve.isCrowded=True
                p.isMove=True
                eve.isMove=False
            elif d==3 and p.x+1==eve.x and p.y+1==eve.y:
                p.isCrowded = True
                eve.isCrowded = True
                p.isMove=True
                eve.isMove=False
            elif d==4 and p.x-1==eve.x and p.y==eve.y:
                p.isCrowded = True
                eve.isCrowded = True
                p.isMove=True
                eve.isMove=False
            elif d==6 and p.x+1==eve.x and p.y==eve.y:
                p.isCrowded = True
                eve.isCrowded = True
                p.isMove=True
                eve.isMove=False
            elif d==7 and p.x-1==eve.x and p.y+1==eve.y:
                p.isCrowded = True
                eve.isCrowded = True
                p.isMove=True
                eve.isMove=False
            elif d==8 and p.x==eve.x and p.y+1==eve.y:
                p.isCrowded = True
                eve.isCrowded = True
                p.isMove=True
                eve.isMove=False
            elif d==9 and p.x+1==eve.x and p.y+1==eve.y:
                p.isCrowded = True
                eve.isCrowded = True
                p.isMove=True
                eve.isMove=False
def peopleScatterMove(p,d,allPeople):
    for volvo in allPeople:
        if p.x==volvo.x and p.y==volvo.y and p.isCrowded and volvo.isCrowded:#看两人是否在同一位置上
            if d!=5:                                                         #说明周围有可以移动的选择
                p.isCrowded=False
                volvo.isCrowded=False
                p.isMove=True
                volvo.isMove=True
            else:
                pass
        # if d==1 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==2 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==3 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==4 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==6 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==7 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==8 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
        # elif d==9 and p.isCrowded and volvo.isCrowded:
        #     p.isCrowded=False
        #     volvo.isCrowded=False
        #     p.isMove=True
        #     volvo.isMove=True
def PeopleMove(p,direction):
    if p.isMove:
        if direction==1:
            p.x=p.x-1
            p.y=p.y-1
        elif direction==2:
            p.y=p.y-1
        elif direction==3:
            p.x=p.x+1
            p.y=p.y-1
        elif direction==4:
            p.x=p.x-1
        elif direction==5:
            p.x=p.x
            p.y=p.y
        elif direction==6:
            p.x=p.x+1
        elif direction==7:
            p.x=p.x-1
            p.y=p.y+1
        elif direction==8:
            p.y=p.y+1
        elif direction==9:
            p.x=p.x+1
            p.y=p.y+1
    else:
        p.x = p.x
        p.y = p.y

# def checkoutPeople(p,allPeople):
#     if (p.x>=8 and p.x<=12) and p.y==Data.ROOM_N:
#         allPeople.remove(p)
#         a=[]

def checkoutPeople(p,allPeople):
    if (p.x>=18 and p.x<=22) and p.y>=Data.ROOM_N:
    # if p.x==20 and p.y>=Data.ROOM_N:
        allPeople.remove(p)
    # if p.x+2>Data.ROOM_M:
    #     return True

