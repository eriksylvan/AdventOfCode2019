# https://adventofcode.com/2019/day/16

import copy

inputFile = 'input/16_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data


def getFFT(insignal,phase):
    '''
    insignal: string of numbers, each number is a single digit: indata '15243' represents the sequence 1, 5, 2, 4, 3.
    phase: 'phase' number of phases to calculate: , FFT operates in repeated phases.
    return the tesult of FFT after 'phase' phases 
    '''
    l = len(insignal)
    o=''
    for c in insignal:
        o += str(int(c) * phase)
    fft = c[0:l]
    return fft

def getTransform(row,l):
    t = []
    le = 0
    for j in range(1,row):
        t.append(0)
        le+=1
        if le >=l:break

    for j in range(l-4):
        for i in [1,0,-1,0]:
            for c in range(row): 
                t.append(i) 
                le+=1
                if le >=l:break
            if le >=l:break
        if le >=l:break

    return t

def day16PartOne():
    answer = "unknown"
    print(f'Solution Day 16, Part one:\nAnswer: {answer} \n\n')


def day16PartTwo():
    answer = "unknown"
    print(f'Solution Day 16, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    # day16PartOne()
    # day16PartTwo()


    print(getTransform(1,8))
    print(getTransform(2,8))
    print(getTransform(3,8))


# Run from terminal:
# $ python day_16.py
