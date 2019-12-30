class LabVis():
    
    import pygame

    def __init__(self, display_width = 50, display_height = 50, block_size = 20):
        self.pygame.init()

        self._display_width = display_width
        self._display_height = display_height
        
        self._width = display_width * block_size
        self._height = display_height * block_size
        self._block_size = block_size

        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,128,255)
        self.darkBlue = (0,0,128)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.gray = (128, 128, 128)
        self.lightGray = (224, 224, 224)
        self.pink = (255,200,200)
        self.yellow = (255,255, 0)
        self._gameDisplay = self.pygame.display.set_mode((self._width,self._height))
        self.pygame.display.set_caption('Labyrinth')
        self._clock = self.pygame.time.Clock()

    def draw_block(self, x,y,size, lColor, fColor):
        xpos = x * self._block_size 
        ypos = y * self._block_size
        self.pygame.draw.rect(self._gameDisplay, fColor, [xpos, ypos , self._block_size, self._block_size],0)
        self.pygame.draw.rect(self._gameDisplay, lColor, [xpos, ypos, self._block_size, self._block_size],1)
        
    # def drawBrick(self ,x ,y ,t):
    #     # shape = [(self._side * x, self._side * y), ((self._side * x + self._side1, self._side * y + self._side))]
    #     if t == 0:
    #         self.draw_block(x,y,20, self.black, self.black)
    #     elif t == 1:
    #         self.draw_block(x,y,20, self.red, self.gray)
    #     elif t == 2:
    #         self.draw_block(x,y,20, self.red, self.yellow)
    #     elif t == 3:
    #         self.draw_block(x,y,20, self.yellow, self.blue)
    #     elif t == 4:
    #         self.draw_block(x,y,20, self.red, self.white)

    def drawStart(self, x,y):
            self.draw_block(x,y,self._block_size, self.black, self.green)

    def drawWall(self, x,y):
            self.draw_block(x,y,self._block_size, self.gray, self.gray)

    def drawPath(self, x,y):
            self.draw_block(x,y,self._block_size, self.lightGray, self.lightGray)
        
    def drawDroid(self, x,y):
            self.draw_block(x,y,self._block_size, self.black, self.yellow)
 
    def drawUnknown(self, x,y):
            self.draw_block(x,y,self._block_size, self.gray, self.black)
 
    def drawGoal(self, x,y):
            self.draw_block(x,y,self._block_size, self.black, self.red)

    def drawOxygen(self, x,y):
            self.draw_block(x,y,self._block_size, self.blue, self.blue)
 

    def drawLabytinth(self, labyrinth):
        for ypos in range(self._display_height):
            for xpos in range(self._display_width):
                if (xpos,ypos) in labyrinth:
                    if labyrinth[(xpos,ypos)]:
                        self.drawPath(xpos,ypos)
                    else:
                        self.drawWall(xpos,ypos)
                else:
                    self.drawUnknown(xpos,ypos)

    def drawLabytinth2(self, labyrinth):
        for ypos in range(self._display_height):
            for xpos in range(self._display_width):
                if (xpos,ypos) in labyrinth:
                    if labyrinth[(xpos,ypos)][0]:
                        self.drawPath(xpos,ypos)
                    else:
                        self.drawWall(xpos,ypos)
                else:
                    self.drawWall(xpos,ypos)

    def draw_text(self,text):
        myfont = self.pygame.font.SysFont('impact', 30)
        textsurface = myfont.render(text, True, self.red)
        self.pygame.draw.rect(self._gameDisplay, self.black, [0, 0 ,59,  39], 0)
        self._gameDisplay.blit(textsurface,(0, 0))
  
    def screen_update(self):
        self.pygame.display.update()
        self.pygame.event.get()
        #self.pygame.display.flip()
        #self._clock.tick(30)

    def wait(self):
        self.pygame.event.wait()


if __name__ == "__main__":

    import time
    BLCK = LabVis()
    # BLCK.draw_block(10, 10, 10, BLCK.white, BLCK.red )
    # BLCK.screen_update()
    # time.sleep(5)
    print(BLCK.pygame.font.get_fonts())



'''

     if t == 0:
            self._imgD.rectangle(shape, fill="black", outline="black")
        elif t == 1:
            self._imgD.rectangle(shape, fill="gray", outline="red")
        elif t == 2:
            self._imgD.rectangle(shape, fill="yellow", outline="red")
        elif t == 3:
            self._imgD.rectangle(shape, fill="blue", outline="yellow")
        elif t == 4:
            self._imgD.rectangle(shape, fill="white", outline="red")

'''