# https://adventofcode.com/2019/day/22

import copy
#from deckClass import Deck

inputFile = 'input/22_input'

def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    shuffle = []
    with open(inputFile) as input:
        for line in input:
            if line[:3]=='cut':
                shuffle.append(('cut',int(line[4:-1])))
            elif line[:19]=='deal with increment':
                shuffle.append(('dealWithIncrement',line[20:-1]))
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


def day22PartOne():
    shuffle=getInputData()
    deck=Deck(10007)
    moveCards(shuffle,deck)
    answer=deck.returnPosition(2019)
    print(f'Solution Day 22, Part one:\nAnswer: {answer} \n\n')


def day22PartTwo():
    answer = "unknown"
    print(f'Solution Day 22, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    day22PartOne()
    day22PartTwo()

# Run from terminal:
# $ python day_22.py