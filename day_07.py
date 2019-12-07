# https://adventofcode.com/2019/day/7

import copy
import itertools
import random

inputFile = 'input/07_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getReturnValue(settingList,amplifierInputCopy):
    return random.randint(0,9)

def maxThrusterSignal(amplifierController):
    thrusterDict={}
    for settingSequence in itertools.permutations([0,1,2,3,4], 5):
        amplifierInputCopy=copy.deepcopy(amplifierController)
        inputOutputValue=0
        for amplifier in range(5):
            inputOutputValue=getReturnValue([settingSequence[amplifier],inputOutputValue],amplifierInputCopy)
        thrusterDict[settingSequence]=inputOutputValue
    maxSetting=max(thrusterDict, key=thrusterDict.get)
    maxSignal=max(thrusterDict.values())
    print(maxSetting)
    print(maxSignal)
    return maxSignal

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