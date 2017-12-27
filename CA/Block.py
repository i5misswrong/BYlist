class Block():
    def __init__(self,logo=0):
        self.logo=logo
        self.x=0
        self.y=0
        self.nextCrowded={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.type=False
        self.allInComeBySort={}# 排序后的总收益
        self.randomIncome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.allIncome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.wallIncome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.distanceIncome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
