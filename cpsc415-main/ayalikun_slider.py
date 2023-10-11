#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2.667 template
Stephen Davies, University of Mary Washington, fall 2023
'''

from puzzle import Puzzle
import numpy as np
import sys
from copy import deepcopy
import random 
import math


def sumOfDistOfEach(puzzle):
    totDist = 0
    for i in range(puzzle.n):
        for j in range(puzzle.n):
            if puzzle.grid[i, j] != -1:
                cRow = (puzzle.grid[i, j] - 1) // puzzle.n
                cCol = (puzzle.grid[i, j] - 1) % puzzle.n
                totDist += abs(i - cRow) + abs(j - cCol)

    return totDist
def randomMove(puzzle):
    numMoves = random.randint(1, 25) 
    copy = deepcopy(puzzle)
    for i in range(numMoves):
        legal_moves = copy.legal_moves()
        random_move = random.choice(legal_moves)
        copy.move(random_move)
    return copy


def simAnnealing(initP):
    BIGITER=100000
    temperature=10000
    coolingRate=0.998
    cur = initP
    curSumOfDist = sumOfDistOfEach(cur)
    print(f'Sum of current out of place tiles: {curSumOfDist}.')
    best = cur
    bestSum = curSumOfDist

   

    return best

    



if __name__ == '__main__':

    if (len(sys.argv) not in [2,3]  or
        not sys.argv[1].isnumeric()  or
        len(sys.argv) == 3 and not sys.argv[2].startswith("seed=")):
        sys.exit("Usage: puzzle.py dimensionOfPuzzle [seed=###].")

    n = int(sys.argv[1])

    if len(sys.argv) == 3:
        seed = int(sys.argv[2][5:])
    else:
        seed = 123

    # Create a random puzzle of the appropriate size and solve it.
    puzzle = Puzzle.gen_random_puzzle(n, seed)
    print(puzzle)
    solution = simAnnealing(puzzle)
    if solution is not None:
        print("Solution found!")
        input("Press Enter to watch.")
        print(solution)
        #solution.verify_visually([solution])
    else:
        print(f"Sorry, no solution.")
