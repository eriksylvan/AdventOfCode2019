# https://adventofcode.com/2019/day/15

import copy
import time
import random
from intcode_computer import IntcodeComputer
from lab_vis import LabVis

inputFile = 'input/15_input'

class RepairDroid():
    def __init__(self, startPostitonX = 0, startPostitonY = 0):
        #self._currentPositionX = startPostitonX   # Cartesian coordinates
        #self._currentPositionY = startPostitonY
        self._currentposition = (startPostitonX, startPostitonY)
        # self._currentDirection = 'U' # The robot starts facing up. (U, D, L, R)
        self._visitedMap = {(startPostitonX,startPostitonY):True} # {position(x,y):visited True/False}
        self._goalpos = (None, None)
        self._goalFound = False
        self._stepsToGoal = 0
        prg = getInputData()
        self.IC = IntcodeComputer(prg)
        self.dir = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)} 

    # north (1) 
    # south (2)
    # west (3)
    # east (4)
    
    def goNorth(self):
        moved, foundGoal = self._go(1)
        if moved: 
            self._currentPositionY -=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX,self._currentPositionY-1)] = False 
        if foundGoal:
            self._goalPosX = self._currentPositionX
            self._goalPosY = self._currentPositionX
            self._goalPosY = True

        return self._currentPositionX, self._currentPositionY, moved

    def goSouth(self):
        moved, foundGoal = self._go(2)
        
        if moved:
            self._currentPositionY +=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX,self._currentPositionY+1)] = False

        if foundGoal:
            self._goalPosX = self._currentPositionX
            self._goalPosY = self._currentPositionX
            self._goalPosY = True

        
        return self._currentPositionX, self._currentPositionY, moved

    def goWest(self):
        
        moved, foundGoal = self._go(3)
        if moved:
            self._currentPositionX -=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX-1,self._currentPositionY)] = False
        if foundGoal:
            self._goalPosX = self._currentPositionX
            self._goalPosY = self._currentPositionX
            self._goalPosY = True


        return self._currentPositionX, self._currentPositionY, moved

    def goEast(self):
        
        moved, foundGoal = self._go(4)
        if moved:
            self._currentPositionX +=1
            self._visitedMap[(self._currentPositionX,self._currentPositionY)] = True
        else:
            self._visitedMap[(self._currentPositionX+1,self._currentPositionY)] = False

        if foundGoal:
            self._goalPosX = self._currentPositionX
            self._goalPosY = self._currentPositionX
            self._goalPosY = True

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
        goalFound = False
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
            self._goalFound = True
            goalFound = True
        else:

            assert False, 'You should not be here'
        return moved, goalFound



    def goExplore(self, fromXY, direction, steps,labytinthDisplay):
        labytinthDisplay.drawLabytinth(self._visitedMap)
        labytinthDisplay.drawDroid(self._currentposition[0],self._currentposition[1])
        if self._goalFound: 
            labytinthDisplay.drawGoal(self._goalpos[0], self._goalpos[1])
            text = self._stepsToGoal
        else:
            text = steps
        labytinthDisplay.drawStart(21,21)
        labytinthDisplay.draw_text(str(text))
        labytinthDisplay.screen_update()
    
        #time.sleep(0.1)
        print(f'xy:{fromXY}')
        
            # north (1) 
            # south (2)
            # west (3)
            # east (4)
            
        def forward(dir):
            return dir

        def left(dir):
            ndir = [-1, 3, 4, 2, 1]
            return ndir[dir]

        def right(dir):
            ndir = [-1, 4, 3, 1, 2]
            return ndir[dir]
        
        def back(dir):
            ndir = [-1, 2, 1, 4, 3]
            return ndir[dir]

        goalFound = False
        print(f'Direction: {direction} = {self.dir[direction]}')
        newXY = (fromXY[0] + self.dir[direction][0],fromXY[1] + self.dir[direction][1]) 
        print(f'ExplorePos: {newXY}')
        print(f'steps: {steps}')
        
        o = self.processInstruction([direction])
        # 0: The repair droid hit a wall. Its position has not changed.
        # 1: The repair droid has moved one step in the requested direction.
        # 2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
        print(f'OUTPUT:{o}')
        if o == 0:
            moved = False
             # self._currentPositionX and self._currentPositionY not changed
            self._visitedMap[newXY] = False # not path
        elif o==1:
            moved = True
            steps += 1
            self._currentposition = newXY
            self._visitedMap[newXY] = True # path!
        elif o==2:
            moved = True
            steps += 1
            self._goalFound = True
            self._currentposition = newXY
            self._visitedMap[newXY] = True # path! and goal
            self._goalpos = newXY
            self._stepsToGoal = steps
            goalFound = True
        else:
            assert False, 'You should not be here'
        
        if moved:
            # left then forward the right... follow thw left wall 
            goalFound = self.goExplore(copy.deepcopy(newXY), left(direction), steps, labytinthDisplay)         # explore to the left
            goalFound = self.goExplore(copy.deepcopy(newXY), forward(direction), steps, labytinthDisplay)      # explore same direction           
            goalFound = self.goExplore(copy.deepcopy(newXY), right(direction), steps, labytinthDisplay)        # explore to the right
            
            # wrong way, go back to where you came from
            o = self.processInstruction([back(direction)])
            self._currentposition = fromXY
            steps -=1 

        
        return goalFound
# END class RepairDroid():





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

    
    droid = RepairDroid(21, 21)
    labytinthDisplay = LabVis(41,41,20)
    labytinthDisplay.drawLabytinth(droid._visitedMap)
    labytinthDisplay.drawStart(21,21)
    steps = 0
    droid.goExplore(droid._currentposition, 1, steps, labytinthDisplay) # start explore north=1
    droid.goExplore(droid._currentposition, 2, steps, labytinthDisplay) 
    droid.goExplore(droid._currentposition, 3, steps, labytinthDisplay) 
    droid.goExplore(droid._currentposition, 4, steps, labytinthDisplay) 

    input('pause')
    with open('day_15_labyrinthDict', 'w') as f:
        print(droid._visitedMap, file=f) 
    # Saves labyrint representes as dict, read with:
    # with open('day_15_labyrinthDict', 'r') as f: content = f.read(); dic = eval(content);
    return droid._stepsToGoal
    


def runDroid_random():
    droid = RepairDroid(25, 25)
    labytinthDisplay = LabVis(50,50,10)
    labytinthDisplay.drawLabytinth(droid._visitedMap)

    

    while True:
        ###### Random Walker:
        r = random.randint(1,4)
        if r==1: droid.goNorth()
        elif r==2: droid.goSouth()
        elif r==3: droid.goEast()
        else: droid.goWest()
        ######

        labytinthDisplay.drawLabytinth(droid._visitedMap)
        labytinthDisplay.drawDroid(droid._currentposition[0],droid._currentposition[1])
        if droid._goalFound: labytinthDisplay.drawGoal(droid._goalPosX, droid._goalPosY)
        labytinthDisplay.screen_update()
        #time.sleep(0.1)



def dict2maze():
    pass

def maze2graph(maze):
    print(maze)
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {}
    print(height,width)
    for j in range(height): 
        for i in range(width): 
            if maze[i][j]:
                graph[(i, j)] = [] 
    print(graph)
    

    for row, col in graph.keys():
        if row < height - 1 and maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def dict2MazeStr(dictionary):
    width = max([w[0] for w in dictionary])
    height = max([h[1] for h in dictionary])
    print(f'w={width}, h={height}')
    mazeStr='' 
    for h in range(height+1):
        for w in range(width+1):
            if (w,h) in dictionary:
                if dictionary[(w,h)]:
                    mazeStr += '.'
                else:
                    mazeStr += '#'
            else:
                mazeStr += '#'
        mazeStr += '\n'
    print(mazeStr)        
    with open('day_15_labyrinthStr', 'w') as f:
        print(mazeStr, file=f) 
    return mazeStr

def mazeStrFile2MazeMatrix(inputFile):
    print(inputFile)
    mazeMatrix = []
    with open(inputFile) as input:
        for line in input:
            mazeMatrix.append([ch=='.' for ch in str(line).strip()])
    return mazeMatrix





def day15PartOne():
    answer = runDroid()
    print(f'Solution Day 15, Part one:\nNumber of steps to the oxygen system: {answer} \n\n')


def day15PartTwo():
    
    with open('day_15_labyrinthDict', 'r') as f: 
        content = f.read()
        dictionary = eval(content)

    #dict2MazeGraph(dictionary)

    answer = "unknown"
    print(f'Solution Day 15, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    # day15PartOne()
    # day15PartTwo()
    # runDroid_random()

    mazeMatrix = mazeStrFile2MazeMatrix('day_15_labyrinthStr')
    graph = maze2graph(mazeMatrix)
    print(graph) 


# Run from terminal:
# $ python day_15.py



##############
#  LINKS


# http://bryukh.com/labyrinth-algorithms/
# https://runestone.academy/runestone/books/published/pythonds/Recursion/ExploringaMaze.html

