# https://adventofcode.com/2019/day/5

import copy
from intcode_computer import IntcodeComputer 

inputFile = 'input/05_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    intCodeProgram = []
    with open(inputFile) as input:
        for line in input:
            intCodeProgram = [int(x) for x in line.split(',')]
    return intCodeProgram

# def runDiagnosticProgram(intCode):
#     return len(intCode)


def day05PartOne():
    prg = getInputData()
    IntCode = IntcodeComputer(prg)
    print(f'Solution Day 05, Part one:\nRunning TEST diagnostic program...\nGive manual input=>1\n')
    IntCode.run_program()
    

def day05PartTwo():
    prg2 = getInputData()
    IntCode2 = IntcodeComputer(prg2)
    print(f'Solution Day 05, Part two:\nRunning TEST diagnostic program...\nGive manual input=>5\n')
    IntCode2.run_program()


if __name__ == "__main__":
    day05PartOne()
    day05PartTwo()


    


# Run from terminal:
# $ python day_05.py

# Result
# part 1
# Output:9006673
#
# part 2
# Output:3629692