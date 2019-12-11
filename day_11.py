# https://adventofcode.com/2019/day/11

import copy

inputFile = 'input/11_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getAnwer(a):
    '''
    To be implemented
    '''
    return -a


def day11PartOne():
    prg = getInputData()
    print(prg)
    
    answer = "unknown"
    print(f'Solution Day 11, Part one:\nAnswer: {answer} \n\n')


def day11PartTwo():
    answer = "unknown"
    print(f'Solution Day 11, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day11PartOne()
    day11PartTwo()

# Run from terminal:
# $ python day_11#.py
