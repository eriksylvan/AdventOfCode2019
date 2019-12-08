# https://adventofcode.com/2019/day/7

import copy
import itertools
import random
from intcode_computer import IntcodeComputer

inputFile = 'input/07_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getReturnValue(settingList,amplifierInputCopy):
    print(settingList)
    IntComp = IntcodeComputer(amplifierInputCopy)
    val = IntComp.run_program(settingList)
    return val

def maxThrusterSignal(amplifierController):
    thrusterDict={}
    for settingSequence in itertools.permutations([0,1,2,3,4], 5):
        amplifierInputCopy=copy.deepcopy(amplifierController)
        inputValue=0
        for amplifier in range(5):
            output=getReturnValue([settingSequence[amplifier],inputValue],amplifierInputCopy)
            inputValue = output[0]
            print(f'INPUT:{inputValue}')
        thrusterDict[settingSequence]=inputValue
    maxSetting=max(thrusterDict, key=thrusterDict.get)
    maxSignal=max(thrusterDict.values())
    print(thrusterDict)
    print(maxSetting)
    print(maxSignal)
    return maxSignal



def maxThrusterSignalFeedbackLoop(acsProgram):
    thrusterDict={}
    for settingSequence in itertools.permutations([5,6,7,8,9], 5):
        pass
    return 0


def day07PartOne():
    amplifierController = getInputData()
    # print(oMap)
    answer = maxThrusterSignal(amplifierController)
    print(f'Solution Day 07, Part one:\nAnswer: {answer} \n\n')


def day07PartTwo():
    answer = "unknown"
    print(f'Solution Day XX, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day07PartOne()

# Run from terminal:
# $ python day_07.py