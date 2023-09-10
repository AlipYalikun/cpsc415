from vacuum import VacuumAgent
import random

class AyalikunVacuumAgent(VacuumAgent):
    #'Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp'
    def __init__(self):
        super().__init__()
        self.curAct = 'Up'
        self.hitTopRight = True
    def program(self, percept):
        # go to up right corner and suck from row to row
        isDirt,isBump = percept
        if isDirt == "Dirty":
            return 'Suck'
        else:
            if isBump == "None":
                if self.curAct == "Up":
                    self.curAct = 'Up'
                elif self.curAct == "Down":
                    self.curAct = 'Right'
                elif self.curAct == "Right":
                    self.curAct = 'Up'
            if isBump=="Bump":
                if self.curAct == 'Up':
                    self.curAct = 'Down'
                elif self.curAct == 'Right':
                    self.curAct = 'Up'            
                
            else:
                pass
            return self.curAct
            #directions = ['Left', 'Right', 'Up', 'Down']
            #return random.choice(directions)
            