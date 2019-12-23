import random

class IntcodeComputer:
    '''
    Represents an Intcode Computer
    '''
    import copy
    
    def __init__(self, program):
        '''
        Instance an Intcode Computer and load a program
        '''
        self._intCodeProgram = program
        self._memoryPosition = 0
        self._silent = False
        self._output = []           # list that holds the outputs
        self._relativeBase = 0      # _relativeBase, used in 'relative mode'
        
        # Converting a list to dictionary with list elements as values in dictionary
        # and keys are enumerated index starting from 0 i.e. index position of element in list
        self._intCodeProgramDict = { i : self._intCodeProgram[i] for i in range(0, len(self._intCodeProgram) ) }

       
 
    def writeMem(self, memPos, value):
        self._intCodeProgramDict[memPos] = value
        return 0

    def readMem(self, memPos):
        p = 0
        try:
            p = self._intCodeProgramDict[memPos]
        except KeyError:
            self._intCodeProgramDict[memPos] = 0
            p = 0
        finally:
            pass
        return p

    def getParameter(self, offset):
        pos = self._memoryPosition + offset
        p = self.readMem(pos)
        return p

    # def putInput(self, inputVal):
    #     self._input.append(inputVal)

    # def popInput(self, inputVal):
    #     self._input.append(inputVal)

##############
# OPERATIONS #
##############       

    

    def addOP(self, paramode):
        p1 = self.getParameter(1)
        p2 = self.getParameter(2)
        p3 = self.getParameter(3)
        if paramode[-1] == 0:
            t1 = int(self.readMem(p1))
        elif paramode[-1] == 1: 
            t1 = int(p1)
        else:
            t1 = int(self.readMem(p1 + self._relativeBase))
        
        if paramode[-2] == 0:
            t2 = int(self.readMem(p2))
        elif paramode[-2] == 1: 
            t2 = int(p2)
        else:
            t2 = int(self.readMem(p2 + self._relativeBase))
        
        if paramode[-3] == 0:
            self._intCodeProgramDict[p3] = int(t1 + t2)
        elif paramode[-3] == 1: 
            self._intCodeProgramDict[self._memoryPosition + 3] = int(t1 + t2)
        else :
            self._intCodeProgramDict[p3 + self._relativeBase] = int(t1 + t2)
            
        return self._memoryPosition + 4 
        

    def multiplyOP(self, paramode):
        p1 = self.getParameter(1)
        p2 = self.getParameter(2)
        p3 = self.getParameter(3)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        # p2 = self._intCodeProgramDict[self._memoryPosition + 2]
        # p3 = self._intCodeProgramDict[self._memoryPosition + 3]
        if paramode[-1] == 0:
            f1 = int(self.readMem(p1))
        elif paramode[-1] == 1: 
            f1 = int(p1)
        else:
            f1 = int(self.readMem(p1+self._relativeBase))
        
        if paramode[-2] == 0:
            f2 = int(self.readMem(p2))
        elif paramode[-2] == 1: 
           
            f2 = int(p2)
        else:
            f2 = int(self.readMem(p2+self._relativeBase))

        if paramode[-3] == 0:
            self._intCodeProgramDict[p3] = int(f1 * f2)
        elif paramode[-3] == 1: 
            self._intCodeProgramDict[self._memoryPosition + 3] = int(f1 * f2)
        else:
            self._intCodeProgramDict[p3 + self._relativeBase] = int(f1 * f2)
            
        return self._memoryPosition + 4 

    def inputOP(self, paramode, inp = None):
        p1 = self.getParameter(1)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        if inp is None:
            print(self._intCodeProgramDict)
            i1 = int(input("?"))    # input from keyboard
            # Todo: check, only number 0-9
        else:
            i1 = inp              # ingut from inparameter
        
        if paramode[-1] == 0:
            self._intCodeProgramDict[p1] = i1
        elif paramode[-1] == 1: 
            self._intCodeProgramDict[self._memoryPosition + 1] = i1        
        else:
            self._intCodeProgramDict[p1 + self._relativeBase] = i1
        return self._memoryPosition + 2
    
    def outputOP(self, paramode):
        p1 = self.getParameter(1)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        if paramode[-1] == 0:
            o1 = self.readMem(p1)
        elif paramode[-1] == 1:
            o1 = p1
        else: 
            o1 = self.readMem(p1 + self._relativeBase)
        self._output.append(o1)        
        if self._silent == False:
            print(f'Output: {o1}')
        return self._memoryPosition + 2

#   Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothi  ng.
    def jumpTrueOP(self, paramode):
        p1 = self.getParameter(1)
        p2 = self.getParameter(2)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        # p2 = self._intCodeProgramDict[self._memoryPosition + 2]
        if paramode[-1] == 0:
            b1 = int(self.readMem(p1))
        elif paramode[-1] == 1: 
            b1 = int(p1)
        else:
            b1 = int(self.readMem(p1 + self._relativeBase))
        if paramode[-2] == 0:
            pt1 = int(self.readMem(p2))
        elif paramode[-2] == 1: 
            pt1 = int(p2)
        else:
            pt1 = int(self.readMem(p2 + self._relativeBase))

        if b1:
            nextMemPosition = pt1
        else:
            nextMemPosition = self._memoryPosition + 3

        return nextMemPosition


#   Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    def jumpFalseOP(self, paramode):
        p1 = self.getParameter(1)
        p2 = self.getParameter(2)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        # p2 = self._intCodeProgramDict[self._memoryPosition + 2]
        if paramode[-1] == 0:
            b1 = int(self.readMem(p1))
        elif paramode[-1] == 1: 
            b1 = int(p1)
        else:
            b1 = int(self.readMem(p1 + self._relativeBase))

        if paramode[-2] == 0:
            pt1 = int(self.readMem(p2))
        elif paramode[-2] == 1: 
            pt1 = int(p2)
        else:
            pt1 = int(self.readMem(p2+self._relativeBase))


        if not b1:
            nextMemPosition = pt1
        else:
            nextMemPosition = self._memoryPosition + 3
        return nextMemPosition

#   Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    def lessOP(self, paramode):
        p1 = self.getParameter(1)
        p2 = self.getParameter(2)
        p3 = self.getParameter(3)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        # p2 = self._intCodeProgramDict[self._memoryPosition + 2]
        # p3 = self._intCodeProgramDict[self._memoryPosition + 3]
        if paramode[-1] == 0:
            v1 = self.readMem(p1)
        elif paramode[-1] == 1: 
            v1 = p1
        else:
            v1 = self.readMem(p1 + self._relativeBase)

        if paramode[-2] == 0:
            v2 = self.readMem(p2)
        elif paramode[-2] == 1: 
            v2 = p2
        else: 
            v2 = self.readMem(p2 + self._relativeBase)

        if v1<v2:
            ls = 1
        else:
            ls = 0

        if paramode[-3] == 0:
            self._intCodeProgramDict[p3] = ls
        elif paramode[-3] == 1:
            self._intCodeProgramDict[self._memoryPosition + 3] = ls
        else:
            self._intCodeProgramDict[p3 + self._relativeBase] = ls
        
        return self._memoryPosition + 4 


#   Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    def equalOP(self, paramode):
        p1 = self.getParameter(1)
        p2 = self.getParameter(2)
        p3 = self.getParameter(3)
        # p1 = self._intCodeProgramDict[self._memoryPosition + 1]
        # p2 = self._intCodeProgramDict[self._memoryPosition + 2]
        # p3 = self._intCodeProgramDict[self._memoryPosition + 3]
        if paramode[-1] == 0:
            v1 = self.readMem(p1)
        elif paramode[-1] == 1: 
            v1 = p1     
        else:
            v1 = self.readMem(p1 + self._relativeBase)

        if paramode[-2] == 0:
            v2 = self.readMem(p2)
        elif paramode[-2] == 1: 
            v2 = p2
        else:
            v2 = self.readMem(p2 + self._relativeBase)

        if v1==v2:
            eq = 1
        else:
            eq = 0
        if paramode[-3] == 0:
            self._intCodeProgramDict[p3] = eq
        elif paramode[-3] == 1:
            self._intCodeProgramDict[self._memoryPosition + 3] = eq
        else:
            self._intCodeProgramDict[p3 + self._relativeBase] = eq
        return self._memoryPosition + 4   

#   Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.
    def adjustRelativeBaseOP(self, paramode):
        p1 = self.getParameter(1)
        # syp1 = self._intCodeProgramDict[self._memoryPosition + 1]
        if paramode[-1] == 0:
            a = self.readMem(p1)
        elif paramode[-1] == 1:
            a = p1
        else:
            a = self.readMem(p1 + self._relativeBase)
        self._relativeBase += a         # Adjusing the relative base
        return self._memoryPosition + 2


    def exitOP(self, paramode):
        return self._memoryPosition




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
        elif opNo == 5:
            op = self.jumpTrueOP
            size = 2    
        elif opNo == 6:
            op = self.jumpFalseOP
            size = 2    
        elif opNo == 7:
            op = self.lessOP
            size = 3     
        elif opNo == 8:
            op = self.equalOP
            size = 3   
        elif opNo == 9:
            op = self.adjustRelativeBaseOP
            size = 1
        elif opNo == 99:
            op = self.exitOP
            size = 0
        else:
            assert False, f'Invalid operation code ({opNo}).'
        return op, size

    def getParameterMode(self, word, size):
        l1 =  [0 for x in range(size)]
        l2 =  [int(i) for i in word[:-2]]
        for x in range(-1,-len(l2)-1,-1):
            l1[x] = l2[x]
        
        return(l1)
        

    def perform_one_operation(self, memPos=None, input = [], stopAtInput = False):
        if memPos: 
            self._memoryPosition = memPos
        nextMemoryPosition = 0
        terminate = False
        stoppedAtInput = False
        opword = str(self._intCodeProgramDict[self._memoryPosition])
        op, opsize = self.getoperation(opword)
        paramode = self.getParameterMode(opword, opsize)
        # DEBUG PRINTOUTS
        # print(f'Operation:{opword}')
        # print(f'ParameterMode:{paramode}')
        # print(f'RelativeBase:{self._relativeBase}')
        # print(f'P1: {self.getParameter(1)}')
        # print(f'P2: {self.getParameter(2)}')
        # print(f'P3: {self.getParameter(3)}')
        # print(f'P4: {self.getParameter(4)}')
        # print(f'halt: {halt}')
        

        # print(f'mempos:{self._memoryPosition}\nword:{opword}\nOperation:{op}\npsize:{opsize}\nparamode:{paramode}\nprg:{self._intCodeProgramDict[memPos:memPos+5]}\nm223:prg:{self._intCodeProgramDict[223]}\nm224:prg:{self._intCodeProgramDict[224]}\nm225:prg:{self._intCodeProgramDict[225]}\n')
        try:
            
            if op == self.exitOP:
                # print('EXIT')
                nextMemoryPosition = self._memoryPosition
                terminate = True
            elif op == self.inputOP:
                #print('input')
                if len(input) > 0:              
                    inparam = input.pop(0)
                    nextMemoryPosition = op(paramode, inparam) # Perform opeartion
                else:
                    if stopAtInput:
                        # Stop at input. This makes it possible for surrounding code to privide new inparameters.False
                        nextMemoryPosition = self._memoryPosition # keep memory position
                        stoppedAtInput = True
                        # do not perform operation
                    
                    else:    
                        inparam = None
                        nextMemoryPosition = op(paramode, inparam) # Perform opeartion
            else:    
                nextMemoryPosition = op(paramode) # Perform opeartion
            
            self._memoryPosition = nextMemoryPosition
        except Exception:
            print("ERROR")
            # print(f'ERROR: memPos:{memPos}, prg:{self._intCodeProgramDict[memPos:memPos+5]} ')
            print(f'ERROR: memPos:{memPos}, prg:{self._intCodeProgramDict[memPos]} ')
            # halt = True
            raise
        # print(terminate, stoppedAtInput)
        return terminate, stoppedAtInput

    def run_program(self, inp=[]):
        self._output = []    # Clear the output list
        terminate = False
        self._memoryPosition = 0
        while not terminate:
            terminate, stoppedAtInput = self.perform_one_operation(self._memoryPosition, inp)
            # input('>')
        return self._output
        
    # def continue_to_input(self, inp=[]):
    #     self._output = []    # Clear the output list
    #     terminate = False
    #     stopedAtInput = False
    #     while not terminate:
    #         terminate, stoppedAtInput = self.perform_one_operation(self._memoryPosition, inp, stopAtInput = True)
    #         print(terminate, stopedAtInput)
    #         if stoppedAtInput:
    #             print(f'memPos:{self._memoryPosition}')
    #             print(f'OutPut{self._output}')
    #             inpInt = random.randint(0,1)
    #             input(f'Input: {inpInt}>')
    #             inp = [inpInt]
    #     return self._output
    




if __name__ == "__main__":
    print('\nMain _ IntCodeProgra\n\n')
   
            # 1   addOP
            # 2   multiplyOP
            # 3   inputOP
            # 4   outputOP
            # 5   jumpTrueOP
            # 6   jumpFalseOP
            # 7   lessOP
            # 8   equalOP
            # 9   adjustRelativeBaseOP
            #10   exitOP