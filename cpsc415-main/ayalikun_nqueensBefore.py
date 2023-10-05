import random
import sys


def randomState(nq):
    return [random.randint(0, nq-1) for _ in range(nq)]
def attack(nq):
    atk = 0
    for i in range(len(nq)):
        for j in range(i+1, len(nq)):
            if nq[i] == nq[j] or abs(i-j) == abs( nq[i] - nq[j]): #check row and diagnal
                atk += 1
    return atk
def simulatedAnnealing(nq):
    bigITERATION = 100000
    curState = randomState(nq) 
    curAtk = attack(curState)
    for a in range(bigITERATION):
        if curAtk == 0:
            print(curState)
        newState = list(curState)
        row = random.randint(0, len(curState)-1)
        col = random.randint(0, len(curState)-1)
        newState[row] = col
        newAtk = attack(newState)
        if newAtk < curAtk:
            curState = newState
            curAtk = newAtk
      
       
n = int(sys.argv[1])
solved = simulatedAnnealing(n)