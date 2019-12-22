# https://adventofcode.com/2019/day/21

import copy

inputFile = 'input/21_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data


def day21PartOne():
    answer = "unknown"
    print(f'Solution Day 21, Part one:\nAnswer: {answer} \n\n')


def day21PartTwo():
    answer = "unknown"
    print(f'Solution Day 21, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day21PartOne()
    day21PartTwo()

# Run from terminal:
# $ python day_21.py
