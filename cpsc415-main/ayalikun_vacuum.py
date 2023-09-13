from vacuum import VacuumAgent
import random
import uuid 

class AyalikunVacuumAgent(VacuumAgent):
    #'Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp'
    def __init__(self):
        super().__init__()
        #creating a list where I will be adding dictionary
        self.listOdDic = []
    def program(self, percept):
        # go to up right corner and suck from row to row
        isDirt,isBump = percept
        dic = {}
        if isDirt == "Dirty":
            return 'Suck'
        else:
            directions = ['Left', 'Right', 'Up', 'Down']
            curAct = random.choice(directions)
            uid = str(uuid.uuid4().fields[-1])[:6]
            dic[uid] = curAct
            self.listOdDic.append(dic)
            print(self.listOdDic)
            return curAct
            #if self.curAct == "Left" and isBump == "Bump":
             #   self.curAct = 'Right'
            #elif self.curAct == "Right" and isBump == "Bump":
             #   self.curAct = 'Down'
            #elif self.curAct == "Up" and isBump == "Bump":
             #   self.curAct = 'Left'
            #elif self.curAct == "Down" and isBump == "Bump":
             #   self.curAct = 'Up'
                #self.curAct = 'Down'
            #if self.curAct == "Up" and isBump == "None":
            #    self.curAct = 'Up'
            #elif self.curAct == "Right" and isBump == "None":
             #   self.curAct = 'Right'
            #elif self.curAct == "Down" and isBump == "None":
             #   self.curAct = 'Left'
            #return self.curAct  
 