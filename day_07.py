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


def test():
    prg = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    thrusterDict={}
    for seq in itertools.permutations([5,6,7,8,9], 5):
        print(f'----- {seq} -----')
        ICA = IntcodeComputer(prg)
        ICB = IntcodeComputer(prg)
        ICC = IntcodeComputer(prg)    
        ICD = IntcodeComputer(prg)
        ICE = IntcodeComputer(prg)
        signal = runOneSeq(ICA, ICB, ICC, ICD, ICE, seq)
        thrusterDict[seq]=signal

    maxSetting=max(thrusterDict, key=thrusterDict.get)
    maxSignal=max(thrusterDict.values())
    print(thrusterDict)
    print(maxSetting)
    print(maxSignal)
    return signal


def runOneSeq(ICA, ICB, ICC, ICD, ICE, seqT):
    
    inputA = [seqT[0]]
    inputB = [seqT[1]]
    inputC = [seqT[2]]
    inputD = [seqT[3]]
    inputE = [seqT[4]]
    
    
    ICA.perform_one_operation(input=inputA, stopAtInput=True)
    ICB.perform_one_operation(input=inputB, stopAtInput=True)
    ICC.perform_one_operation(input=inputC, stopAtInput=True)
    ICD.perform_one_operation(input=inputD, stopAtInput=True)
    ICE.perform_one_operation(input=inputE, stopAtInput=True)
    # print(f'A:{ICA._output}')
    # print(f'B:{ICB._output}')
    # print(f'C:{ICC._output}')
    # print(f'D:{ICD._output}')
    # print(f'E:{ICE._output}')
    terminateE = False
    inputA.append(0)
    step = 0
    while not terminateE:
        step += 1
        # print(f'step: {step}')
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

        # print('A')
        while not stoppedAtInputA and not terminateA:
            terminateA, stoppedAtInputA = ICA.perform_one_operation(input=inputA,stopAtInput=True)
            # terminateA, stoppedAtInputA = ICA.perform_one_operation()
        outA = ICA._output.pop()
        inputB.append(outA)
        # print(f'A:{outA}, {terminateA}, {stoppedAtInputA}')

        # print('B')
        while not stoppedAtInputB and not terminateB:
            terminateB, stoppedAtInputB = ICB.perform_one_operation(input=inputB, stopAtInput=True)
            # terminateB, stoppedAtInputB = ICB.perform_one_operation()
        outB = ICB._output.pop()
        inputC.append(outB)
        # print(f'B:{outB}, {terminateB}, {stoppedAtInputB}')

        # print('C')
        while not stoppedAtInputC and not terminateC:
            terminateC, stoppedAtInputC = ICC.perform_one_operation(input=inputC, stopAtInput=True)
            # terminateC, stoppedAtInputC = ICC.perform_one_operation()
        outC = ICC._output.pop()
        inputD.append(outC)
        # print(f'C:{outC} , {terminateC}, {stoppedAtInputC}')


        # print('D')
        while not stoppedAtInputD and not terminateD:
            terminateD, stoppedAtInputD = ICD.perform_one_operation(input=inputD, stopAtInput=True)
            # terminateD, stoppedAtInputD = ICD.perform_one_operation()
        outD = ICD._output.pop()
        inputE.append(outD)
        # print(f'D:{outD}, {terminateD}, {stoppedAtInputD}')

        # print('E')
        while not stoppedAtInputE and not terminateE:
            terminateE, stoppedAtInputE = ICE.perform_one_operation(input=inputE, stopAtInput=True)
            # terminateE, stoppedAtInputE = ICD.perform_one_operation()
        
        outE = ICE._output.pop()
        inputA.append(outE)
        # print(f'E:{outE}, {terminateE}, {stoppedAtInputE}')
    return outE

#####################
def test_igen():
    prg = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    IC = IntcodeComputer(prg)
    inp = [5,0,100]
    stoppedAtInput = False 
    terminate = False
    print(IC._intCodeProgramDict)
    print(IC._output)
    while not stoppedAtInput and not terminate:
        terminate, stoppedAtInput = IC.perform_one_operation(input=inp)
        print(IC._intCodeProgramDict)
        print(IC._output)
    
#####################


def day07PartTwo():
    thrusterDict={}
    amplifierController = getInputData()
    for seq in itertools.permutations([5,6,7,8,9], 5):
        print(f'----- {seq} -----')
        ICA = IntcodeComputer(amplifierController)
        ICB = IntcodeComputer(amplifierController)
        ICC = IntcodeComputer(amplifierController)    
        ICD = IntcodeComputer(amplifierController)
        ICE = IntcodeComputer(amplifierController)
        signal = runOneSeq(ICA, ICB, ICC, ICD, ICE, seq)
        print(f'-  {signal}  -')
        thrusterDict[seq]=signal

    maxSetting=max(thrusterDict, key=thrusterDict.get)
    maxSignal=max(thrusterDict.values())
    print(thrusterDict)
    print(maxSetting)
    print(maxSignal)

    print(f'Solution Day 07, Part two:\nAnswer: Amp.dettings:{maxSetting} --> signal:{maxSignal},  \n\n')

    return signal


def day07PartTwo_old():
    '''
    #########################
    #  NOT YEY IMPLEMENTED  #
    #########################
    '''
    thrusterDict={}
    amplifierController = getInputData()
    # l = [itertools.permutations([5,6,7,8,9], 5)]
    # print(l)
    # input()
    for seq in itertools.permutations([5,6,7,8,9], 5):
        print(f'----- {seq} -----')
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
            print(f'A:{outA}, {terminateA}, {stoppedAtInputA}')

            while not stoppedAtInputB and not terminateB:
                terminateB, stoppedAtInputB = ICB.perform_one_operation(input=[outA])
            outB = ICB._output.pop()
            print(f'B:{outB}, {terminateB}, {stoppedAtInputB}')

            while not stoppedAtInputC and not terminateC:
                terminateC, stoppedAtInputC = ICC.perform_one_operation(input=[outB])
            outC = ICC._output.pop()
            print(f'C:{outC} , {terminateC}, {stoppedAtInputC}')


            while not stoppedAtInputD and not terminateD:
                terminateD, stoppedAtInputD = ICD.perform_one_operation(input=[outC])
            outD = ICD._output.pop()
            print(f'D:{outD}, {terminateD}, {stoppedAtInputD}')

            while not stoppedAtInputE and not terminateE:
                terminateE, stoppedAtInputE = ICE.perform_one_operation(input=[outD])
            outE = ICE._output.pop()
            print(f'E:{outE}, {terminateE}, {stoppedAtInputE}')
            inA = outE


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
    # test()
    # test_igen()
# $ python day_07.py