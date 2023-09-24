#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Stephen Davies, University of Mary Washington, fall 2023
'''

from atlas import Atlas
import numpy as np 
import sys
import math

def find_path(atlas, alg):
    '''Finds a path from src to dest using a specified algorithm, and
    based on costs from the atlas provided. The second argument must be one
    of the values "greedy", "Dijkstras", or "A*".

    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.
    for index, value in enumerate(row):
                if value > num and value != math.inf:
                    print(f'[{row_index}, {index}]: {value}')'''
    if alg == 'Dijkstras':
        #a = atlas._adj_mat
        #print(a)
        #setting distance from nodes to infinite first
        numOfCity = atlas.get_num_cities()
        distance = [math.inf] * numOfCity
        #root node is always zero 
        rootCity = 0
        distance[rootCity] = 0
        #setting unvisited nodes to false once visited it will be true
        visited = [False] * numOfCity
        #print(distance)
        #setting previous to -1
        previous = [-1] * numOfCity
        #print(a[0,:])
        #num = 0
        #nums = []
        #expanded = atlas._nodes_expanded
        for city in range(numOfCity):
            #get list of unvisited cities
            #print(f"proccesing city {city}")
            unvisitedC = [i for i in range(numOfCity) if not visited[i]]
            #print(f'unvisited city: {unvisitedC}')
            #find the unvisited city with the shortest distance from the source
            currentC = min(unvisitedC, key=lambda i: distance[i])
            #print(f'current city: {currentC}')
            visited[currentC] = True
            for neighborC in range(numOfCity):
               #print(f'considering the neighbor {neighborC}')
                #updating distance if shorter is found
               if not visited[neighborC] and atlas.get_road_dist(currentC, neighborC) != math.inf:
                    newD = distance[currentC] + atlas.get_road_dist(currentC, neighborC)
                    #print(f"New distance to {neighborC}: {newD}")
                    #update the distace and previos node if shorter found
                    if newD < distance[neighborC]:
                        distance[neighborC] = newD
                        previous[neighborC] = currentC
                    
    
                   
        #recoanstruct the path
        path = []
        currentC = numOfCity -1
        while currentC != -1:
            path.append(currentC)
            currentC = previous[currentC]
   
        path.reverse()
        #print("visited node: ", expanded)

        #s = {}
        #for row_index, row in enumerate(a):
        #    vals = [(j,num) for j, num in enumerate(row) if num > 0 and num != math.inf]
        #    if vals:
        #        s[row_index] = vals
        #for node in s:
        #for node, v in s.items():
        #    sorteD =  sorted(v, key=lambda x: min(x))
        #    for index, value in sorteD:
        #        print(f"Row {node}: Index: {index}, Value: {value}")
        #        if value > num:
        #            num = value
        #            nums.append(num)
        #            num = 0
        #print(s)      
        #print(nums)
        cost = distance[numOfCity-1]
    return (path,cost)
   


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: gps.py numCities|atlasFile algorithm.")
        sys.exit(1)

    if len(sys.argv) > 2:
        if sys.argv[2] not in ['greedy', 'Dijkstras', 'A*']:
            print(f'Algorithm must be one of: "greedy", "Dijkstras", or "A*".'
                f' (You put "{sys.argv[2]}".)')
            sys.exit(2)
        else:
            alg = sys.argv[2]

    try:
        num_cities = int(sys.argv[1])
        print(f'Building random atlas with {num_cities} cities...')
        usa = Atlas(num_cities)
        print('...built.')
    except:
        print(f'Loading atlas from file {sys.argv[1]}')
        usa = Atlas.from_filename(sys.argv[1])
        print('...loaded.')
    
    path, cost = find_path(usa, alg)
    print(f'The {alg} path from 0 to {usa.get_num_cities()-1}'
        f' costs {cost}: {path}.')
    ne = usa._nodes_expanded
    print(f'It expanded {len(ne)} nodes: {ne}')

