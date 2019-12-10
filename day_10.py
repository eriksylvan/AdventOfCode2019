# https://adventofcode.com/2019/day/10

import copy

inputFile = 'input/10_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b using Euclidean algorithm

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def contVisibleAsroids(astroidMap):
    '''
    Not yet implemented
    '''
    print(astroidMap)
    return (len(astroidMap) * len(astroidMap[0]), (0,0))

def day10PartOne():
    answer = "unknown"
    print(f'Solution Day 10, Part one:\nAnswer: {answer} \n\n')


def day10PartTwo():
    answer = "unknown"
    print(f'Solution Day 10, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day10PartOne()
    day10PartTwo()

# Run from terminal:
# $ python day_10.py
