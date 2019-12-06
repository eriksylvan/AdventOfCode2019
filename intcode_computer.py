class IntcodeComputer:
    '''
    Represents an Intcode Computer
    '''

    def __init__(self, program):
        '''
        Instance an Intcode Computer and load a program
        '''
        self._intCodeProgram = program
        self._memoryPosition = 0

    def addOP(self, paramode):
        # #print("ADD")
        #print(paramode)
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        p2 = self._intCodeProgram[self._memoryPosition + 2]
        p3 = self._intCodeProgram[self._memoryPosition + 3]
        #print(p1,p2,p3)
        if paramode[-1] == 0:
            t1 = self._intCodeProgram[p1]
        else: 
            t1 = p1
        
        if paramode[-2] == 0:
            t2 = self._intCodeProgram[p2]
        else: 
            t2 = p2
        #print(t1, t2)
        self._intCodeProgram[p3] = int(t1 + t2)
        return 3 # OP size
        

    def multiplyOP(self, paramode):
        # #print("MULTIPLY")
        # #print(paramode)
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        p2 = self._intCodeProgram[self._memoryPosition + 2]
        p3 = self._intCodeProgram[self._memoryPosition + 3]
        if paramode[-1] == 0:
            f1 = self._intCodeProgram[p1]
        else: 
            f1 = p1
        
        if paramode[-2] == 0:
            f2 = self._intCodeProgram[p2]
        else: 
            f2 = p2
        self._intCodeProgram[p3] = int(f1 * f2)
        return 3 # OP size

    def inputOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        i1 = input("?")
        # Todo: check, only number 0-9
        self._intCodeProgram[p1] = int(i1)
        return 1
    
    def outputOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        print(f'Output:{self._intCodeProgram[p1]}')
        return 1


    def getoperation(self, word):
        opNo = int(word[-2:])

        if opNo == 1:
            size = 3
            op = self.addOP
        elif opNo == 2:
            size = 3
            op = self.multiplyOP
        elif opNo == 3:
            size = 1
            op = self.inputOP
        elif opNo == 4:
            op = self.outputOP
            size = 1
        else:
            assert False, f'Invalid operation code ({opNo}).'
        return op, size

    def getParameterMode(self, word, size):
        l1 =  [0 for x in range(size)]
        l2 =  [int(i) for i in word[:-2]]
        #print(l1, l2, len(l2), -len(l2))
        for x in range(-1,-len(l2)-1,-1):
            l1[x] = l2[x]
        return(l1)
        

    def perform_one_operation(self, memPos):
        self._memoryPosition = memPos
        halt = False
        opword = str(self._intCodeProgram[self._memoryPosition])
        op, opsize = self.getoperation(opword)
        paramode = self.getParameterMode(opword, opsize)
        # #print(f'mempos:{self._memoryPosition}\nword:{opword}\nOperation:{op}\npsize:{opsize}\nparamode:{paramode}\n')
        try:
            op(paramode) # Perform opeartion
        except:
            print(f'ERROR: memPos:{memPos}, prg:{self._intCodeProgram[memPos:memPos+5]} ')
        self._memoryPosition += opsize + 1
        if self._intCodeProgram[self._memoryPosition] == 99:
            halt = True
        
        return halt

    def run_program(self):
        halt = False
        self._memoryPosition = 0
        while not halt:
            halt = self.perform_one_operation(self._memoryPosition)
        return True
        





if __name__ == "__main__":
    IntCode = IntcodeComputer([1001, 4, -1040, 4, 4])
    IntCode.perform_one_operation(0)
    #IntCode.run_program()
    # #print(IntCode._intCodeProgram)



        # value1 = intCodeProgram[intCodeProgram[position+1]]
        # value2 = intCodeProgram[intCodeProgram[position+2]]
        # outputPosition = intCodeProgram[position+3]
        # if opcode == 1:
        #     intCodeProgram[outputPosition] = value1+value2
        # elif opcode == 2:
        #     intCodeProgram[outputPosition] = value1*value2
        # position = position+4
        # return nextMemPos, halt 