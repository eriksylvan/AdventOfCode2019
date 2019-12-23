# https://adventofcode.com/2019/day/21

import copy
import random
from intcode_computer import IntcodeComputer

inputFile = 'input/21_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def runRobot(instructions):
    robotController = getInputData()
    IC = IntcodeComputer(robotController)
    IC.run_program(instructions)
    outCode = IC._output
    # print(ascii2str(outCode))
    return ascii2str(outCode)
    
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
    

def day21PartOne():
    instructions = "NOT C T\nNOT A J\nOR T J\n AND D J\nWALK\n" #jump if (A=hole OR C=hole) AND D not hole 
    ascciInst = str2asciiList(instructions) 
    answer = runRobot(ascciInst)
    print(f'Solution Day 21, Part one:\n\n {answer} \n\n')


def day21PartTwo():
    answer = "unknown"
    print(f'Solution Day 21, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day21PartOne()
    # day21PartTwo()

    #print(str2asciiList("Erik\n"))
    # instructions = "NOT A J\nNOT B T\nAND T J\nNOT C T\nAND T J\nAND D J\nWALK\n"
    # instructions = "NOT A J\nWALK\n" #Jump  if A=hole /FAIL
    # instructions = "NOT D T\nNOT T J\nWALK\n" # always jump if you can land /FAIL
    # instructions = "NOT C J\nAND D J\nWALK\n" #jump if theren is a hole on C and floor on D
    ##instructions = "NOT C T\nNOT A J\nOR T J\n AND D J\nWALK\n" #jump if (A=hole OR C=hole) AND D not hole 
    #ascciInst = str2asciiList(instructions)
    #print(ascciInst)
    #runRobot(ascciInst)

# Run from terminal:
# $ python day_21.py