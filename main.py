import pygame, sys
from characters import Protagonist1
from settings import SCREEN_HEIGHT,SCREEN_WIDTH

pygame.init()


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.walkingRight = False
        self.GonChar = Protagonist1(300,500)
        
    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.walkingRight = True
                        
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.walkingRight = False
             
              
            self.screen.fill((0,50,135))
            self.GonChar.draw(self.screen) 
            self.GonChar.animation()
            self.GonChar.yCollisions()
            self.GonChar.physics()
            
            
            if self.walkingRight:
                self.GonChar.override_currentAction(1)
                self.GonChar.move()
            else:
                self.GonChar.override_currentAction(0)
            
            self.clock.tick(60)
            pygame.display.update()
   
     
if __name__ == '__main__':
    main = Main()
    main.run()
            
  
       

        
                
        
                
        
    
            
    