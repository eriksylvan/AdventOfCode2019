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

def countOutersteps(orbitDictonary,satellite,step,deeplist):
    deep=step
    for s in satellite:
        step=deep
       # print(f'Visiting: {s} step:{step}')
       # print(f'Child: {orbitDictonary.get(s,"Not centre")}')
        deeplist.append(step)
        if orbitDictonary.get(s,"Not centre")=="Not centre":
            step+=1
        else:
            step+=1
            nextSatellite=orbitDictonary.get(s)
            step+=countOutersteps(orbitDictonary,nextSatellite,step, deeplist)          
    return step



def noOfOrbits(orbitMap):
    orbitDictonary = defaultdict(list)
    for orbit in orbitMap:
        centre=orbit.split(')')[0]
        satellite=orbit.split(')')[1]
        orbitDictonary[centre].append(satellite)
    satellite=orbitDictonary.get("COM")
    deeplist=[]
    countOutersteps(orbitDictonary,satellite,1, deeplist) 
    return sum(deeplist)  

########################################
########################################


def getOrbitRoute(orbitDictonary, satellite, orbitRoute, EndPoint):
    '''
    Returns the path fom Center of Mass (COM) to 'EndPoint', represented as a list of satellites to pass.
    '''
    found = False
    routeSoFar = copy.deepcopy(orbitRoute)
    for s in satellite:
        orbitRoute = copy.deepcopy(routeSoFar)
        orbitRoute.append(s)
        #print(f'Visiting: {s} orbitRoute:{orbitRoute}')
        #print(f'Child: {orbitDictonary.get(s,"Not centre")}')
        if s==EndPoint:
                # print('Endpoint found!')
                found = True
        if orbitDictonary.get(s,"Not centre")!="Not centre" and not found:
            nextSatellite=orbitDictonary.get(s)
            orbitRoute, found = getOrbitRoute(orbitDictonary, nextSatellite, orbitRoute, EndPoint)
        if found: break
    return orbitRoute, found

def distanceSanta(orbitMap):
    found = False
    orbitDictonary = defaultdict(list)
    for orbit in orbitMap:
        centre=orbit.split(')')[0]
        satellite=orbit.split(')')[1]
        orbitDictonary[centre].append(satellite)
    #print(orbitDictonary)

    satellite=orbitDictonary.get("COM")
    #print(satellite)
    youRoute = []
    youRoute, found = getOrbitRoute(orbitDictonary,satellite, youRoute,'YOU')
    #print(youRoute)
    #print('FindSanta!!!!!!!!!!!!')
    santaRoute = []    
    #satellite=orbitDictonary.get("COM")
    santaRoute, found = getOrbitRoute(orbitDictonary,satellite, santaRoute,'SAN')
    #print(santaRoute)

    youSet = set(youRoute)
    santaSet = set(santaRoute)

    #print(youSet ^ santaSet)

    return len(youSet ^ santaSet)-2






######################################
######################################
def day06PartOne():
    oMap = getInputData()
    # print(oMap)
    answer = noOfOrbits(oMap)
    print(f'Solution Day 06, Part one:\nAnswer: {answer} \n\n')


def day06PartTwo():
    oMap = getInputData()
    # print(oMap)
    answer = distanceSanta(oMap)
    print(f'Solution Day 06, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day06PartOne()
    day06PartTwo()

# Run from terminal:
# $ python day_05.py