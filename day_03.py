# https://adventofcode.com/2019/day/3

import copy
from PIL import Image, ImageDraw   # python -m pip install pillow
import os


inputFile = 'input/03_input'


def getInputData():
    '''Reads the input file end returns the data in lists of strings'''
    wirePath = []
    with open(inputFile) as input:
        for line in input:
            wirePath.append([str(x) for x in line.strip().split(',')])
    return wirePath


def calcManhattanDistance(pos1, pos2):
    '''
    Calculates the Manhattan distance between two positions in a grid. (x1,y2) and (x2,y2)
    '''
    xDistance = pos1[0] - pos2[0]
    yDistance = pos1[1] - pos2[1]
    return abs(xDistance) + abs(yDistance)


def getGridPathDict(wire):
    ''' 
    Takes one wire grid paths as input and return gridPathDict that represent evey cell that whw wire pass in the grid path.     
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    The dictionary key is a position (x,y) the value is minimum number of steps to reach that potition.
    '''

    x = 0
    y = 0
    stp = 0
    gridDict = {}

    for word in wire:
        direction = word[:1]
        distance = int(word[1:])

        if direction == 'U':
            for move in range(distance):
                stp += 1
                if (x, y+move+1) not in gridDict:  # Do not override if position already exists
                    gridDict[(x, y+move+1)] = stp
            y = y+distance

        elif direction == 'D':
            for move in range(distance):
                stp += 1
                if (x, y-move-1) not in gridDict:
                    gridDict[(x, y-move-1)] = stp
            y = y-distance

        elif direction == 'L':
            for move in range(distance):
                stp += 1
                if (x-move-1, y) not in gridDict:
                    gridDict[(x-move-1, y)] = stp
            x = x-distance

        elif direction == 'R':
            for move in range(distance):
                stp += 1
                if (x+move+1, y) not in gridDict:
                    gridDict[(x+move+1, y)] = stp
            x = x+distance

    return gridDict


def manhattanDistance(wire1, wire2):
    ''' 
    Takes two wire grid paths as input and return the Manhattan Distance from the central port to the closest intersection of the wires.
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    '''

    gridDict1 = getGridPathDict(wire1)
    gridDict2 = getGridPathDict(wire2)
    set1 = set(gridDict1)
    set2 = set(gridDict2)

    intersection = set2 & set1
    distance = []
    for i in intersection:
        distance.append(calcManhattanDistance((0, 0), i))

    return min(distance)


def gridMinStep(wire1, wire2):
    '''
    Takes two wire grid paths as input and return the Min grid distance to the fist intersection of the wires.
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    '''
    gridDict1 = getGridPathDict(wire1)
    gridDict2 = getGridPathDict(wire2)
    set1 = set(gridDict1)
    set2 = set(gridDict2)

    intersection = set2 & set1
    steps = []
    for i in intersection:
        steps.append(gridDict1.get(i) + gridDict2.get(i))
    return min(steps)


def drawWire(cp, wire2, draw, scale, color):
    x, y = cp[0], cp[1]
    newx, newy = x, y

    for word in wire2:
        direction = word[:1]
        distance = int(word[1:])

        if direction == 'U':
            newx = x - distance
        elif direction == 'D':
            newx = x + distance
        elif direction == 'L':
            newy = y - distance
        elif direction == 'R':
            newy = y + distance
        draw.line((int(x/scale), int(y/scale), int(newx/scale),
                   int(newy/scale)), fill=color, width=1)
        x = copy.deepcopy(newx)
        y = copy.deepcopy(newy)


def calculateGridSize(wire1, wire2):
    '''
    Calculates the maximal gridsize that is needed
    '''

    def gridSize(wire):
        U = 0
        D = 0
        L = 0
        R = 0
        for word in wire:
            direction = word[0]
            distance = int(word[1:])

            if direction == 'U':
                U += distance
            elif direction == 'D':
                D += distance
            elif direction == 'L':
                L += distance
            elif direction == 'R':
                R += distance
            else:
                assert False, f'Invalid direction: {direction}'
        return [U, D, L, R]

    s1 = gridSize(wire1)
    s2 = gridSize(wire2)

    for i in range(3):
        s1[i] = max(s1[i], s2[i])

    return (s1[0]+s1[1]+1, s1[2]+s1[3]+1), (s1[1]+1, s1[2]+1)


def day03PartOne():

    wirePaths = getInputData()
    answer = manhattanDistance(wirePaths[0], wirePaths[1])
    #  drawGrid(wirePaths[0], wirePaths[1])
    print(f'Solution Day 03, Part one:\nThe Manhattan distance from the central port to the closest intersection: {answer} \n\n')


def day03PartTwo():
    wirePaths = getInputData()
    answer = gridMinStep(wirePaths[0], wirePaths[1])
    print(f'Solution Day 03, Part two:\nThe fewest combined steps the wires must take to reach an intersection: {answer} \n\n')


def drawWirePath():
    ''' 
    Dray a picture of two grid paths  
    '''
    wirePaths = getInputData()
    # cp: control port location
    size, cp = calculateGridSize(wirePaths[0], wirePaths[1])
    scale = 100

    img = Image.new('RGB', (int(size[0]/scale), int(size[1]/scale)))
    draw = ImageDraw.Draw(img)

    drawWire(cp, wirePaths[0], draw, scale, (255, 255, 0))
    drawWire(cp, wirePaths[1], draw, scale, (255, 128, 0))
    img.show()


if __name__ == "__main__":
    day03PartOne()
    day03PartTwo()
    drawWirePath()

# Run from terminal:
# $ python day_03.py
