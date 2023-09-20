import pygame, sys
from characters import Protagonist1
from settings import SCREEN_HEIGHT,SCREEN_WIDTH
from tiles import *

pygame.init()


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.walkingRight = False
        self.walkingLeft = False
        self.jumping = False
        self.boosting = False
        self.GonChar = Protagonist1(300,500)
        
        self.map  = Tiles("greedIslandV2Assets/raw/mainMap.csv")
        
    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.jumping = True
                        
                    if event.key == pygame.K_d:
                        self.walkingRight = True
                        
                    if event.key == pygame.K_a:
                        self.walkingLeft = True
                    if event.key == pygame.K_e:
                        self.boosting = True
                        
                        
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.jumping = False
                    if event.key == pygame.K_d:
                        self.walkingRight = False
                        
                    if event.key == pygame.K_a:
                        self.walkingLeft = False
                    if event.key == pygame.K_e:
                        self.boosting = False
             
              
            
            self.map.draw_tile(self.screen)
            self.GonChar.draw(self.screen) 
            self.GonChar.animation(self.walkingRight)
            self.GonChar.yCollisions()
            self.GonChar.physics()
            
            
            if self.walkingLeft:
                self.GonChar.override_currentAction(1)
                self.GonChar.moveLeft()
            elif self.walkingRight:
                self.GonChar.override_currentAction(1)
                self.GonChar.moveRight()
            elif self.jumping:
                self.GonChar.jump()
            elif self.boosting:
                self.GonChar.override_currentAction(2)
                
            else:
                self.GonChar.override_currentAction(0)
            
            self.clock.tick(60)
            pygame.display.update()
   
     
if __name__ == '__main__':
    main = Main()
    main.run()
            
  
       

        
                
        
                
        
    
            
    