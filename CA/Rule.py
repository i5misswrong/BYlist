import Block,Data

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


