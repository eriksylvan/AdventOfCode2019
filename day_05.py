# https://adventofcode.com/2019/day/5

import copy

inputFile = 'input/05_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    intCodeProgram = []
    with open(inputFile) as input:
        for line in input:
            intCodeProgram = [int(x) for x in line.split(',')]
    return intCodeProgram

def runDiagnosticProgram(intCode):
    return len(intCode)


def day05PartOne():
    answer = "unknown"
    print(f'Solution Day 05, Part one:\nAnswer: {answer} \n\n')


def day05PartTwo():
    answer = "unknown"
    print(f'Solution Day 05, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day05PartOne()
    day05PartTwo()

# Run from terminal:
# $ python day_05.py
