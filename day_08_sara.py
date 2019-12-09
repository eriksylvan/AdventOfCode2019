# https://adventofcode.com/2019/day/8

import copy
from PIL import Image, ImageDraw   # python -m pip install pillow
from collections import defaultdict

inputFile = 'input/08_input_sara'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = ''
    with open(inputFile) as input:
        for line in input:
            for x in line.split(','):
                data = data+ str(x) 
    return data

def checkCorrect(image,wide,tall):
    imageString=str(image)
    layers=len(imageString)//(wide*tall)
    print(image)
    numbersDict=defaultdict(dict)
    position=0
    for l in range(layers):
        layerDict={}
        for w in range(wide):
            for t in range(tall):
                imageValue=imageString[position]
                layerDict[imageValue]=layerDict.get(imageValue,0)+1
                print(layerDict)
                position+=1
        numbersDict[l]=layerDict
    print(numbersDict)
    minZero=wide*tall+1
    for l in range(layers):
        numberOfZeros=numbersDict.get(l,{}).get('0',minZero)
        if numberOfZeros<minZero:
            minZero=numberOfZeros
            layerWithMinZero=l
    numberOfOne=numbersDict.get(layerWithMinZero,{}).get('1',0)
    numberOfTwo=numbersDict.get(layerWithMinZero,{}).get('2',0)

    print(numbersDict.get(layerWithMinZero,{}))
    print(layerWithMinZero)
    return numberOfOne*numberOfTwo

def createImageDescription(image,wide,tall):
    imageString=image
    layers=len(imageString)//(wide*tall)
    Matrix = [[2 for x in range(wide)] for y in range(tall)] 
    for w in range(wide):
        print(f'w: {w}')
        for t in range(tall):
            for l in range(layers):
                position=l*wide*tall+w+t*wide
                pixelValue=imageString[position]
                if pixelValue!='2':
                    print(f'PixelValue:{pixelValue} l:{l} t:{t} w:{w} position: {position}')
                    Matrix[t][w]=pixelValue
                    break
  
    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new( 'RGB', (250,60), "black") # create a new black image
    pixels = img.load() # create the pixel map
    for i in range(25):    # for every col:
       for j in range(6):    # For every row
           pixels[i,j] =  (0,0,int(Matrix[j][i])*250) # set the colour accordingly
    img.show()
    return Matrix

def day08PartOne():
    image=getInputData()
    answer = checkCorrect(image,25,6)
    print(f'Solution Day 08, Part one:\nAnswer: {answer} \n\n')


def day08PartTwo():
    image=getInputData()
    answer = createImageDescription(image,25,6)
    print(f'Solution Day 08, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day08PartOne()
    day08PartTwo()

# Run from terminal:
# $ python day_08.py    
