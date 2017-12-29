

def PeopleInCome(p,allPeople):
    d=6
    for pp in allPeople:
        if p.x+1==pp.x and p.y==pp.y:
            if pp.isCrow:
                d=5
            else:
                p.isCrow=True
                pp.isCrow=True
                d=6
    return d