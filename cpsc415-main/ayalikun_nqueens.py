import random
import math
import sys
 

def randomState(nq):
    return [random.randint(0, nq-1) for _ in range(nq)]
def attack(nq):
    atk = 0
    for i in range(len(nq)):
        for j in range(i+1, len(nq)):
            if nq[i] == nq[j] or abs(i-j) == abs(nq[i] - nq[j]): #check row and diagnal
                atk += 1
    return atk
def simulatedAnnealing(nq):
    bigITERATION = 100000
    temprature = 1000
    coolRate = 0.998
    curState = randomState(nq) 
    curAtk = attack(curState)
    for a in range(bigITERATION):
        if curAtk == 0:
            #print(curState)
            return curState 
        newState = list(curState)
        row = random.randint(0, len(curState)-1)
        col = random.randint(0, len(curState)-1)
        newState[row] = col
        newAtk = attack(newState)
        if newAtk < curAtk or random.random() < math.exp((curAtk - newAtk) / temprature):
            curState = newState
            curAtk = newAtk
            a = ''.join(str(curState).split(","))
            print(a)
        temprature *= coolRate
n = int(sys.argv[1])
solved = simulatedAnnealing(n)
#printing it pretty 
matrix = [["." for i in range(len(solved))] for j in range(len(solved))]
for i,col in enumerate(solved):
    matrix[col][i] = 'Q'
border = '+' + '-' * (n * 2) + '+'
matrixStr = border + '\n' + '\n'.join('|' + ' '.join(rows) + '|' for rows in matrix) + '\n' +border
if solved:
    a = ''.join(str(solved).split(","))
    print(f'The answer to {n} queens is {a}')
    print(matrixStr)  
else:
    print("try again or smaller")