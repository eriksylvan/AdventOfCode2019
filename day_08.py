# https://adventofcode.com/2019/day/8

import copy

inputFile = 'input/08_input'


def getInputData():
    '''Reads the input file end returns the iage data in a string'''
    with open(inputFile) as input:
        for line in input:
            imgStr = str(line)
    return imgStr

def test_layerFewest0(input):
    return 0


def buildLayerImageMatrix(imgStr, width, hight):
    '''
    Returns a matrix representing th image, dimensions: layer x hight width
    '''
    layers = len(imgStr) // (width * hight)
    img = [[[-1 for x in range(width)] for y in range(hight)] for z in range(layers) ] 
    for l in range(layers):
        for h in range(hight):
            for w in range(width):
                pos = (l * width * hight) + (h * width) + w               
                img[l][h][w] = int(imgStr[pos]) 
    return img

def buildLayerImage(imgStr, width, hight):
    '''
    Returns a list representing the image, every layer with a string
    '''
    size = (width * hight)
    layers = len(imgStr) // size
    img = [ '' for l in range(layers) ] 
    for l in range(layers):
        img[l] = imgStr[(l * size):(l * size + size)]
    return img


def getAnswerPartOne(imgStr, width, hight):
    img = buildLayerImage(imgStr, width, hight)
    min_zero = len(img[0]) + 1 # Start value one bigger than max size
    for layer in img:
        zero = layer.count('0') 
        one = layer.count('1')
        two = layer.count('2')
        if min_zero > zero:
            min_zero = zero
            print(one,two)
            p12 = one * two
    return p12


def day08PartOne():
    imgStr = getInputData()
    answer = getAnswerPartOne(imgStr,25,6)
    print(f'Solution Day 08, Part one:\nAnswer: {answer} \n\n')


def day08PartTwo():
    answer = "unknown"
    print(f'Solution Day 08, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day08PartOne()
    #day08PartTwo()


# Run from terminal:
# $ python day_08.py
