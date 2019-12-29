# https://adventofcode.com/2019/day/25

import copy
from intcode_computer import IntcodeComputer 

inputFile = 'input/25_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data


def ascii2str(asciiList):
    outStr = ""
    for i in asciiList:
        if i > 128: # if not ascii value
            outStr+=f'\nAmount of damage to the hull:{i}\n'
        else:
            outStr+=chr(i)
    return outStr

def str2asciiList(inpStr):
    return [ord(c) for c in inpStr]


def runDroid(instructions):
    trystring = getTryStr()
    droidController = getInputData()
    IC = IntcodeComputer(droidController)
    saved_Controller = copy.deepcopy(IC._intCodeProgramDict)
    saved_memPos = copy.deepcopy(IC._memoryPosition)
    saved_relativeBase = copy.deepcopy(IC._relativeBase)
    inp = []
    stoppedAtInput = False
    terminated = False
    autotry = False

    while not terminated:
        # print(inp)
        # print(terminated, stoppedAtInput)
        while not terminated and not stoppedAtInput:
            terminated, stoppedAtInput = IC.perform_one_operation(input=inp,stopAtInput=True)
            #print('hej')
    
        if stoppedAtInput:
            outCode = IC._output
            print(ascii2str(outCode))
            if not autotry: inpStr = input('> ')
            if inpStr == 'save':
                saved_Controller = copy.deepcopy(IC._intCodeProgramDict)
                saved_memPos = copy.deepcopy(IC._memoryPosition)
                print('\nGame saved\n\n')
                f = open("25save", "w")
                f.write("Now the file has more content!")
                f.close()
                inpStr = input('> ')
            if inpStr == 'load':
                IC._intCodeProgramDict = copy.deepcopy(saved_Controller)
                IC._memoryPosition = copy.deepcopy(saved_memPos) 
                IC._relativeBase = copy.deepcopy(saved_relativeBase)
                print('\nGame loaded\n\n')
                #outCode = IC._output
                #print(ascii2str(outCode))
                inpStr = input('> ')
            if inpStr == 'FF':
                inpStr = 'south\nwest\nnorth\ntake fuel cell\nsouth\neast\nnorth\nnorth\neast\ntake candy cane\nsouth\ntake hypercube\nnorth\nwest\nnorth\ntake coin\neast\ntake tambourine\nwest\nwest\ntake spool of cat6\nnorth\ntake weather machine\nwest\ntake mutex\nwest\ndrop spool of cat6\ndrop hypercube\ndrop weather machine\ndrop coin\ndrop candy cane\ndrop tambourine\ndrop fuel cell\ndrop mutex\ninv'
            if inpStr == 'autotry':
                autotry = True
                inpStr = '\nwest'
            if autotry:
                inpStr = trystring.pop(0) # pop first item
                print(inpStr)
            print('\n')
            inp = str2asciiList(inpStr + '\n')
            stoppedAtInput = False
    outCode = IC._output
    outstr = ascii2str(outCode)
    if outstr.find('Alert'):
        print('****** ALERT *********')
        
    print(outstr)
    return outstr

def getTryStr():
    import itertools

    items = ('spool of cat6', 
                'hypercube',
                'weather machine',
                'coin',
                'candy cane',
                'tambourine',
                'fuel cell',
                'mutex')

    def combs(x):
        return [c for i in range(len(x)+1) for c in itertools.combinations(x,i)]

    allCombinations = combs(items)

    trystring = []
    for i in allCombinations:
        print('-== next try ==-')
        takeString =''
        dropString =''
        for item in i:
            takeString += f'take {item}\n'
            dropString += f'drop {item}\n'
        print(takeString)
        print(dropString)
        trystring.append(takeString)
        trystring.append('west\n')
        trystring.append(dropString)
    return trystring



def day25PartOne():
    runDroid([])
    answer = "unknown"
    print(f'Solution Day 25, Part one:\nAnswer: {answer} \n\n')


def day25PartTwo():
    answer = "unknown"
    print(f'Solution Day 25, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day25PartOne()
    # day25PartTwo()



# Run from terminal:
# $ python day_25.py



# You take the spool of cat6.
# You take the hypercube.
# You take the weather machine.
# You take the tambourine.

# A loud, robotic voice says "Analysis complete! You may proceed." and you enter the cockpit.
# Santa notices your small droid, looks puzzled for a moment, realizes what has happened, and radios your ship directly.
# "Oh, hello! You should be able to get in by typing 84410376 on the keypad at the main airlock."
