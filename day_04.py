# https://adventofcode.com/2019/day/4

import copy

inputFile = 'input/04_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    intCodeProgram = []
    with open(inputFile) as input:
        for line in input:
            intCodeProgram = [int(x) for x in line.split(',')]
    return intCodeProgram


def day04PartOne():
    answer = "unknown"
    print(f'Solution Day 04, Part one:\nAnswer: {answer} \n\n')


def day04PartTwo():
    answer = "unknown"
    print(f'Solution Day 04, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day04PartOne()
    day04PartTwo()

# Run from terminal:
# $ python day_03.py
