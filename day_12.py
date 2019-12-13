# https://adventofcode.com/2019/day/12

import copy

inputFile = 'input/12_input'


def getInputData():
    '''Reads the input file end returns the data in a list of int'''
    data = []
    with open(inputFile) as input:
        for line in input:
            data = [int(x) for x in line.split(',')]
    return data

class Planet:
    def __init__(self, position, velocity):
        self._position = position
        self._velocity = velocity
    
    def __str__(self):
        return f'pos=<x={self._position[0]},y={self._position[1]},z={self._position[2]}>,vel=<x={self._velocity[0]},y={self._velocity[1]},z={self._velocity[2]}>'

    @property
    def position(self):
        pass

    @property
    def velocity(self):
        pass

    @position.setter
    def position(self, val):
        _position = val

    @velocity.setter
    def velocity(self, val):
        _velocity = val

    def move(self):
        for i in range(3):
            self._position[i] += self._velocity[i]

    def calculateVelocity(self, otherPlanet):
        for i in range(3):
            if self._position[i] > otherPlanet._position[i]:
                self._velocity[i] -= 1
            elif  self._position[i] < otherPlanet._position[i]:
                self._velocity[i] = self._velocity[i] + 1
            else:
                pass # No change in velocity component when self._position[i] == otherPlanet.position[i] 
                
    def energy(self):
        e = 0
        v = 0
        for i in range(3):
             e += abs(self._position[i]) 
             v += abs(self._velocity[i])  
        return e * v


def newPlanetPositions(planets):
    for planet1 in planets:
        for planet2 in planets:
            planet1.calculateVelocity(planet2)

    for planet in planets:
        planet.move() 
    
    newPlanetPos = []
    for planet in planets:
        newPlanetPos.append(planet._position)

    return newPlanetPos
    

def getPlanestData(inData, steps):

    planets = []
    for i in range(4):
        planets.append(Planet(inData[i],[0,0,0]))

    for i in range(steps):
        newPlanetPositions(planets)

    eTot = 0
    outData = []
    for planet in planets:
        outData.append(str(planet))
        eTot += planet.energy()
    return eTot, outData

def stepsUntilPosRepeat(planetsStartPos):
    planets = []
    for i in range(4):
        planets.append(Planet(copy.deepcopy(planetsStartPos[i]),[0,0,0]))

    planetsPos = []
    stepcount=3
    planetsPos = newPlanetPositions(planets)
    planetsPos = newPlanetPositions(planets)
    while planetsStartPos != planetsPos:
        stepcount += 1
        planetsPos = newPlanetPositions(planets)
    return stepcount


def day12PartOne():
    planetsStartPos = [[-1,-4,0],[4,7,-1],[-14,-10,9],[1,2,17]]
    eTot, outData = getPlanestData(planetsStartPos, 1000)
    print(f'Solution Day 12, Part one:\nTotal energy after 1000 steps: {eTot} \n\n')


def day12PartTwo():
    planetsStartPos = [[-1,-4,0],[4,7,-1],[-14,-10,9],[1,2,17]]
    #example1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
    answer = stepsUntilPosRepeat(planetsStartPos)
    print(f'Solution Day 12, Part two:\nAnswer: {answer} \n\n')


if __name__ == "__main__":
    #day12PartOne()
    day12PartTwo()

  


# Run from terminal:
# $ python day_12.py
