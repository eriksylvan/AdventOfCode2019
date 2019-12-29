import itertools

items = ('spool of cat6', 
            'hypercube',
            'weather machine',
            'coin',
            'candy cane',
            'tambourine',
            'fuel cell',
            'mutex')

def combs(x):
    return [c for i in range(len(x)+1) for c in itertools.combinations(x,i)]

allCombinations = combs(items)

trystring = []
for i in allCombinations:
    print('-== next try ==-')
    takeString =''
    dropString =''
    for item in i:
        takeString += f'take {item}\n'
        dropString += f'drop {item}\n'
    print(takeString)
    print(dropString)
    trystring.append(takeString)
    trystring.append('west\n')
    trystring.append(dropString)
print(trystring)
