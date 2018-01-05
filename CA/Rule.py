import Block,Data
def PeopleTypeMove(p,d,allPeople):
    for eve in allPeople:
        if d==1 and p.x-1==eve.x and p.y-1==eve.y:
            p.isCrowded=True
            eve.isCrowded=True
        elif d==2 and p.x==eve.x and p.y-1==eve.y:
            p.isCrowded=True
            eve.isCrowded=True
        elif d==3 and p.x+1==eve.x and p.y+1==eve.y:
            p.isCrowded = True
            eve.isCrowded = True
        elif d==4 and p.x-1==eve.x and p.y==eve.y:
            p.isCrowded = True
            eve.isCrowded = True
        elif d==6 and p.x+1==eve.x and p.y==eve.y:
            p.isCrowded = True
            eve.isCrowded = True
        elif d==7 and p.x-1==eve.x and p.y+1==eve.y:
            p.isCrowded = True
            eve.isCrowded = True
        elif d==8 and p.x==eve.x and p.y+1==eve.y:
            p.isCrowded = True
            eve.isCrowded = True
        elif d==9 and p.x+1==eve.x and p.y+1==eve.y:
            p.isCrowded = True
            eve.isCrowded = True
def PeopleMove(p,direction):
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

# def checkoutPeople(p,allPeople):
#     if (p.x>=8 and p.x<=12) and p.y==Data.ROOM_N:
#         allPeople.remove(p)
#         a=[]

def checkoutPeople(p,allPeople):
    if (p.x>=18 and p.x<=22) and p.y==Data.ROOM_N:
        allPeople.remove(p)
    # if p.x+2>Data.ROOM_M:
    #     return True

