# https://adventofcode.com/2019/day/XX

import copy

inputFile = 'input/XX_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    intCodeProgram = []
    with open(inputFile) as input:
        for line in input:
            intCodeProgram = [int(x) for x in line.split(',')]
    return intCodeProgram


def dayXXPartOne():
    answer = "unknown"
    print(f'Solution Day XX, Part one:\nAnswer: {answer} \n\n')


def dayXXPartTwo():
    answer = "unknown"
    print(f'Solution Day XX, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    dayXXPartOne()
    dayXXPartTwo()

# Run from terminal:
# $ python day_03.py
