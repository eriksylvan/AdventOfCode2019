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
    xDistance = pos1[0]-pos2[0]
    yDistance = pos1[1]-pos2[1]
    return abs(xDistance)+abs(yDistance)


def getGridPathDicts(wire1):
    ''' 
    Takes two wire grid paths as input and return gridPathDict with every cell in the grid 
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    '''

    # size, cp = calculateGridSize(wire1, wire2) # cp: control port location
    x = 0
    y = 0
    stp = 0
    pos1 = {}
      
    for word in wire1:
        direction = word[:1]
        distance = int(word[1:])

        if direction == 'U':
            for move in range(distance):
                stp += 1
                if (x, y+move+1) not in pos1:
                    pos1[(x, y+move+1)] = stp
            y = y+distance

        elif direction == 'D':
            for move in range(distance):
                stp += 1
                if (x, y-move-1) not in pos1:
                    pos1[(x, y-move-1)] = stp
            y = y-distance

        elif direction == 'L':
            for move in range(distance):
                stp += 1
                if (x-move-1, y) not in pos1:
                    pos1[(x-move-1, y)] = stp
            x = x-distance

        elif direction == 'R':
            for move in range(distance):
                stp += 1
                if (x+move+1, y) not in pos1:
                    pos1[(x+move+1, y)] = stp
            x = x+distance
    ###################

    # x = 0
    # y = 0
    # stp = 0    
    # pos2 = {}
    # for word in wire2:
    #     direction = word[:1]
    #     distance = int(word[1:])

    #     if direction == 'U':
    #         for move in range(distance):
    #             stp += 1
    #             if (x, y+move+1) not in pos2: 
    #                 pos2[(x, y+move+1)] = stp
    #         y = y+distance

    #     elif direction == 'D':
    #         for move in range(distance):
    #             stp += 1
    #             if (x, y-move-1) not in pos2:
    #                 pos2[(x, y-move-1)] = stp      
    #         y = y-distance

    #     elif direction == 'L':
    #         for move in range(distance):
    #             stp += 1
    #             if (x-move-1, y) not in pos2 :
    #                 pos2[(x-move-1, y)] = stp
    #         x = x-distance

    #     elif direction == 'R':
    #         for move in range(distance):
    #             stp += 1
    #             if (x+move+1, y) not in pos2:
    #                 pos2[(x+move+1, y)] = stp
    #         x = x+distance

    ###################
    



    return pos1

def manhattanDistance(wire1, wire2):
    ''' 
    Takes two wire grid paths as input and return the Manhattan Distance from the central port to the closest intersection of the wires.
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    '''


    pos1 = getGridPathDicts(wire1)
    pos2 = getGridPathDicts(wire2)
    set1 = set(pos1)
    set2 = set(pos2)
    
    intersection = set2 & set1
    print(intersection)
    distance = []
    for i in intersection:
        distance.append(calcManhattanDistance((0, 0), i))
    
    return min(distance)
    

def drawGrid(wire1, wire2):
    ''' 
    Dray a picture of two grid paths  
    '''

    size, cp = calculateGridSize(wire1, wire2)  # cp: control port location
    scale = 100

    img = Image.new('RGB', (int(size[0]/scale), int(size[1]/scale)))
    draw = ImageDraw.Draw(img)

    drawOneWire(cp, wire1, draw, scale, (255, 255, 0))
    drawOneWire(cp, wire2, draw, scale, (255, 128, 0))
    img.show()

    return None


def drawOneWire(cp, wire2, draw, scale, color):
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
                   int(newy/scale)), fill=color, width=4)
        x = copy.deepcopy(newx)
        y = copy.deepcopy(newy)


def calculateGridSize(wire1, wire2):

    def gridSize(wire):
        U = 0
        D = 0
        L = 0
        R = 0
        for word in wire:
            direction = word[:1]
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
    print(f'Solution Day 03, Part one:\nAnswer: {answer} \n\n')


def day03PartTwo():
    answer = "unknown"
    print(f'Solution Day 03, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day03PartOne()
    day03PartTwo()


# Run from terminal:
# $ python day_03.py
