from vacuum import VacuumAgent
import random
import uuid 

class AyalikunVacuumAgent(VacuumAgent):
    #'Right', 'Left', 'Up', 'Down', 'Suck', 'NoOp'
    def __init__(self):
        super().__init__()
        #creating a list where I will be adding dictionary
        self.listOdDic = []
        self.cord = (0,0)
        self.curAct = "Up"
    def program(self, percept):
        # go to up right corner and suck from row to row
        isDirt,isBump = percept
        dic = {}
        if isDirt == "Dirty":
            return 'Suck'
        else:
            if self.curAct == "Left" and isBump == "Bump":
                self.curAct = 'Right'
            elif self.curAct == "Right" and isBump == "Bump":
                self.curAct = 'Down'
            elif self.curAct == "Up" and isBump == "Bump":
                self.curAct = 'Left'
            elif self.curAct == "Down" and isBump == "Bump":
                self.curAct = 'NoOp'
            elif self.curAct == "Up" and isBump == "None":
                self.curAct = 'Up'
            elif self.curAct == "Right" and isBump == "None":
                self.curAct = 'Right'
            elif self.curAct == "Down" and isBump == "None":
                self.curAct = 'Left'
            #tOfCord = self.cord #x,y cordinates
            #go up add 1 to y go down minus 1 from y
            # go left minus 1 to x go right plus 1 to x
            
            #curAct = random.choice(directions)
            next_cord = self.cord
            if self.curAct == "Right" and isBump == "None":
                next_cord = (self.cord[0] + 1 , self.cord[1])
            elif self.curAct == "Left" and isBump == "None":
                next_cord = (self.cord[0] - 1 , self.cord[1])
            elif self.curAct == "Up" and isBump == "None":
                next_cord = (self.cord[0], self.cord[1] + 1)
            elif self.curAct == "Down" and isBump == "None":
                next_cord = (self.cord[0], self.cord[1] - 1)
           # elif self.curAct == "Right" and isBump == "Bump":
            #    if self.cord[0] > 0:
             #       next_cord = (self.cord[0] - 1 , self.cord[1])
              #  else:
               #     next_cord = (self.cord[0] + 1 , self.cord[1])
            #elif self.curAct == "Left" and isBump == "Bump":
             #   if self.cord[0] < 0 :
              #      next_cord = (self.cord[0] + 1, self.cord[1])
               # else:
                #    next_cord = (self.cord[0] - 1 , self.cord[1])
            #elif self.curAct == "Up" and isBump == "Bump":
             #   if self.cord[1] > 0:
              #      next_cord = (self.cord[0] , self.cord[1] - 1)
               # else:
                #    next_cord = (self.cord[0] , self.cord[1] + 1)
            #elif self.curAct == "Down" and isBump == "Bump":
             #   if self.cord[1] < 0:
              #      next_cord = (self.cord[0] , self.cord[1] + 1)
               # else:
                #    next_cord = (self.cord[0] , self.cord[1] - 1)
            #uid = str(uuid.uuid4().fields[-1])[:6]
            #dic[self.cord] = curAct
          
                
            self.listOdDic.append(next_cord)
            #print(self.listOdDic)
            #print(len(self.listOdDic))
            #self.cord = next_cord
            return self.curAct

 