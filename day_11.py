# https://adventofcode.com/2019/day/11

import random
import copy
from intcode_computer import IntcodeComputer


inputFile = 'input/11_input'

class SolarPanelMap:
    def __init__(self):
        self._currentPositionX = 0   # Cartesian coordinates
        self._currentPositionY = 0
        self._currentDirection = 'U' # The robot starts facing up. (U, D, L, R)
        self._panelMap = {(0,0):0} # {position(x,y):color 0=black 1=white}

    def moveForward(self):
        if self._currentDirection == 'U':
            self._currentPositionY -= 1   # y-1 
        elif self._currentDirection == 'D':
            self._currentPositionY += 1   # y+1 
        elif self._currentDirection == 'L':
            self._currentPositionX -= 1   # x-1 
        elif self._currentDirection == 'R':
            self._currentPositionX += 1   # x + 1 
        else:
            assert False, 'Direction error'
        if not (self._currentPositionX, self._currentPositionY) in self._panelMap: 
            self._panelMap[(self._currentPositionX, self._currentPositionY)] = 0 # add black 

    def turnLeft(self):
        if self._currentDirection == 'U':
            self._currentDirection = 'L'

        elif self._currentDirection == 'D':
            self._currentDirection = 'R'

        elif self._currentDirection == 'L':
            self._currentDirection = 'D' 

        elif self._currentDirection == 'R':
            self._currentDirection = 'U'  
        else:
            assert False, 'Direction error'

    def turnRight(self):
        if self._currentDirection == 'U':
            self._currentDirection = 'R'

        elif self._currentDirection == 'D':
            self._currentDirection = 'L'

        elif self._currentDirection == 'L':
            self._currentDirection = 'U' 
            
        elif self._currentDirection == 'R':
            self._currentDirection = 'D'  
        else:
            assert False, 'Direction error'
    
    def paintBlack(self):
        self._panelMap[(self._currentPositionX,self._currentPositionY)] = 0

    def paintWhite(self):
        self._panelMap[(self._currentPositionX,self._currentPositionY)] = 1

    def getColor(self):
        return self._panelMap.get((self._currentPositionX,self._currentPositionY))


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getAnwer(a):
    '''
    To be implemented
    '''
    return -a


def day11PartOne():
    prg = getInputData()
    print(prg)
    
    answer = "unknown"
    print(f'Solution Day 11, Part one:\nAnswer: {answer} \n\n')


def day11PartTwo():
    answer = "unknown"
    print(f'Solution Day 11, Part two:\nAnswer: {answer} \n\n')

def startRobot():
    code = getInputData()
    IC = IntcodeComputer(code)
    

    robotOnMap = SolarPanelMap()

    step=0
    inp=[0]
    IC._output = []    # Clear the output list
    terminate = False
    stoppedAtInput = False
    while not terminate:
        while not stoppedAtInput and not terminate:
            terminate, stoppedAtInput = IC.perform_one_operation(IC._memoryPosition, inp, stopAtInput = True) 
        step +=1
        # print(f'### STEP {step} ###')
        # print(f'OutPut{IC._output}')
        paintBlack = IC._output.pop(0) == 0
        # print(f'OutPut{IC._output}')        

        turnLeft = (IC._output.pop(0) == 0)
        # print(f'OutPut{IC._output}')
        
        if paintBlack: 
            robotOnMap.paintBlack()
        else:
            robotOnMap.paintWhite()

        if turnLeft:
            robotOnMap.turnLeft()
        else:
            robotOnMap.turnRight()
        
        robotOnMap.moveForward()
        
        color = robotOnMap.getColor() # 0=black, 1=white
        inp = [color]
        stoppedAtInput = False
    
    print(f'Robot: {len(robotOnMap._panelMap)}')



if __name__ == "__main__":
    startRobot()

    # day11PartOne()
    # day11PartTwo()

# Run from terminal:
# $ python day_11#.py

