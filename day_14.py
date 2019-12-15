# https://adventofcode.com/2019/day/14

import copy
import collections

inputFile = 'input/14_input'




def splitMaterialInput(str):
    nbr,material=str.split(' ')
    return nbr,material

def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    reactios = {}   #   collections.defaultdict(dict)
    with open(inputFile) as inputData:
        for line in inputData:
            inputMaterial,outputMaterial = line.split(' => ')
            outputNbr,outputResult=splitMaterialInput(outputMaterial)
            inputList=inputMaterial.split(', ')
            inputMaterial={}
            for i in range(len(inputList)):
                material=inputList[i]
                inputNbr,inputResult=splitMaterialInput(material)
                inputMaterial[inputResult.strip()] = int(inputNbr.strip())
            reactios[outputResult.strip()]= [ int(outputNbr.strip()), inputMaterial ]
    return reactios



def createChemical(name, amountNeed, storage, reactios, oreUsed):
    '''
        returns ORE used
    '''
    if name == 'ORE':
        return oreUsed + amountNeed   # RETURN
    
    else:
        if name in storage: # check storage
            inStore = storage[name]
            # print(f'Take from storage: ({name}:{inStore}), I need {amountNeed}')
            if inStore >= amountNeed:
                storage[name] -= amountNeed
                return oreUsed     # RETURN
            else:
                amountNeed = amountNeed - storage[name]
                storage[name] = 0    
            # print(f'Left in storage: ({name}:{storage[name]})')             

        # create more cemicals
        recepie = reactios[name]
      
        minAmountToProduce = recepie[0]

        iter = amountNeed // minAmountToProduce
        if amountNeed % minAmountToProduce != 0: iter += 1
        producedAmount = minAmountToProduce * iter
        # print(f'Need to produce {name}={amountNeed}: Min amount={minAmountToProduce} * iter={iter} = produced:{producedAmount} ')

        for i in range(iter):
            

            for ingredience in recepie[1]:
                ingName = ingredience
                ingAmount = recepie[1][ingredience]
                oreUsed = createChemical(ingName, ingAmount, storage, reactios, oreUsed)
                
                
        # print(f'I produced {producedAmount} of {name}, I ordered {amountNeed}.')

        rest = producedAmount - amountNeed
        # print(f'Rest:{rest}, {name}')
        if rest > 0: 
            if name in storage:
                storage[name] += rest
            else:
                storage[name] = rest
        return oreUsed
         




def day14PartOne():
    reactios = getInputData()
    storage={} 
    answer = createChemical('FUEL', 1, storage, reactios, 0)
    print(f'Solution Day 14, Part one:\nI need {answer} units ORE to produce 1 unit FUEL. \n\n')


def day14PartTwo():
    answer = "unknown"
    print(f'Solution Day 14, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day14PartOne()
    day14PartTwo()

# Run from terminal:
# $ python day_14.py
