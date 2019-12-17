# https://adventofcode.com/2019/day/17

import copy
from intcode_computer import IntcodeComputer
import re   # regular expression


inputFile = 'input/17_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def cameraOutput(defaultColor=0):
    code = getInputData()
    IC = IntcodeComputer(code)
    


    step=0
    inp=[]
    IC._output = []    # Clear the output list
    terminate = False
    stoppedAtInput = False
    while not terminate:
        while not stoppedAtInput and not terminate:
            terminate, stoppedAtInput = IC.perform_one_operation(IC._memoryPosition, inp, stopAtInput = True) 
        step +=1
        # print(f'### STEP {step} ###')
        # print(f'OutPut{IC._output}')
        # print(f'OutPut{IC._output}')        
        stoppedAtInput = False
    ret = []
    row = ''
    for ascii in IC._output:
        if str(ascii) == '10': 
            ret.append(row)
            row = ''
        else:
            row += chr(ascii)
    return ret

def findIntersections(map):
    length = len(map[0])
    hight = len(map)
    p = re.compile('[.][.][.]')
    r = re.compile('[.][^.][.]')
    ret = []

    for r in range(1, hight-1):
        for c in range(1, length-1):
            # print(map[r-1][c-1:c+2])
            # print(map[r][c-1:c+2])
            # print(map[r+1][c-1:c+2])
            # print(f'---   ({r},{c})')

            if re.match('[.][^.][.]', map[r-1][c-1:c+2]) and  \
                re.match('[^.][^.][^.]', map[r][c-1:c+2]) and \
                re.match('[.][^.][.]', map[r+1][c-1:c+2]):
                    ret.append((r,c))
    return ret

def calcAlignmentParameters(map):
    inter = findIntersections(map)
    ret = 0
    for t in inter: ret += t[0] *t[1]
    return ret


def day17PartOne():
    map = cameraOutput()
    alPar = calcAlignmentParameters(map)
    

    print(f'Solution Day 17, Part one:\nAnswer: {alPar} \n\n')


def day17PartTwo():
    answer = "unknown"
    print(f'Solution Day 17, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day17PartOne()
    day17PartTwo()

# Run from terminal:
# $ python day_17.py


# Solution Day 17, Part one:
# Answer: 2508