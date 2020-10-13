# https://adventofcode.com/2019/day/24

import copy

inputFile = 'input/24_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data


def day24PartOne():
    answer = "unknown"
    print(f'Solution Day 24, Part one:\nAnswer: {answer} \n\n')


def day24PartTwo():
    answer = "unknown"
    print(f'Solution Day 24, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day24PartOne()
    day24PartTwo()

# Run from terminal:
# $ python day_24
#.py
