# https://adventofcode.com/2019/day/16

import copy

inputFile = 'input/16_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = line
    return data


def getFFT(insignal,phase):
    '''
    insignal: string of numbers, each number is a single digit: indata '15243' represents the sequence 1, 5, 2, 4, 3.
    phase: 'phase' number of phases to calculate: , FFT operates in repeated phases.
    return the tesult of FFT after 'phase' phases 
    '''
    
    l = len(insignal)
    # print(l)
    # print(insignal)
   

    for ph in range(phase):
        ret = ''
        # print(insignal)
        o=[None]*l
        for row in range(l):
            fft = getTransform(row,l)
            # print(fft)
            for i in range(l):
                # print(i)
                o[i] = int(fft[i]) * int(insignal[i])
            sum = 0
            # print(f'O: {o}')
            for s in o:
                sum +=int(s)
            # print(f'SUM:{sum}')
            
            ch = str(sum)[-1:] # pick last digit
            ret+=ch
            # print(ch)
        insignal = copy.deepcopy(ret)
            
            
    
    return ret


def getTransform(row,l):
    t = []
    le = 0
    # print(l,row)
    for j in range(row):
        # print("in loop")
        t.append(0)
        le+=1
        if le >=l:break

    for j in range(l):
        for i in [1,0,-1,0]:
            for c in range(row+1): 
                t.append(i) 
                le+=1
                if le >=l:break
            if le >=l:break
        if le >=l:break

    return t

#################
# PART 2 SHEATING
# copied from u/wzkx reddit

def SOL2():
    with open(inputFile,"rt") as f: t = f.read().strip() # input as string
    d = [int(x) for x in t]; N = len(d) # input as numbers
    v = d[:] # working copy of data
    for _ in range(100):
        v = [abs(sum( (0,1,0,-1)[(i+1)//(k+1)%4]*v[i] for i in range(N) )) % 10 for k in range(N)]
    #print(''.join(str(x) for x in v[:8]))
    v = (10000*d)[int(t[:7]):] # tail for part2
    for _ in range(100):
        for i in range(len(v)-1,0,-1): # need to do calculations from the end!!! that's the key idea!
            v[i-1] = (v[i-1]+v[i]) % 10
    # print(''.join(str(x) for x in v[:8]))
    return ''.join(str(x) for x in v[:8])





def day16PartOne():
    insignal = getInputData()
    answer = getFFT(insignal,100)[0:8]

    print(f'Solution Day 16, Part one:\nAnswer: {answer} \n\n')


def day16PartTwo():
    answer = SOL2()
    print(f'Solution Day 16, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    #day16PartOne()
    day16PartTwo()


  

# Run from terminal:
# $ python day_16.py
