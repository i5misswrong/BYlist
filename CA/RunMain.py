import InitPeople,Rule,Data,DrawFirst,InCome
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time

def run_f():
    allPeople=InitPeople.creatAppointPeo()
    allTable=InitPeople.creatTable()
    print(len(allPeople))
    while Data.flag:
        for p in allPeople:


            d=InCome.PeopleInCome(p,allPeople)

            d = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]

            # if Rule.checkoutPeople(p):


            Rule.PeopleMove(p,d)

            # direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]


            # Rule.checkoutPeople(p,allPeople)
            # direction=8
            # Rule.PeopleMove(p,direction)
            # print(p.allIncomeBySort)
            # print(qq)
        DrawFirst.drawPeople(allPeople,allTable)





if __name__=='__main__':
    run_f()