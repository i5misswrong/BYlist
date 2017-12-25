import InitPeople,Rule,Block,Data,DrawFirst

def run_f():
    allPeople=InitPeople.creatAppointPeo()
    while Data.flag:
        for p in allPeople:
            direction=6
            Rule.PeopleMove(p,direction)
        DrawFirst.drawPeople(allPeople)


if __name__=='__main__':
    run_f()