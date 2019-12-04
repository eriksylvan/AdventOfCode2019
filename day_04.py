# https://adventofcode.com/2019/day/4

import copy

# inputFile = ''


def getInputData():
    '''
    Returns input data. 
    The range within the passwors are valid
    '''
    limits = (357253, 892942)
    return limits

def isValidPassword(password):
    '''     To be implemented     '''
    
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

    return False

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
