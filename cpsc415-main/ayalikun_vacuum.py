from vacuum import VacuumAgent

class AyalikunVacuumAgent(VacuumAgent):
    def __init__(self):
        super().__init__()
    
    def program(self, percept):
        #return super().program(percept)
        return 'NoOp'
    