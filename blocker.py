class Blocker():
    
    import pygame

    def __init__(self, display_width = 800, display_height = 600):
        self.pygame.init()

        _width = 800
        _height = 600

        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.darkBlue = (0,0,128)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (128, 128, 128)
        self.pink = (255,200,200)
        self._gameDisplay = self.pygame.display.set_mode((display_width,display_height))
        self.pygame.display.set_caption('Blocker')
        self._clock = self.pygame.time.Clock()

    def draw_block(self, x,y,size, lColor, fColor):
        self.pygame.draw.rect(self._gameDisplay, fColor, [x, y, size, size],0)
        self.pygame.draw.rect(self._gameDisplay, lColor, [x, y, size, size],2)
        
   
    def screen_update(self):
        self.pygame.display.update()


if __name__ == "__main__":

    import time
    BLCK = Blocker()
    BLCK.draw_block(10, 10, 10, BLCK.white, BLCK.red )
    BLCK.screen_update()
    time.sleep(5)



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