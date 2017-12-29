import InitPeople,Rule,Block,Data,DrawFirst,Income

def run_f():
    allPeople=InitPeople.creatAppointPeo()
    while Data.flag:
        for p in allPeople:
            Income.outDirection(p,allPeople)
            direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]

            # Rule.checkoutPeople(p,allPeople)
            # direction=8
            Rule.PeopleMove(p,direction)
            # print(p.allIncomeBySort)
        DrawFirst.drawPeople(allPeople)


if __name__=='__main__':
    run_f()