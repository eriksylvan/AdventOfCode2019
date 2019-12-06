# https://adventofcode.com/2019/day/6

import copy

inputFile = 'input/06_input'


def getInputData():
    '''Reads the input file end returns the data in a list of strings'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data.append(str(line).replace('\n','').replace('\r',''))
    return data

def noOfOrbits(orbitMap):
    '''
    To be implemented
    '''
    return(len(orbitMap))


def day06PartOne():
    oMap = getInputData()
    # print(oMap)
    answer = noOfOrbits(oMap)
    print(f'Solution Day 06, Part one:\nAnswer: {answer} \n\n')


def day06PartTwo():
    answer = "unknown"
    print(f'Solution Day 06, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day06PartOne()
    day06PartTwo()

# Run from terminal:
# $ python day_06.py
