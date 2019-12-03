# https://adventofcode.com/2019/day/3

import copy
from PIL import Image, ImageDraw   # python -m pip install pillow
import os


inputFile = 'input/03_input'


def getInputData():
    '''Reads the input file end returns the data in lists of strings'''
    wirePath = []
    with open(inputFile) as input:
        for line in input:
            wirePath.append([str(x) for x in line.strip().split(',')])
    return wirePath


def manhattanDistance(wire1, wire2):
    ''' 
    Takes two wire grid paths as input and return the Manhattan Distance from the central port to the closest intersection of the wires.
    Wire grid path is represented by a list of directions and steps e.g. ['R8','U5','L5','D3']  
    '''

    size, cp = calculateGridSize(wire1, wire2) # cp: contral port location
    
    
    img = Image.new('RGB', (int(size[0]/100),int(size[1]/100)))
    draw = ImageDraw.Draw(img) 
    

    x,y = cp[0], cp[1]
    newx, newy = x, y
    

    #################
    for word in wire1:
        direction = word[:1]
        distance = int(word[1:])
        
        if direction == 'U':
            new = x - distance             
        elif direction == 'D':
            newx = x + distance             
        elif direction == 'L':
            newy = y - distance             
        elif direction == 'R':
            newy = y + distance             
        draw.line((int(x/100), int(y/100), int(newx/100), int(newy/100)), fill=(225,128,0) ,width=4)    
        x=copy.deepcopy(newx)
        y=copy.deepcopy(newy)
    ###################
    x,y = cp[0], cp[1]
    newx, newy = x, y
    
    for word in wire2:
        direction = word[:1]
        distance = int(word[1:])
        
        if direction == 'U':
            new = x - distance             
        elif direction == 'D':
            newx = x + distance             
        elif direction == 'L':
            newy = y - distance             
        elif direction == 'R':
            newy = y + distance             
        draw.line((int(x/100), int(y/100), int(newx/100), int(newy/100)),fill=(225,225,0) ,width=4  ) 
        x=copy.deepcopy(newx)
        y=copy.deepcopy(newy)
    ####################
    img.show()
    


    '''To be implemented'''
    return len(wire1)+len(wire2)

def calculateGridSize(wire1, wire2):
    
    def gridSize(wire):
        U=0; D=0; L=0; R=0
        for word in wire:
            direction = word[:1]
            distance = int(word[1:])
            
            if direction == 'U':
                U += distance
            elif direction == 'D':
                D += distance
            elif direction == 'L':
                L += distance
            elif direction == 'R':
                R += distance
            else:
                assert False, f'Invalid direction: {direction}'
        return [U,D,L,R] 
    
    s1 = gridSize(wire1)
    s2 = gridSize(wire2)
    
    for i in range(3): s1[i]=max(s1[i], s2[i])
       
    return (s1[0]+s1[1]+1, s1[2]+s1[3]+1),(s1[1]+1, s1[2]+1)


def day03PartOne():

    wirePaths = getInputData()
    manhattanDistance(wirePaths[0],wirePaths[1])
    print(calculateGridSize(wirePaths[0],wirePaths[1]))

    answer = 0
    print(f'Solution Day 03, Part one:\nAnswer: {answer} \n\n')


def day03PartTwo():
    answer = "unknown"
    print(f'Solution Day 03, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day03PartOne()
    day03PartTwo()


# Run from terminal:
# $ python day_03.py
