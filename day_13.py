# https://adventofcode.com/2019/day/13

import copy
import time

from intcode_computer import IntcodeComputer

import math 
from PIL import Image, ImageDraw 

inputFile = 'input/13_input'


# class PygameGameScreen():
#     import pygame    

#     def __init__(self):
#         pygame.init()
#         self._screen = pygame.display.set_mode((400, 300))
#         self.size = 20

#     def drawBoard(self, x,y,t):
#         pygame.draw.rect(self._screen, pygame.Color.b, pygame.Rect(x * self.size, y * self.size, 60, 60))
        
class PILScreen():
    def __init__(self):
        # creating new Image object 
        side = 20
        self._side = side
        w = 42 * side+1
        h = 600 
        self._img = Image.new("RGB", (w, h)) 
        self._imgD = ImageDraw.Draw(self._img) 
        self._side = 20
        
        
        
    def drawBrick(self ,x ,y ,t):
        shape = [(self._side * x, self._side * y), ((self._side * x + self._side, self._side * y + self._side))]
        if t == 1:
            self._imgD.rectangle(shape, fill="gray", outline="red")
        elif t == 2:
            self._imgD.rectangle(shape, fill="yellow", outline="red")
        elif t == 3:
            self._imgD.rectangle(shape, fill="blue", outline="yellow")
        elif t == 4:
            self._imgD.rectangle(shape, fill="white", outline="red")
  
    def show(self):
        self._img.show() 


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data




def runGame():

    code = getInputData()
    IC = IntcodeComputer(code)
    game = PILScreen()
    count = 0




    ##################
    step=0
    inp=[] #input??
    IC._output = []    # Clear the output list
    terminate = False
    stoppedAtInput = False
    while not terminate:


        # while not stoppedAtInput and not terminate:
        #     terminate, stoppedAtInput = IC.perform_one_operation(IC._memoryPosition, inp, stopAtInput = True) 
        
        length = 0
        while length < 3 and not terminate:
            terminate, stoppedAtInput = IC.perform_one_operation(IC._memoryPosition, inp, stopAtInput = True) 
            length = len(IC._output)
        print(f'OutPut: {IC._output}')
        print(terminate)
        try:
            x = IC._output[0]
            y = IC._output[1]
            t = IC._output[2]
            IC._output = [] 
            
        except Exception:
            game.show()

        ########   TILES
        #    
        #   0 is an empty tile. No game object appears in this tile.
        #   1 is a wall tile. Walls are indestructible barriers.
        #   2 is a block tile. Blocks can be broken by the ball.
        #   3 is a horizontal paddle tile. The paddle is indestructible.
        #   4 is a ball tile. The ball moves diagonally and bounces off objects.    
        
        if t == 2:
            count += 1
        if t != 0:
            game.drawBrick(x,y,t)
        
        #time.sleep(0.5)

        
        # step +=1
        # #inp = [color]
        # stoppedAtInput = False

        # print(f'OutPut: {IC._output}')
    
    return count

    ##################


def day12PartOne():
    answer = runGame()
    print(f'Solution Day 12, Part one:\nAnswer: {answer} \n\n')


def day12PartTwo():
    answer = "unknown"
    print(f'Solution Day 12, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day12PartOne()
    day12PartTwo()

# Run from terminal:
# $ python day_12.py
