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
            if isBump=="None":
                self.curAct = 'Up'
            else:
                if self.curAct == 'Up':
                    self.curAct = 'Right'
                elif self.curAct == 'Right':
                    self.curAct = 'Up'
            return self.curAct
            #directions = ['Left', 'Right', 'Up', 'Down']
            #return random.choice(directions)
            