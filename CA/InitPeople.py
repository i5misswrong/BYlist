import Block,Data,random

def creatAppointPeo():
    allPeople=[]
      # for exm in range(1,416):
      #     rand=random(exm)
      #     if rand>0.5:
      #         pass
      #     else:
      #         pass
    for l in range(6,38,2):
        for m in range(6,19):
            # n=range(22,36)
            p1=Block.Block(1)
            p1.x=l
            p1.y=m
            p1.type=True
            allPeople.append(p1)
        for n in range(22,35):
            p1=Block.Block(1)
            p1.x=l
            p1.y=n
            p1.type=True
            allPeople.append(p1)
    return allPeople

def creatOnePeople():
    allPeople=[]
    p1=Block.Block(1)
    p1.x=20
    p1.y=30
    p1.type=True
    p1.isCrowded=False
    allPeople.append(p1)
    return allPeople

def creatTable():
    allTable=[]
    for i in range(5,37,2):
        for j in range(6,19):
            t1=Block.Block(10)
            t1.x=i
            t1.y=j
            t1.type=True
            allTable.append(t1)
        for k in range(22, 35):
            t1 = Block.Block(10)
            t1.x = i
            t1.y = k
            t1.type = True
            allTable.append(t1)
    return allTable
# def creatWall():
#     allWall=[]
#     for i in range(40):
#         for ii in range(8):
#             D=[i,0]
#             U=[ii,0]
#             L=[0,i]
#             R=[Data.ROOM_M,i]