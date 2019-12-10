# https://adventofcode.com/2019/day/10

import copy

inputFile = 'input/10_input'

class Astroid:

    def __init__(self,pos):
        self._pos = pos
        self._noVisibleFromMe = 0 #start fom 0
    def __str__(self):
        return str(self._pos)

def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data.append(line.strip()) # strip() removes tailing \n
    return data

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b using Euclidean algorithm

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def contVisibleAsroids(astroidMap):
    '''
    Not yet implemented
    '''

    return (len(astroidMap) * len(astroidMap[0]), (0,0))



def findBestMonitoringStation(map):
    '''
    The best location is the asteroid that can detect the largest number of other asteroids.
    Returning #asdroids and Position
    '''


    # Get unique set of angle vectors 
    hight = len(map)
    width = len(map[0])
    aList = []
    for y in range(-hight, hight):
        for x in range(-width, width):
            aList.append((x,y))

    naList = []
    for a in aList:
        d = abs(gcd(a[0],a[1]))
       
        if d!=0:
            na = (a[0]//d, a[1]//d)
        else:
            na = (a[0], a[1])
        naList.append(na)

    uniqueAngleSet = set(naList)
    uniqueAngleSet.discard((0,0))

    # Get Astroid coodrinates (cartesian x,y)
    astroids = {}
    backup = {}
    for yy, line in enumerate(map):
        for xx, p in enumerate(line):         
            if p == '#':
                astroids[(xx,yy)] = Astroid((xx,yy))
                backup[(xx,yy)] = 0
           

    # For ecery asdroid, find its closest visible neighbours and count them 
    for astPos, astVal in astroids.items():
        counter=0
        for angle in uniqueAngleSet:
            sx = astPos[0] + angle[0]
            sy = astPos[1] + angle[1]
            while (0 <= sx <= width) and (0 <= sy <= hight):
                if (sx,sy) in astroids.keys():
                    counter+=1
                    break
                sx += angle[0]
                sy += angle[1]

        astVal._noVisibleFromMe = counter
        maxCount = 0
        maxPos = (-1,-1) 

    for ast in astroids.values():
        if ast._noVisibleFromMe > maxCount:
            maxCount = ast._noVisibleFromMe
            maxPos = ast._pos    
    
    return maxCount, maxPos        


def day10PartOne():
    androidMap = getInputData()
    count, pos = findBestMonitoringStation(androidMap)  
    
    print(f'Solution Day 10, Part one:\nBest Androis monitoring spot is: {pos}\nNumber of visible asdroids: {count} \n\n')


def day10PartTwo():
    answer = "unknown"
    print(f'Solution Day 10, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    
    day10PartOne()
    # day10PartTwo()

# Run from terminal:
# $ python day_10.py





# Solution Day 10, Part one:
# Best Androis monitoring spot is: (23, 20)
# Number of visible asdroids: 334