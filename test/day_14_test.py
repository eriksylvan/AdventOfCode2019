import unittest
import day_14

class TestDay14(unittest.TestCase):
    
    #@unittest.skip("Skip")
    def test_createChemical_1ORE(self):
        self.assertEqual(day_14.createChemical('ORE',1, storage={},reactios={}, oreUsed=0), 1)

    def test_createChemical_99ORE(self):
        self.assertEqual(day_14.createChemical('ORE',99,storage={},reactios={}, oreUsed=0),99)

    def test_createChemical_getFromStorage(self):
        self.assertEqual(day_14.createChemical('LEAD',4,storage={'LEAD':8},reactios={}, oreUsed=0), 0)

    def test_createChemical_lookupReaction(self):
        self.assertEqual(day_14.createChemical('FUEL',1,storage={},reactios=reactions2, oreUsed=0), 165 )

    def test_createChemical_reactions1_fuel(self):
        self.assertEqual(day_14.createChemical('FUEL',1,storage={},reactios=reactions1, oreUsed=0), 31)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_14_test.py




##########################
#  TEST DATA
##########################

reactions1 = {
'A': [10, {'ORE': 10}], 
'B': [1, {'ORE': 1}], 
'C': [1, {'A': 7, 'B': 1}], 
'D': [1, {'A': 7, 'C': 1}], 
'E': [1, {'A': 7, 'D': 1}], 
'FUEL': [1, {'A': 7, 'E': 1}]
}

reactions2 = {
    'A': [2, {'ORE': 9}], 
    'B': [3, {'ORE': 8}], 
    'C': [5, {'ORE': 7}], 
    'AB': [1, {'A': 3, 'B': 4}], 
    'BC': [1, {'B': 5, 'C': 7}], 
    'CA': [1, {'C': 4, 'A': 1}], 
    'FUEL': [1, {'AB': 2, 'BC': 3, 'CA': 4}]
    }