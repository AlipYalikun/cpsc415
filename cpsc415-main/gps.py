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
    of that path.'''

    # THIS IS WHERE YOUR AMAZING CODE GOES
    if sys.argv[2] == 'Dijkstras':
        aCity = Atlas(int(sys.argv[1]))
        indexNumOfCity = aCity.get_num_cities() -1 
        path = []
        v = []
        dic = {}
        length = 0
        print(aCity._adj_mat)
        for i in range(indexNumOfCity+1):
            for j in range(indexNumOfCity+1):
                dist = aCity.get_road_dist(i,j)
                if dist != 0 and dist != math.inf:
                    path.append(i)
                    v.append(dist)
        # Here's a (bogus) example return value:
        #print(indexNumOfCity)
        print(v)
    return (path,length)



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

