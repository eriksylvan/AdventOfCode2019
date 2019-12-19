# https://adventofcode.com/2019/day/19

import copy
from intcode_computer import IntcodeComputer

inputFile = 'input/19_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def drone():
    code = getInputData()
    # IC = IntcodeComputer(code)
#    out = {}
    pic = []
    count = 0
    for y in range(50):
        row = ''
        for x in range(50):
            IC = IntcodeComputer(code)
            o = IC.run_program([x,y])
            if o[0] == 1:
                count +=1
                row += '#'
            else:
                row += '.'
            
        pic.append(row)

    # print(out)
    for r in pic: print(r)
    
    return count
    
def getAnwer(v):
    return -v*v

def day19PartOne():
    answer = drone()
    print(f'Solution Day 19, Part one:\nTractor beam affects: {answer} positions within 50x50 range \n\n')


def day19PartTwo():
    answer = "unknown"
    print(f'Solution Day 19, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    # drone()
    day19PartOne()
    day19PartTwo()

# Run from terminal:
# $ python day_19.py
