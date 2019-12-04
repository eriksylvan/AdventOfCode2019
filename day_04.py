# https://adventofcode.com/2019/day/4

import copy

# inputFile = ''


def getInputData():
    '''
    Returns input data. 
    The range within the passwors are valid
    '''
    limits = (357253, 892942)
    return limits

def isValidPassword(password):
    '''     To be implemented     '''
    
    pwd = str(password)
    
    try:
        # It is a six-digit number.
        v = len(pwd)==6
        if not v: raise Exception()

        # Two adjacent digits are the same (like 22 in 122345).
        v = False
        for i in range(len(pwd)-1):
            if pwd[i] == pwd[i+1]:
                v = True
                break
        if not v: raise Exception()

        # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
        v = True
        for i in range(len(pwd)-1):
            if int(pwd[i]) > int(pwd[i+1]):
                v = False
                raise Exception()
    finally:
            return v

def isValidPassword2(password):
    
    v = isValidPassword(password)    
    pwd = '#' + str(password) + '#'
    v2 = False

    for i in range(len(pwd)-2):
        if pwd[i] != pwd[i+1] and pwd[i+1] == pwd[i+2] and pwd[i+2] != pwd[i+3]:
            v2 = True
            break
    
    return v and v2


def day04PartOne():
    limits = getInputData()
    validPwdList = []
    for p in range(limits[0],limits[1]+1):
        if isValidPassword(p):
            validPwdList.append(p)
    answer = len(validPwdList)
    print(f'Solution Day 04, Part one:\nAnswer: {answer} \n\n')


def day04PartTwo():
    limits = getInputData()
    validPwdList = []
    for p in range(limits[0],limits[1]+1):
        if isValidPassword2(p):
            validPwdList.append(p)
    answer = len(validPwdList)
    print(f'Solution Day 04, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day04PartOne()
    day04PartTwo()

# Run from terminal:
# $ python day_04.py
