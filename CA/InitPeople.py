import Block
def creatAppointPeo():
    allPeople=[]

    b1=Block.Block(1)
    b1.x=3
    b1.y=5
    b1.type=True
    allPeople.append(b1)

    b2=Block.Block(1)
    b2.x=4
    b2.y=5
    b2.type=False
    allPeople.append(b2)

    b3 = Block.Block(1)
    b3.x = 10
    b3.y = 10
    b3.type = True
    allPeople.append(b3)

    return allPeople