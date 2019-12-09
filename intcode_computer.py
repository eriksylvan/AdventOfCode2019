

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

    def addOP(self, paramode):
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
        if paramode[-3] == 0:
            self._intCodeProgram[p3] = int(f1 + f2)
        else: 
            self._intCodeProgram[self._memoryPosition + 3] = int(f1 + f2)
            
        return self._memoryPosition + 4 
        

    def multiplyOP(self, paramode):
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

        if paramode[-3] == 0:
            self._intCodeProgram[p3] = int(f1 * f2)
        else: 
            self._intCodeProgram[self._memoryPosition + 3] = int(f1 * f2)
            
        return self._memoryPosition + 4 

    def inputOP(self, paramode, inp = None):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        if inp is None:
            i1 = int(input("?"))    # input from keyboard
            # Todo: check, only number 0-9
        else:
            i1 = inp              # ingut from inparameter
        
        if paramode[-1] == 0:
            self._intCodeProgram[p1] = i1
        else: 
            self._intCodeProgram[self._memoryPosition + 1] = i1        
        return self._memoryPosition + 2
    
    def outputOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        if paramode[-1] == 0:
            o1 = self._intCodeProgram[p1]
        else:
            o1 = p1
        
        self._output.append(o1)        
        if self._silent == False:
            print(f'Output:{o1}')
        return self._memoryPosition + 2

#   Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothi  ng.
    def jumpTrueOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        p2 = self._intCodeProgram[self._memoryPosition + 2]
        if paramode[-1] == 0:
            b1 = int(self._intCodeProgram[p1])
        else: 
            b1 = int(p1)
        if paramode[-2] == 0:
            pt1 = int(self._intCodeProgram[p2])
        else: 
            pt1 = int(p2)


        if b1:
            nextMemPosition = pt1
        else:
            nextMemPosition = self._memoryPosition + 3

        return nextMemPosition


#   Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    def jumpFalseOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        p2 = self._intCodeProgram[self._memoryPosition + 2]
        if paramode[-1] == 0:
            b1 = int(self._intCodeProgram[p1])
        else: 
            b1 = int(p1)
        if paramode[-2] == 0:
            pt1 = int(self._intCodeProgram[p2])
        else: 
            pt1 = int(p2)


        if not b1:
            nextMemPosition = pt1
        else:
            nextMemPosition = self._memoryPosition + 3
        return nextMemPosition

#   Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    def lessOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        p2 = self._intCodeProgram[self._memoryPosition + 2]
        p3 = self._intCodeProgram[self._memoryPosition + 3]
        if paramode[-1] == 0:
            v1 = self._intCodeProgram[p1]
        else: 
            v1 = p1
        if paramode[-2] == 0:
            v2 = self._intCodeProgram[p2]
        else: 
            v2 = p2
        if v1<v2:
            self._intCodeProgram[p3] = 1
        else:
            self._intCodeProgram[p3] = 0
        return self._memoryPosition + 4 

#   Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    def equalOP(self, paramode):
        p1 = self._intCodeProgram[self._memoryPosition + 1]
        p2 = self._intCodeProgram[self._memoryPosition + 2]
        p3 = self._intCodeProgram[self._memoryPosition + 3]
        if paramode[-1] == 0:
            v1 = self._intCodeProgram[p1]
        else: 
            v1 = p1     
        if paramode[-2] == 0:
            v2 = self._intCodeProgram[p2]
        else: 
            v2 = p2
        if v1==v2:
            self._intCodeProgram[p3] = 1
        else:
            self._intCodeProgram[p3] = 0
        return self._memoryPosition + 4   




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
            size = 4     
        elif opNo == 8:
            op = self.equalOP
            size = 4   
        else:
            assert False, f'Invalid operation code ({opNo}).'
        return op, size

    def getParameterMode(self, word, size):
        l1 =  [0 for x in range(size)]
        l2 =  [int(i) for i in word[:-2]]
        for x in range(-1,-len(l2)-1,-1):
            l1[x] = l2[x]
        return(l1)
        

    def perform_one_operation(self, memPos, input = []):
        self._memoryPosition = memPos
        nextMemoryPosition = 0
        halt = False
        opword = str(self._intCodeProgram[self._memoryPosition])
        op, opsize = self.getoperation(opword)
        paramode = self.getParameterMode(opword, opsize)
      
        # print(f'mempos:{self._memoryPosition}\nword:{opword}\nOperation:{op}\npsize:{opsize}\nparamode:{paramode}\nprg:{self._intCodeProgram[memPos:memPos+5]}\nm223:prg:{self._intCodeProgram[223]}\nm224:prg:{self._intCodeProgram[224]}\nm225:prg:{self._intCodeProgram[225]}\n')
        try:
            if op == self.inputOP:
                if len(input) > 0:              
                    inparam = input.pop(0)
                else:
                    inparam = None
                nextMemoryPosition = op(paramode, inparam) # Perform opeartion
            else:    
                nextMemoryPosition = op(paramode) # Perform opeartion
            self._memoryPosition = nextMemoryPosition
        except Exception:
            print(f'ERROR: memPos:{memPos}, prg:{self._intCodeProgram[memPos:memPos+5]} ')
            halt = True
            raise
        if self._intCodeProgram[self._memoryPosition] == 99:
            halt = True
        return halt

    def run_program(self, input=[]):
        self._output = []    # Clear the output list
        halt = False
        self._memoryPosition = 0
        while not halt:
            halt = self.perform_one_operation(self._memoryPosition, input)
        #    input('>')
        return self._output
        





if __name__ == "__main__":
    print('\nMain\n\n')
    # IntCode = IntcodeComputer([1105, 1, 4, 4, 99])
    # # IntCode.perform_one_operation(0)
    # IntCode.run_program()
    # print(IntCode._intCodeProgram)

    # # Example 1, input equal 8, Input == 8 -> 1
    # print("Example 1, input equal 8, Input == 8 -> 1")
    # IC = IntcodeComputer([3,9,8,9,10,9,4,9,99,-1,8])
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # Example 2, input less than 8, Input == 8 --> 0 
    # print("Example 2, input less than 8, Input == 8 --> 0")
    # IC = IntcodeComputer([3,9,7,9,10,9,4,9,99,-1,8])
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # Example 3, input equal 8, Input == 8 --> 0 
    # print("Example 3, input equal 8, Input == 8 --> 0")
    # IC = IntcodeComputer([3,3,1108,-1,8,3,4,3,99])
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # Example 4, input less than 8, Input == 8 --> 0 
    # print("Example 4, input less than 8, Input == 8 --> 0")
    # IC = IntcodeComputer([3,3,1107,-1,8,3,4,3,99])
    # IC.run_program()
    # print(IC._intCodeProgram)


    # # Example 5, (using position mode), Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    # print('Example 5, (using position mode), Jump test Input == 0 --> 0, Input != 0 --> 1 )')
    # IC = IntcodeComputer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
    # IC.run_program()
    # print(IC._intCodeProgram)


    # # Example 6, (using immediate  mode), Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    # print('Example 6, (using position mode), Jump test Input == 0 --> 0, Input != 0 --> 1 )')
     
    # IC = IntcodeComputer([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]) 
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # # Example 7, Lager program, input > 8 --> output 999, input == 8 --> output 1000, input > 8 --> output 1001
    # print('Example 7, Lager program, input > 8 --> output 999, input == 8 --> output 1000, input > 8 --> output 1001')
    # IC = IntcodeComputer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    # IC.run_program()
    # print(IC._intCodeProgram)


            # 1   addOP8
            # 2   multiplyOP
            # 3   inputOP
            # 4   outputOP
            # 5   jumpTrueOP
            # 6   jumpFalseOP
            # 7   lessOP
            # 8   equalOP
        


    # self.assertEqual(IC._intCodeProgram,[])
        # self.assertEqual(IC._memoryPosition,4)



        # value1 = intCodeProgram[intCodeProgram[position+1]]
        # value2 = intCodeProgram[intCodeProgram[position+2]]
        # outputPosition = intCodeProgram[position+3]
        # if opcode == 1:
        #     intCodeProgram[outputPosition] = value1+value2
        # elif opcode == 2:
        #     intCodeProgram[outputPosition] = value1*value2
        # position = position+4
        # return nextMemPos, halt 