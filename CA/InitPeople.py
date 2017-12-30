import Block,Data,random
def creatAppointPeo():
    allPeople=[]
    # for i in Data.PEOPLE_NUMBER:
    #     ran = random.random(i)
    #     if ran>0.5:
    #         Block.type=1
    #     else:
    #         Block.type=2
    for l in range(6,38,2):
        for m in range(6,19):
            for n in range(22,36):
              p1=Block.Block(1)
              p2=Block.Block(1)
              p1.x=l
              p1.y=m
              p2.x=l
              p2.y=n
              p1.type=True
              p2.type=True
              allPeople.append(p1)
              allPeople.append(p2)
    return allPeople

def creatTable():
    allTable=[]
    for i in range(5,37,2):
        for j in range(6,19):
            for k in range(22,36):
              t1=Block.Block(10)
              t2=Block.Block(10)
              t1.x=i
              t1.y=j
              t2.x=i
              t2.y=k
              t1.type=True
              t2.type=True
              allTable.append(t1)
              allTable.append(t2)
    return allTable
# def creatWall():
#     allWall=[]
#     for i in range(40):
#         for ii in range(8):
#             D=[i,0]
#             U=[ii,0]
#             L=[0,i]
#             R=[Data.ROOM_M,i]