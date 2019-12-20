# https://adventofcode.com/2019/day/19

import copy
from intcode_computer import IntcodeComputer

inputFile = 'input/19_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def drone(h=50, w=50):
    code = getInputData()
    # IC = IntcodeComputer(code)
#    out = {}
    pic = []
    count = 0
    for y in range(h):
        row = ''
        for x in range(w):
            IC = IntcodeComputer(code)
            o = IC.run_program([x,y])
            if o[0] == 1:
                count +=1
                row += '#'
            else:
                row += '.'
            
        pic.append(row)

    # print(out)
    for r in pic: print(r)
    
    return count
    
def getAnwer(v):
    return -v*v

def isInBeam(x,y):
    code = getInputData()
    IC = IntcodeComputer(code)
    o = IC.run_program([x,y])
    if o[0] == 1:
        return True
    else:
        return False

def shipInside(x, y, sDx, sDy):
    print(isInBeam(x,y))
    print(isInBeam(x+sDx-1,y))
    print(isInBeam(x, y+sDy-1))
    print(isInBeam(x+sDx-1, y+sDy-1))
    return [isInBeam(x,y), isInBeam(x+sDx-1,y), isInBeam(x, y+sDy-1), isInBeam(x+sDx-1, y+sDy-1)]

def findClosest():
    '''
    Approach: moving in the beam direction one step at the time until the ship (100 x 100 fits)
    Start with a known secure point in teh beam, schoosen manually (6,20)
    TopLeft corner is always in the beam, 
        If BottomLeft outside beam: move right
        If TopRight outside beam: move down
        If both BottomLeft and TopRight in beam: firt fit location found. 
    '''
    topLeft=[6,20]    
    sD =[100, 100]

    while True:
        topRight = [topLeft[0] + sD[0]-1, topLeft[1] ]
        bottomLeft = [topLeft[0], topLeft[1] + sD[1]-1]
        if isInBeam(bottomLeft[0], bottomLeft[1]):
            if isInBeam(topRight[0], topRight[1]):  # True implies topLeft and bottomRight also inside beam
                return topLeft
            topLeft = [topLeft[0], topLeft[1] + 1]  # Move down
        else:
            topLeft = [topLeft[0] + 1, topLeft[1]]  # Move right    

            




def day19PartOne():
    answer = drone()
    print(f'Solution Day 19, Part one:\nTractor beam affects: {answer} positions within 50x50 range \n\n')


def day19PartTwo():
    topLeftCorner = findClosest()
    answer = topLeftCorner[0] * 10000 + topLeftCorner[1]
    print(f'Solution Day 19, Part two:\nFist position that the ship fits is: {topLeftCorner} (TopLeftCorner) \nThis gives the answer: {answer} \n\n')


if __name__ == "__main__":
    day19PartOne()
    day19PartTwo()

# Run from terminal:
# $ python day_19.py
