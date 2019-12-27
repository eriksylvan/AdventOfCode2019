class Planet:
    def __init__(self,pos,vel):
        self.pos=pos
        self.vel=vel
    
    def __str__(self):
        return f'Position: {self.pos} Velocity: {self.vel}\n'

    def move(self):
        for i in range(3):
            self.pos[i]=self.pos[i]+self.vel[i]
    
    def moveOneDimension(self,dim):
        self.pos[dim]=self.pos[dim]+self.vel[dim]

    def gravity(self,otherPlanet):
        for i in range(3):
            if self.pos[i]<otherPlanet.pos[i]:
                self.vel[i]=self.vel[i]+1
            if self.pos[i]>otherPlanet.pos[i]:
                self.vel[i]=self.vel[i]-1

    def gravityOneDimension(self,otherPlanet,dim):
        if self.pos[dim]<otherPlanet.pos[dim]:
            self.vel[dim]=self.vel[dim]+1
        if self.pos[dim]>otherPlanet.pos[dim]:
            self.vel[dim]=self.vel[dim]-1
    
    def getVelocityOneDimension(self,dim):
        return self.vel[dim]
    
    def getPositionOneDimension(self,dim):
        return self.pos[dim]

    def energy(self):
        potentialEnergy=0
        kineticEnergy=0
        for i in range(3):
            potentialEnergy=potentialEnergy+abs(self.pos[i])
            kineticEnergy=kineticEnergy+abs(self.vel[i])
        energy=potentialEnergy*kineticEnergy
        return energy

                





