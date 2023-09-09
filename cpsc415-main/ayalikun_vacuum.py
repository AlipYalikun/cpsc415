from vacuum import VacuumAgent
import random

class AyalikunVacuumAgent(VacuumAgent):
    #'Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp'
    def __init__(self):
        super().__init__()
    
    def program(self, percept):
        #return super().program(percept)
        isDirt,isBump = percept
        if isDirt == "Dirty":
            return 'Suck'
        else:
            directions = ['Left', 'Right', 'Up', 'Down']
            return random.choice(directions)
            