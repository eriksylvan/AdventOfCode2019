# https://adventofcode.com/2019/day/25

import copy
from intcode_computer import IntcodeComputer 

inputFile = 'input/25_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data


def ascii2str(asciiList):
    outStr = ""
    for i in asciiList:
        if i > 128: # if not ascii value
            outStr+=f'\nAmount of damage to the hull:{i}\n'
        else:
            outStr+=chr(i)
    return outStr

def str2asciiList(inpStr):
    return [ord(c) for c in inpStr]


def runDroid(instructions):
    droidController = getInputData()
    IC = IntcodeComputer(droidController)
    inp = []
    stoppedAtInput = False
    terminated = False
    
    while not terminated:
        # print(inp)
        # print(terminated, stoppedAtInput)
        while not terminated and not stoppedAtInput:
            terminated, stoppedAtInput = IC.perform_one_operation(input=inp,stopAtInput=True)
            #print('hej')
    
        if stoppedAtInput:
            outCode = IC._output
            print(ascii2str(outCode))
            inpStr = input('>')+'\n'
            inp = str2asciiList(inpStr)
            stoppedAtInput = False

    return ascii2str(outCode)


def day25PartOne():
    runDroid([])
    answer = "unknown"
    print(f'Solution Day 25, Part one:\nAnswer: {answer} \n\n')


def day25PartTwo():
    answer = "unknown"
    print(f'Solution Day 25, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day25PartOne()
    # day25PartTwo()



# Run from terminal:
# $ python day_25.py
