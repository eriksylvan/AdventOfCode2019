# https://adventofcode.com/2019/day/12

import copy
import re
from planetClass import Planet
from math import gcd
from PlanetSystem import PlanetSystem

inputFile = 'input/12_input'

def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    planets = [[17,-7,-11],[1,4,-1],[6,-2,-6],[19,11,9]]
    #planets=[[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]
    return planets

def movePlanets(planets,steps):
    for step in range(steps):
        for planetA in range(len(planets)):
            for planetB in range(len(planets)):
                planets[planetA].gravity(planets[planetB])
        for planetA in range(len(planets)):
            planets[planetA].move()
            
    return planets

def day12PartOne():
    startPos=getInputData()
    planets=[]
    startVel=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for p in (range(len(startPos))):
        planets.append(Planet(startPos[p],startVel[p]))
    newPositions=movePlanets(planets,1000)
    totalEnergy=0
    for p in (range(len(planets))):
        totalEnergy=totalEnergy+planets[p].energy()
    answer = totalEnergy
    print(f'Solution Day 12, Part one:\nAnswer: {answer} \n\n')

def lcm(a, b):
      return (a * b) // gcd(a, b)

def findReturnToOrigin(planets):
    times=[]
    for dim in range(3):
        time=0
        while (planets.getVelocity(dim)!=[0,0,0,0] or time==0):
            time=time+1
            planets.moveOneTimeStep(dim)
        times.append(2*time)
    minTimes=lcm(times[0],lcm(times[1],times[2]))
    return minTimes

def day12PartTwo():
    startPos=getInputData()
    planets=[]
    startVel=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for p in (range(len(startPos))):
        planets.append(Planet(startPos[p],startVel[p]))
    planetSystem=PlanetSystem(planets)
    answer=findReturnToOrigin(planetSystem)
    print(f'Solution Day 12, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day12PartOne()
    day12PartTwo()

# Run from terminal:
# $ python day_12.py