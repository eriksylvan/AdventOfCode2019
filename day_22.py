# https://adventofcode.com/2019/day/22

import fileinput
import copy
#from deckClass import Deck

inputFile = 'input/22_input'

def getInputData():
    '''Reads the input file end returns the data in a list shuffle instructions'''
    instructions = []
    with open(inputFile) as input:
        for line in input:
            instructions.append(line.strip())
    return instructions

def readInstructions(inst):
    '''Reads list of instructiona and returns at list with tuples of instaction and value'''
    shuffle = []
    for line in inst:
        if line[:3]=='cut':
            shuffle.append(('cut',int(line[4:])))
        elif line[:19]=='deal with increment':
            shuffle.append(('dealWithIncrement',int(line[20:])))
        else:
            shuffle.append(('dealIntoNewStack',0))
    return shuffle

class Deck:
    def __init__(self,deckSize):
        self.deck=list(range(deckSize))
        self.deckSize=deckSize

    def __str__(self):
        return f'Deck: {self.deck}'

    def cut(self,number):
        newDeck=[None]*self.deckSize
        if number>0:
            newDeck[-number:]=self.deck[:number]
            newDeck[:self.deckSize-number]=self.deck[-self.deckSize+number:]
        if number<0:
            newDeck[:abs(number)]=self.deck[number:]
            newDeck[-self.deckSize+abs(number):]=self.deck[:self.deckSize-abs(number)]
        self.deck=newDeck

    def dealIntoNewStack(self):
        newDeck=[]
        for i in range(self.deckSize):
            newDeck.append(self.deck[self.deckSize-1-i])
        self.deck=newDeck
    
    def returnPosition(self,cardNbr):
        return self.deck.index(cardNbr)

    def dealWithIncrement(self,incr):
        newDeck=[None]*self.deckSize
        for i in range(self.deckSize):
            position=i*int(incr)%int(self.deckSize)
            newDeck[position]=self.deck[i]
        self.deck=newDeck
# end Deck class

def moveCards(shuffle,deck):
    print(f'Start deck: {deck}')
    for draw in shuffle:
        if draw[0]=='cut':
            deck.cut(draw[1])
        if draw[0]=='dealWithIncrement':
            deck.dealWithIncrement(draw[1])
        if draw[0]=='dealIntoNewStack':
            deck.dealIntoNewStack()
    print(f'deck: {deck}')

#########################################
##
##  Stolen with pride from u/bla2, Reddit
##  https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbwp0r0/?context=3
##  
#########################################

def applyMagic():
    n = 119315717514047
    c = 2020

    a, b = 1, 0
    #for l in fileinput.input():
    with open(inputFile) as input:
        for l in input:
            if l == 'deal into new stack\n':
                la, lb = -1, -1
            elif l.startswith('deal with increment '):
                la, lb = int(l[len('deal with increment '):]), 0
            elif l.startswith('cut '):
                la, lb = 1, -int(l[len('cut '):])
            # la * (a * x + b) + lb == la * a * x + la*b + lb
            # The `% n` doesn't change the result, but keeps the numbers small.
            a = (la * a) % n
            b = (la * b + lb) % n

    M = 101741582076661
    # Now want to morally run:
    # la, lb = a, b
    # a = 1, b = 0
    # for i in range(M):
    #     a, b = (a * la) % n, (la * b + lb) % n

    # For a, this is same as computing (a ** M) % n, which is in the computable
    # realm with fast exponentiation.
    # For b, this is same as computing ... + a**2 * b + a*b + b
    # == b * (a**(M-1) + a**(M) + ... + a + 1) == b * (a**M - 1)/(a-1)
    # That's again computable, but we need the inverse of a-1 mod n.

    # Fermat's little theorem gives a simple inv:
    def inv(a, n): return pow(a, n-2, n)

    Ma = pow(a, M, n)
    Mb = (b * (Ma - 1) * inv(a-1, n)) % n

    # This computes "where does 2020 end up", but I want "what is at 2020".
    #print((Ma * c + Mb) % n)

    # So need to invert (2020 - MB) * inv(Ma)
    answer = ((c - Mb) * inv(Ma, n)) % n
    print(((c - Mb) * inv(Ma, n)) % n)
    return answer


#########################################



def day22PartOne():
    instr = getInputData()
    print(instr)
    shuffle = readInstructions(instr)
    print('\n\n')
    print(shuffle)
    print('\n\n')
    
    deck = Deck(10007)
    moveCards(shuffle, deck)
    answer = deck.returnPosition(2019)
    print(f'Solution Day 22, Part one:\nAnswer: {answer} \n\n')


def day22PartTwo():
    answer = applyMagic()
    print(f'Solution Day 22, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day22PartOne()
    day22PartTwo()

# Run from terminal:
# $ python day_22.py


# Solution Day 22, Part one:
# Answer: 8502

# Solution Day 22, Part two:
# Answer: 41685581334351