import Block,Data,random
def creatAppointPeo():
    allPeople=[]
    # for i in Data.PEOPLE_NUMBER:
    #     ran = random.random(i)
    #     if ran>0.5:
    #         Block.type=1
    #     else:
    #         Block.type=2

    b1=Block.Block(1)
    b1.x=10
    b1.y=8
    b1.type=True
    allPeople.append(b1)

    b2=Block.Block(1)
    b2.x=10
    b2.y=9
    b2.type=False
    allPeople.append(b2)

    b3 = Block.Block(1)
    b3.x = 10
    b3.y = 10
    b3.type = True
    allPeople.append(b3)
    return allPeople

# def creatWall():
#     allWall=[]
#     for i in range(40):
#         for ii in range(8):
#             D=[i,0]
#             U=[ii,0]
#             L=[0,i]
#             R=[Data.ROOM_M,i]