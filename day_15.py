# https://adventofcode.com/2019/day/15

import copy
import time
import random
from intcode_computer import IntcodeComputer
from lab_vis import LabVis

inputFile = 'input/15_input'

class RepairDroid():
    def __init__(self, startPostitonX = 0, startPostitonY = 0):
        self._currentPositionX = startPostitonX   # Cartesian coordinates
        self._currentPositionY = startPostitonY
        # self._currentDirection = 'U' # The robot starts facing up. (U, D, L, R)
        self._visitedMap = {(startPostitonX,startPostitonY):True} # {position(x,y):visited True/False}
        self.goalPosX = None
        self.goalPosY = None
        self.goalFound = False
        prg = getInputData()
        self.IC = IntcodeComputer(prg)


    # north (1) 
    # south (2)
    # west (3)
    # east (4)
    
    def goNorth(self):
        moved = self._go(1)
        foundGoal = False
        if moved: 
            self._currentPositionY -=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX,self._currentPositionY-1)] = False 
        return self._currentPositionX, self._currentPositionY, moved

    def goSouth(self):
        moved = self._go(2)
        if moved:
            self._currentPositionY +=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX,self._currentPositionY+1)] = False
        return self._currentPositionX, self._currentPositionY, moved

    def goWest(self):
        moved = self._go(3)
        if moved:
            self._currentPositionX -=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX-1,self._currentPositionY)] = False
        return self._currentPositionX, self._currentPositionY, moved

    def goEast(self):
        moved = self._go(4)
        if moved:
            self._currentPositionX +=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX+1,self._currentPositionY)] = False
        return self._currentPositionX, self._currentPositionY, moved

    def processInstruction(self, instr):      
        stoppedAtInput = False
        terminated = False
        while not terminated:
            print(f'entering whileLoop:{terminated}, {stoppedAtInput}\n')
            while not terminated and not stoppedAtInput:
                terminated, stoppedAtInput = self.IC.perform_one_operation(input=instr,stopAtInput=True)
                
        
            if stoppedAtInput:
                print('Time to stop, input.')
                break
       # print(f'Outside loop:{terminated}, {stoppedAtInput}')        
       # print(f'OUTPUT:self.IC._output')
        o=""
        if len(self.IC._output) > 0:
       #    print('popping')
            o = self.IC._output.pop()
        return o

    def _go(self, dir):
        o = self.processInstruction([dir])
        # 0: The repair droid hit a wall. Its position has not changed.
        # 1: The repair droid has moved one step in the requested direction.
        # 2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
        print(f'OUTPUT:{o}')
        if o == 0:
            moved = False
        elif o==1:
            moved = True
        elif o==2:
            moved = True
            self.goalFound = True
        else:

            assert False, 'You should not be here'
        return moved
        

def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

def getAnwer(x):
    return x*x


def runDroid():
    droid = RepairDroid(25, 25)
    labytinthDisplay = LabVis(50,50,10)
    labytinthDisplay.drawLabytinth(droid._visitedMap)


    x, y, moved = droid.goNorth()
    print('North')
    print(x, y, moved)
    

    x, y, moved = droid.goSouth()
    print('South')
    print(x, y, moved)

    x, y, moved = droid.goEast()
    print('East')
    print(x, y, moved)
    
    x, y, moved = droid.goWest()
    print('West')
    print(x, y, moved)
    print(droid._visitedMap)
    droid.goEast()
    droid.goEast()
    droid.goEast()
    droid.goSouth()
    droid.goSouth()
    droid.goSouth()

    while True:
        r = random.randint(1,4)
        if r==1: droid.goNorth()
        elif r==2: droid.goSouth()
        elif r==3: droid.goEast()
        else: droid.goWest()

        

        labytinthDisplay.drawLabytinth(droid._visitedMap)
        labytinthDisplay.drawDroid(droid._currentPositionX,droid._currentPositionY)
        labytinthDisplay.screen_update()
        #time.sleep(0.1)


def day15PartOne():
    answer = "unknown"
    print(f'Solution Day 15, Part one:\nAnswer: {answer} \n\n')


def day15PartTwo():
    answer = "unknown"
    print(f'Solution Day 15, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    # day15PartOne()
    # day15PartTwo()
    runDroid()


# Run from terminal:
# $ python day_15.py



##############
#  LINKS


# http://bryukh.com/labyrinth-algorithms/
# https://runestone.academy/runestone/books/published/pythonds/Recursion/ExploringaMaze.html
