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

    def getVelocity(self):
        return self._velocity

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

    def isAtEndpoint(self):
        # print(self._velocity[0]==0, self._velocity[1]==0, self._velocity[2]==0)
        # print(self._velocity[0], self._velocity[1], self._velocity[2])
        return (self._velocity[0]==0 and self._velocity[1]==0 and self._velocity[2]==0)



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


###########
def findTurningPointOneDim(inData):

    planets = []
    for i in range(4):
        planets.append(Planet(inData[i],[0,0,0]))
    steps = 0
    
    while (steps==0 or (                           \
            not planets[0].isAtEndpoint() or \
            not planets[1].isAtEndpoint() or \
            not planets[2].isAtEndpoint() or \
            not planets[3].isAtEndpoint() )):
            steps=steps+1
            newPlanetPositions(planets)


    return steps * 2

def findTurningPointsXYZ():
    Xsteps = findTurningPointOneDim([[-1,0,0],[4,0,0],[-14,0,0],[1,0,0]])
    print(f'Xfound: {Xsteps}')
    Ysteps = findTurningPointOneDim([[0,-4,0],[0,7,0],[0,-10,0],[0,2,0]])
    print(f'Yfound: {Ysteps}')
    Zsteps = findTurningPointOneDim([[0,0,0],[0,0,-1],[0,0,9],[0,0,17]])
    print(f'Zfound: {Zsteps}')
    return Xsteps, Ysteps, Zsteps




def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b using Euclidean algorithm

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
        returns the Lowest Common Multiple 
    """
    return (a * b) // gcd(a, b)

def day12PartOne():
    planetsStartPos = [[-1,-4,0],[4,7,-1],[-14,-10,9],[1,2,17]]
    eTot, outData = getPlanestData(planetsStartPos, 1000)
    print(f'Solution Day 12, Part one:\nTotal energy after 1000 steps: {eTot} \n\n')


def day12PartTwo():
    # planetsStartPos = [[-1,-4,0],[4,7,-1],[-14,-10,9],[1,2,17]]
    Xsteps, Ysteps, Zsteps = findTurningPointsXYZ()
    # finally find the lowest multiple of the Greatest Common Divider
    answer = lcm(Xsteps, lcm(Ysteps, Zsteps))
    print(f'Solution Day 12, Part two:\n The four planets will be back at the starting position after {answer} steps. \n\n')


if __name__ == "__main__":
    day12PartOne()
    day12PartTwo()


# Solution Day 12, Part one:
# Total energy after 1000 steps: 7988
# Xfound: 231614
# Yfound: 193052
# Zfound: 60424
# Solution Day 12, Part two:
#  The four planets will be back at the starting position after 337721412394184 steps.


# Run from terminal:
# $ python day_12.py
