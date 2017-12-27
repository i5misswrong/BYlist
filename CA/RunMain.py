import InitPeople,Rule,Block,Data,DrawFirst,Income

def run_f():
    allPeople=InitPeople.creatAppointPeo()
    while Data.flag:
        for p in allPeople:
            # Income.addIncome(p, allPeople)
            direction=8
            Rule.PeopleMove(p,direction)
        DrawFirst.drawPeople(allPeople)


if __name__=='__main__':
    run_f()