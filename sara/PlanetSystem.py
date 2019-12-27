class PlanetSystem:
    def __init__ (self,planets):
        self.planets=planets

    def __str__(self):
        str=''
        for planet in range(4):
            str=str+f'Planet Nr: {planet} {self.planets[planet]}'
        return str

    def moveOneTimeStep(self,dim):
        for planetA in range(4):
            for planetB in range(4):
                self.planets[planetA].gravityOneDimension(self.planets[planetB],dim)
        for planetA in range(4):
            self.planets[planetA].moveOneDimension(dim)
    
    def getVelocity(self,dim):
        velocties=[]
        for planet in range(4):
            velocties.append(int(self.planets[planet].getVelocityOneDimension(dim)))
        return velocties


def movePlanetsTest(planets,steps):
    for dim in range(3):
        for step in range(steps):
            for planetA in range(len(planets)):
                for planetB in range(len(planets)):
                    planets[planetA].gravityOneDimension(planets[planetB],dim)
            for planetA in range(len(planets)):
                planets[planetA].moveOneDimension(dim)
    return planets