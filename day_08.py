# https://adventofcode.com/2019/day/8

import copy
from PIL import Image, ImageDraw   # python -m pip install pillow

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
    NOT USED IN SOLUTION
    '''
    layers = len(imgStr) // (width * hight)
    img = [[[-1 for x in range(width)] for y in range(hight)]
           for z in range(layers)]
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
    img = ['' for l in range(layers)]
    for l in range(layers):
        img[l] = imgStr[(l * size):(l * size + size)]
    return img


def getAnswerPartOne(imgStrLayers, width, hight):
    img = buildLayerImage(imgStrLayers, width, hight)
    min_zero = len(img[0]) + 1  # Start value one bigger than max size
    for layer in img:
        zero = layer.count('0')
        one = layer.count('1')
        two = layer.count('2')
        if min_zero > zero:
            min_zero = zero
            p12 = one * two
    return p12


def drawImage(imgStr, width, hight):
    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new('1', (width, hight))  # create a new black 1-bit image (BW)
    pixels = img.load()         # create the pixel map
    for c in range(width):      # for every col:
        for r in range(hight):   # for every row
            p = getStringPos(c, r, width, hight)
            pixels[c, r] = int(imgStr[p]) % 2
    img.show()


def mergeLayers(imgStrLayers):
    '''
    Mergis all layers in an image. 2 is transparent, not used, 0 = black, 1= white. The first (lowest layer) pixel is used 
    '''
    layers = len(imgStrLayers)
    size = len(imgStrLayers[0])
    mergedImg = ['0' for x in range(size)]  # start with black list
    for pos in range(size):
        for l in range(layers):
            pixVal = imgStrLayers[l][pos]
            if pixVal == '2':
                pass  # Transparent pixel, do nothing
            else:
                mergedImg[pos] = pixVal
                break  # Pixel found, jump out of loop
    return ''.join(mergedImg)   # convert list into string


def getPixelPos(pos, width, hight):
    return (pos % width, pos // hight)


def getStringPos(c, r, width, hight):
    return (r * width) + c


def day08PartOne():
    imgStr = getInputData()
    answer = getAnswerPartOne(imgStr, 25, 6)
    print(f'Solution Day 08, Part one:\nAnswer: {answer} \n\n')


def day08PartTwo():
    imgData = getInputData()
    img = buildLayerImage(imgData, 25, 6)
    imgStr = mergeLayers(img)
    drawImage(imgStr, 25, 6)
    print(f'Solution Day 08, Part two: \n\n')

    # Your puzzle answer was ZLBJF.


if __name__ == "__main__":

    day08PartOne()
    day08PartTwo()


# Run from terminal:
# $ python day_08.py
