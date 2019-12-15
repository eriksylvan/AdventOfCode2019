# https://adventofcode.com/2019/day/15

import copy

inputFile = 'input/15_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getAnwer(x):
    return x*x

def day15PartOne():
    answer = "unknown"
    print(f'Solution Day 15, Part one:\nAnswer: {answer} \n\n')


def day15PartTwo():
    answer = "unknown"
    print(f'Solution Day 15, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day15PartOne()
    day15PartTwo()

# Run from terminal:
# $ python day_15.py
