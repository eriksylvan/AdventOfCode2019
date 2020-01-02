# https://adventofcode.com/2019/day/2

import copy

inputFile = 'input/02_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    intCodeProgram = []
    with open(inputFile) as input:
        for line in input:
            intCodeProgram = [int(x) for x in line.split(',')]
    return intCodeProgram


def intcode(intCodeProgram):
    '''Performs an Intcode program

    Parameters:
    intCodeProgram (int[]): initial state for the memory

    Returns:
    intCodeProgram (int[]): the final state for the memory
    '''
    position = 0
    while intCodeProgram[position] != 99:
        opcode = intCodeProgram[position]
        value1 = intCodeProgram[intCodeProgram[position+1]]
        value2 = intCodeProgram[intCodeProgram[position+2]]
        outputPosition = intCodeProgram[position+3]
        if opcode == 1:
            intCodeProgram[outputPosition] = value1+value2
        elif opcode == 2:
            intCodeProgram[outputPosition] = value1*value2
        position = position+4
    return(intCodeProgram)


def day02PartOne():

    intCodeProgram = getInputData()
    print(intCodeProgram)
    intCodeProgram[1] = 12
    intCodeProgram[2] = 2
    intCodeProgram = intcode(intCodeProgram)

    print(
        f'Solution Day 02, Part one:\nThe first code in the program is: {intCodeProgram[0]} \n\n')


def day02PartTwo():

    intCodeProgram = getInputData()
    exitLoops = False
    for noun in range(100):
        for verb in range(100):
            alteredCodeProgram = copy.deepcopy(intCodeProgram)
            alteredCodeProgram[1] = noun
            alteredCodeProgram[2] = verb
            alteredCodeProgram = intcode(alteredCodeProgram)
            exitLoops = alteredCodeProgram[0] == 19690720
            if exitLoops:
                break
        if exitLoops:
            break
    result = 100*noun+verb
    print(
        f'Solution Day 02, Part one:\nThe first code in the program is 19690720 for (noun {noun}, verb {verb} ), \nthis gives the result: {result} \n\n')


if __name__ == "__main__":
    day02PartOne()
    day02PartTwo()

# Run from terminal:
# $ python day_02.py
