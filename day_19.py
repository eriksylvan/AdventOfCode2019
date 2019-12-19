# https://adventofcode.com/2019/day/19

import copy

inputFile = 'input/19_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getAnwer(v):
    return -v*v

def day19PartOne():
    answer = "unknown"
    print(f'Solution Day 19, Part one:\nAnswer: {answer} \n\n')


def day19PartTwo():
    answer = "unknown"
    print(f'Solution Day 19, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day19PartOne()
    day19PartTwo()

# Run from terminal:
# $ python day_19.py
