import InitPeople,Rule,Block,Data,DrawFirst,InCome

def run_f():
    allPeople=InitPeople.creatAppointPeo()
    while Data.flag:
        for p in allPeople:
<<<<<<< HEAD
            Income.outDirection(p,allPeople)
            direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]
=======
            d=InCome.PeopleInCome(p,allPeople)
            if Rule.checkoutPeople(p):
                d=5

            Rule.PeopleMove(p,d)
            # direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]
>>>>>>> 6371ca470c6b48a96c34617216dbb0bf28a6c9ed

            # Rule.checkoutPeople(p,allPeople)
            # direction=8
            # Rule.PeopleMove(p,direction)
            # print(p.allIncomeBySort)
        DrawFirst.drawPeople(allPeople)


if __name__=='__main__':
    run_f()