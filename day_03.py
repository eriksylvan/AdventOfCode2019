# https://adventofcode.com/2019/day/3

import copy

inputFile = 'input/03_input'


def getInputData():
    '''Reads the input file end returns the data in lists of strings'''
    wirePath = []
    with open(inputFile) as input:
        for line in input:
            wirePath.append([str(x) for x in line.strip().split(',')])
    return wirePath


def manhattanDistance(wire1, wire2):
    ''' 
    Takes two wire grid paths as input and return the Manhattan Distance from the central port to teh closest intersection of the wires.
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    '''

    size = calculateMaxGridSize(wire1, wire2)

    '''To be implemented'''
    return len(wire1)+len(wire2)

def calculateMaxGridSize(wire1, wire2):
    
    
    def gridSize(wire):
        U=0; D=0; L=0; R=0
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
        return [U,D,L,R] 

    print(gridSize(wire1))
    print(gridSize(wire2))
    # [('U'),('D'),('L'),('R')]

    return 0


def day03PartOne():

    wirePaths = getInputData()
    # answer = manhattanDistance(wirePaths[0],wirePaths[1])
    print(calculateMaxGridSize(wirePaths[0],wirePaths[1]))
    answer = 0
    print(f'Solution Day 03, Part one:\nAnswer: {answer} \n\n')


def day03PartTwo():
    answer = "unknown"
    print(f'Solution Day 03, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day03PartOne()
    day03PartTwo()


# Run from terminal:
# $ python day_03.py