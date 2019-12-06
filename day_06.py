# https://adventofcode.com/2019/day/6

import copy
from collections import defaultdict

inputFile = 'input/06_input'


def getInputData():
    '''Reads the input file end returns the data in a list of strings'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data.append(str(line).replace('\n','').replace('\r',''))
    return data

def countOutersteps(orbitDictonary,satellite,step):
    deep=step
    for s in satellite:
        step=deep
        print(f'Visiting: {s} step:{step}')
        result=step
        print(f'Child: {orbitDictonary.get(s,"Not centre")}')
        if orbitDictonary.get(s,"Not centre")=="Not centre":
            print(step)
        else:
            step+=1
            print(step)
            nextSatellite=orbitDictonary.get(s)
            result+=countOutersteps(orbitDictonary,nextSatellite,step)
            print(step)
            
    return result

def noOfOrbits(orbitMap):
    orbitDictonary = defaultdict(list)
    for orbit in orbitMap:
        centre=orbit.split(')')[0]
        satellite=orbit.split(')')[1]
        orbitDictonary[centre].append(satellite)
    print(f'orbitDictonary:{orbitDictonary}')
    satellite=orbitDictonary.get("COM")
    nbrOrbits=countOutersteps(orbitDictonary,satellite,1) 
    return nbrOrbits  



def day06PartOne():
    oMap = getInputData()
    # print(oMap)
    answer = noOfOrbits(oMap)
    print(f'Solution Day 06, Part one:\nAnswer: {answer} \n\n')


def day06PartTwo():
    answer = "unknown"
    print(f'Solution Day 06, Part two:\nAnswer: {answer} \n\n')