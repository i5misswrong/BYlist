import InitPeople,Rule,Data,DrawFirst,InCome
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time,random

def run_f():
    allPeople=InitPeople.creatAppointPeo()
    # allPeople=InitPeople.creatOnePeople()
    print(len(allPeople))
    allTable=InitPeople.creatTable()
    while Data.flag:
        random.shuffle(allPeople)
        for p in allPeople:
            d=InCome.PeopleInCome(p,allPeople,allTable)
            d = max(p.allInComeBySort.items(), key=lambda x: x[1])[0]
            # if Rule.checkoutPeople(p):
            Rule.PeopleTypeMove(p,d,allPeople)
            Rule.PeopleMove(p,d)
            Rule.checkoutPeople(p,allPeople)
            # direction = max(p.allIncomeBySort.items(), key=lambda x: x[1])[0]
            # Rule.checkoutPeople(p,allPeople)
            # direction=8
            # Rule.PeopleMove(p,direction)
            # print(p.allIncomeBySort)
            # print(qq)
        DrawFirst.drawPeople(allPeople,allTable)
        print(len(allPeople))
        if len(allPeople)==0:
            Data.flag=False
if __name__=='__main__':
    run_f()