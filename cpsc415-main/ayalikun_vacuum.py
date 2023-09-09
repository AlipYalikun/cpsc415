from vacuum import VacuumAgent
import random

class AyalikunVacuumAgent(VacuumAgent):
    #'Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp'
    def __init__(self):
        super().__init__()
        self.curAct = 'Right'
    
    def program(self, percept):
        #return super().program(percept)
        # go to up right corner and suck from row to row
        isDirt,isBump = percept
        if isDirt == "Dirty":
            return 'Suck'
        else:
            if isBump == "Bump":
                self.curAct = 'Down'
            elif self.curAct == 'Right':
                self.curAct = 'Up'
            elif self.curAct == 'Up':
                self.curAct = 'Right'
            elif self.curAct == 'Down':
                self.curAct = 'Left'
            return self.curAct
            #directions = ['Left', 'Right', 'Up', 'Down']
            #return random.choice(directions)
            