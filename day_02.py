# https://adventofcode.com/2019/day/2

inputFile = 'input/02_input'


def intcode(program):
    '''To be implemented'''
    return(program)

def day02PartOne():

    intCodeProgram = []
    with open(inputFile) as input:
        for line in input:
            intCodeProgram = [ int(x) for x in line.split(',') ]
   
    print(intcode(intCodeProgram))


if __name__ == "__main__":
    day02PartOne()
    # day02PartTwo()    
    