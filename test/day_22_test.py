import unittest
import day_22
from day_22 import Deck

class TestDay22(unittest.TestCase):
    

    #@unittest.skip("Skip")
    def test_deck10all(self):
        cards = Deck(10)
        print(cards)
        self.assertEqual(cards.deck, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_deck10pos(self):
        cards = Deck(10)
        print(cards)
        self.assertEqual(cards.returnPosition(9), 9)
        self.assertEqual(cards.returnPosition(5), 5)
        self.assertEqual(cards.returnPosition(0), 0)

    def test_deck10inc3(self):
        cards = Deck(10)
        # 'deal with increment 3'
        cards.dealWithIncrement(3)
        self.assertEqual(cards.deck, [0, 7, 4, 1, 8, 5, 2, 9, 6, 3])
        
    def test_deck10cut3(self):
        cards = Deck(10)
        # 'deal with increment 7'
        cards.cut(3)
        self.assertEqual(cards.deck, [3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
        
    def test_deck10cutneg4(self):
        cards = Deck(10)
        # 'deal with increment 7'
        cards.cut(-4)
        self.assertEqual(cards.deck, [6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
    
    def test_deck10newstack(self):
        cards = Deck(10)
        # 'deal with increment 7'
        cards.dealIntoNewStack()
        self.assertEqual(cards.deck, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    
    def test_readInstructions(self):
        instr=['deal with increment 7', 'deal with increment 711', 'cut 4', 'cut -123', 'deal into new stack']
        shuffle = day_22.readInstructions(instr)
        print(shuffle)
        self.assertEqual(shuffle, [('dealWithIncrement', 7), ('dealWithIncrement', 711), ('cut', 4), ('cut', -123), ('dealIntoNewStack', 0)])


    def test_deck10combined1(self):
        cards = Deck(10)
        instr=['deal with increment 7', 'deal into new stack', 'deal into new stack']
        shuffle = day_22.readInstructions(instr)
        day_22.moveCards(shuffle,cards)
        self.assertEqual(cards.deck, [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])

    def test_deck10combined2(self):
        cards = Deck(10)
        instr=['cut 6','deal with increment 7','deal into new stack']
        shuffle = day_22.readInstructions(instr)
        day_22.moveCards(shuffle,cards)
        
        self.assertEqual(cards.deck, [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])
     
    def test_deck10combined3(self):
        cards = Deck(10)
    
        instr=['deal with increment 7',
        'deal with increment 9',
        'cut -2',
        'shuffle = day_22.readInstructions(instr)',
        'day_22.moveCards(shuffle,cards)']
        shuffle = day_22.readInstructions(instr)
        day_22.moveCards(shuffle,cards)
        self.assertEqual(cards.deck, [6, 3, 0, 7, 4, 1, 8, 5, 2, 9])
 
    def test_deck10combined4(self):
        cards = Deck(10)
    
        instr=['deal into new stack',
        'cut -2',
        'deal with increment 7',
        'cut 8',
        'cut -4',
        'deal with increment 7',
        'cut 3',
        'deal with increment 9',
        'deal with increment 3',
        'cut -1']

        shuffle = day_22.readInstructions(instr)
        day_22.moveCards(shuffle,cards)
        self.assertEqual(cards.deck, [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
    
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_22_test.py

