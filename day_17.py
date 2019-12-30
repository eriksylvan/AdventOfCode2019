# https://adventofcode.com/2019/day/17

import copy
from intcode_computer import IntcodeComputer
import re   # regular expression


inputFile = 'input/17_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def cameraOutput(defaultColor=0):
    code = getInputData()
    IC = IntcodeComputer(code)
    


    step=0
    inp=[]
    IC._output = []    # Clear the output list
    terminate = False
    stoppedAtInput = False
    while not terminate:
        while not stoppedAtInput and not terminate:
            terminate, stoppedAtInput = IC.perform_one_operation(IC._memoryPosition, inp, stopAtInput = True) 
        step +=1
        # print(f'### STEP {step} ###')
        # print(f'OutPut{IC._output}')
        # print(f'OutPut{IC._output}')        
        stoppedAtInput = False

    ret = decodeMap(IC._output)    
    # ret = []
    # row = ''
    # for ascii in IC._output:
    #     if str(ascii) == '10': 
    #         ret.append(row)
    #         row = ''
    #     else:
    #         row += chr(ascii)
    return ret

def decodeMap(mapList):
    ret = []
    row = ''
    for ascii in mapList:
        if str(ascii) == '10': 
            ret.append(row)
            row = ''
        else:
            row += chr(ascii)
    return ret

def findIntersections(map):
    length = len(map[0])
    hight = len(map)
    # p = re.compile('[.][.][.]')
    # r = re.compile('[.][^.][.]')
    ret = []

    for r in range(1, hight-1):
        for c in range(1, length-1):
            # print(map[r-1][c-1:c+2])
            # print(map[r][c-1:c+2])
            # print(map[r+1][c-1:c+2])
            # print(f'---   ({r},{c})')

            if re.match('[.][^.][.]', map[r-1][c-1:c+2]) and  \
                re.match('[^.][^.][^.]', map[r][c-1:c+2]) and \
                re.match('[.][^.][.]', map[r+1][c-1:c+2]):
                    ret.append((r,c))
    return ret

def calcAlignmentParameters(map):
    inter = findIntersections(map)
    ret = 0
    for t in inter: ret += t[0] *t[1]
    return ret

##############################################################
# Part 2

class Robot():
    def __init__(self, xy, d):
        self._xPos = xy[0]
        self._yPos = xy[1]
        self._direction = d # ^ > v <
    
    def moveForward(self, steps = 1):
        if self._direction == '^':
            self._yPos -= 1
        elif self._direction == '>':
            self._xPos += 1
        elif self._direction == 'v':
            self._yPos += 1
        elif self._direction == '<':
            self._xPos -= 1
        else: 
            assert False, f'Invalid direction: {self._direction}'
            
        return (self._xPos, self._yPos), self._direction

    def turnLeft(self):
        #print("turnLeft")
        if self._direction == '^':
            self._direction = '<'
        elif self._direction == '>':
            self._direction = '^'
        elif self._direction == 'v':
            self._direction = '>'
        elif self._direction == '<':
            self._direction = 'v'
        return (self._xPos, self._yPos), self._direction
    
    def turnRight(self):
        #print("turnRight")
        if self._direction == '^':
            self._direction = '>'
        elif self._direction == '>':
            self._direction = 'v'
        elif self._direction == 'v':
            self._direction = '<'
        elif self._direction == '<':
            self._direction = '^'
        return (self._xPos, self._yPos), self._direction
        

def printMap(map):
    for r in map:
        print(r)


def findRobot(map):
    for i, row in enumerate(map):
        for j, ch in enumerate(row):
            if re.match('[\^>v<]', ch):
                return (j,i), ch
    return None, None

def followPath(map):
    stepcounter = 0
    stepSequence = '' 
    pos, d = findRobot(map)
    robot = Robot(pos, d)
    
    while True:
        # input()
        x = pos[0]
        y = pos[1]
        try:
            if d == '^':
                
                inLeft = (x-1, y)
                inFront =  (x, y-1)
                inRight = (x+1, y)

            elif d == '>':

                inLeft = (x, y-1)
                inFront =  (x+1, y)
                inRight = (x, y+1)

            elif d == 'v':
                
                inLeft = (x+1, y)
                inFront =  (x, y+1)
                inRight = (x-1, y)

            elif d == '<':            
                inLeft = (x, y+1)
                inFront =  (x-1, y)
                inRight = (x, y-1)
            else: 
                pass
        except Exception as e:  # Out of range exception
            pass


        inLeftX = inLeft[0] 
        inFrontX = inFront[0]
        inRightX = inRight[0]
        inLeftY = inLeft[1] 
        inFrontY = inFront[1]
        inRightY = inRight[1]
        


        if inLeftX < 0: inLeftX = None 
        if inFrontX < 0: inFrontX = None
        if inRightX < 0: inRightX = None
        if inLeftY  < 0: inLeftY = None 
        if inFrontY < 0: inFrontY = None
        if inRightY < 0: inRightY = None
        

        try:     
            inFrontCh = map[inFrontY][inFrontX]
        except Exception as e:
            # print('BOOM F')
            inFrontCh = 'w'

        try:
            inLeftCh = map[inLeftY][inLeftX]
        except Exception as e:
            # print('BOOM L')
            inLeftCh = 'w'
        try:
            inRightCh = map[inRightY][inRightX]
        except Exception as e:
            # print('BOOM R')
            inRightCh = 'w'

        # print(f'--  {d}  -- pos({pos})')
        
        # print(inLeftCh, inFrontCh, inRightCh)
        # print(inLeft, inFront, inRight)
      

        if inFrontCh == 'w' or inFrontCh == '.':
            # turn
            # save turn
            if inLeftCh == '#':
                #turn left
                turn = 'L'
                pos, d = robot.turnLeft()
                
            elif inRightCh == '#':
                #turn right
                turn = 'R'
                pos, d = robot.turnRight()
            else:
                # nowhere to turn, stop
                stepSequence += str(stepcounter)  
                break

            if stepcounter != 0:
                stepSequence += str(stepcounter)        
            stepSequence += turn
            stepcounter = 0
            

        else:
            # go straight "
            # count step
            stepcounter += 1
            pos, d = robot.moveForward()
       
    return stepSequence

def doTheSpacewalk():
    code = getInputData()
    IC = IntcodeComputer(code)
    IC._intCodeProgramDict[0] = 2 # orce the vacuum robot to wake up by changing the value in your ASCII program at address 0 from 1 to 2
    # print(IC._intCodeProgramDict)
    M = 'A,B,A,B,A,C,B,C,A,C\n'
    A = 'L,10,L,12,R,6\n'
    B = 'R,10,L,4,L,4,L,12\n'
    C = 'L,10,R,10,R,6,L,4\n'
    F = 'n\n' # continuous video feed; provide either y or n and a newline
    Ml = [ord(ch) for ch in M]
    Al = [ord(ch) for ch in A]
    Bl = [ord(ch) for ch in B]
    Cl = [ord(ch) for ch in C]
    Fl = [ord(ch) for ch in F]
    input = Ml + Al + Bl + Cl + Fl
    # print(input) 
    output = IC.run_program(input)
    # print(output)
    map = decodeMap(output[:-1])
    printMap(map)
    return output[-1] # amount of space dust it collected as a large, non-ASCII value in a single output instruction.

def day17PartOne():
    map = cameraOutput()
    alPar = calcAlignmentParameters(map)
    printMap(map)
    print('\n\n')
    print(f'Solution Day 17, Part one:\Sum of the alignment parameters: {alPar} \n\n')


def day17PartTwo():
    map = cameraOutput()
    print(f'Robot start position and direction: {findRobot(map)}\n')
    s = followPath(map)
    print(f'Robot movement sequence:\n{s}\n')
    '''
    I was not able to find an algoritm to compress the sequence.
    I had to do it manually:
    A = L10L12R6
    B = R10L4L4L12
    A = L10L12R6
    B = R10L4L4L12
    A = L10L12R6
    C = L10R10R6L4
    B = R10L4L4L12
    C = L10R10R6L4
    A = L10L12R6
    C = L10R10R6L4
    '''
    answer = doTheSpacewalk()
    print(f'Solution Day 17, Part two:\nAmount od spacedust: {answer} \n\n')



if __name__ == "__main__":
    day17PartOne()
    day17PartTwo()

# Run from terminal:
# $ python day_17.py


# Solution Day 17, Part one:
# Answer: 2508