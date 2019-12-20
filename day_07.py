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
    '''
    #########################
    #  NOT YEY IMPLEMENTED  #
    #########################
    '''
    thrusterDict={}
    amplifierController = getInputData()

    for seq in itertools.permutations([5,6,7,8,9], 5):

        ICA = IntcodeComputer(amplifierController)
        ICB = IntcodeComputer(amplifierController)
        ICC = IntcodeComputer(amplifierController)    
        ICD = IntcodeComputer(amplifierController)
        ICE = IntcodeComputer(amplifierController)

        ICA.perform_one_operation(input=[seq[0]])
        ICB.perform_one_operation(input=[seq[1]])
        ICC.perform_one_operation(input=[seq[2]])
        ICD.perform_one_operation(input=[seq[3]])
        ICE.perform_one_operation(input=[seq[4]])
        
        terminateE = False
        inA = 0
        step = 0
        while not terminateE:
            step += 1
            print(step)
            stoppedAtInputA = False
            terminateA = False
            stoppedAtInputB = False
            terminateB = False
            stoppedAtInputC = False
            terminateC = False
            stoppedAtInputD = False
            terminateD = False
            stoppedAtInputE = False
            terminateE = False

            while not stoppedAtInputA and not terminateA:
                terminateA, stoppedAtInputA = ICA.perform_one_operation(input=[inA])
            outA = ICA._output.pop()

            while not stoppedAtInputB and not terminateB:
                terminateB, stoppedAtInputB = ICB.perform_one_operation(input=[outA])
            outB = ICB._output.pop()

            while not stoppedAtInputC and not terminateC:
                terminateC, stoppedAtInputC = ICC.perform_one_operation(input=[outB])
            outC = ICC._output.pop()
            
            while not stoppedAtInputD and not terminateD:
                terminateD, stoppedAtInputD = ICD.perform_one_operation(input=[outC])
            outD = ICD._output.pop()
            
            while not stoppedAtInputE and not terminateE:
                terminateE, stoppedAtInputE = ICE.perform_one_operation(input=[outD])
            outE = ICE._output.pop()
            print(terminateE, outE)
            inA = outE
            print(outE)

        thrusterDict[seq]=outE

    maxSetting=max(thrusterDict, key=thrusterDict.get)
    maxSignal=max(thrusterDict.values())
    print(thrusterDict)
    print(maxSetting)
    print(maxSignal)
    return maxSignal

        
    answer = "unknown"
    print(f'Solution Day XX, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    # day07PartOne()
    day07PartTwo()

# Run from terminal:
# $ python day_07.py