from vacuum import VacuumAgent
import random

class AyalikunVacuumAgent(VacuumAgent):
    #'Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp'
    def __init__(self):
        super().__init__()
        self.curAct = 'Up'
    
    def program(self, percept):
        #return super().program(percept)
        # go to up right corner and suck from row to row
        isDirt,isBump = percept
        if isDirt == "Dirty":
            return 'Suck'
        else:
            if self.curAct == 'Up' and isBump=="Bump":
                self.curAct = 'Right'
            elif self.curAct == 'Right' and isBump == "Bump":
                self.curAct = "Down"
            elif self.curAct == 'Right' and isBump == "None":
                self.curAct = "Right"
            elif self.curAct == 'Down' and isBump == "None":
                self.curAct = 'Right'
            elif self.curAct == "Down" and isBump == "Bump":
                self.curAct = 'Left'
            return self.curAct
            #directions = ['Left', 'Right', 'Up', 'Down']
            #return random.choice(directions)
            