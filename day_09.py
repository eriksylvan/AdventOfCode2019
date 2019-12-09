# https://adventofcode.com/2019/day/9

import copy
from intcode_computer import IntcodeComputer

inputFile = 'input/09_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def BOOSTkeycode(intOpPrg,input):
    IntComp = IntcodeComputer(intOpPrg)
    keycode = IntComp.run_program(inp = input)
    return keycode


def day09PartOne():
    intOpPrg = getInputData()
    answer = BOOSTkeycode(intOpPrg,[1])

    print(f'Solution Day 09, Part one:\nAnswer: {answer} \n\n')


def day09PartTwo():
    answer = "unknown"
    print(f'Solution Day 09, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day09PartOne()
    day09PartTwo()

# Run from terminal:
# $ python day_09.py

# Solution Day 09, Part one:
# Answer: [3241900951]