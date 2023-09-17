
import pygame
from settings import GRAVITY,SCREEN_HEIGHT
class Protagonist1(pygame.sprite.Sprite):
    def __init__(self,xCoordinate,yCoordinate):
        self.value = 0
        self.animationList = []
        self.updateTime = pygame.time.get_ticks()
        self.frameIndex = 0
        self.animationIndex = 0
        
        individualAnimList = []
        for i in range(4): # Idle Stance 
            character = pygame.image.load(f"greedIslandV2Assets/raw/gon/stance/{i}.png").convert_alpha()
            character = pygame.transform.scale(character, (100, 150))  
            # the list  is appended into a greater animation list
            individualAnimList.append(character)
        self.animationList.append(individualAnimList)
        
        individualAnimList = []
        for i in range(8): # run Stance 
            character = pygame.image.load(f"greedIslandV2Assets/raw/gon/run/{i}.png").convert_alpha()
            character = pygame.transform.scale(character, (100, 150))  
            # the list  is appended into a greater animation list
            individualAnimList.append(character)
        self.animationList.append(individualAnimList)
        
        
        self.image = self.animationList[self.animationIndex][self.frameIndex]
        self.imageRect = self.image.get_rect()
        
    def physics(self):
        self.imageRect.y += GRAVITY
        
    def yCollisions(self):
        
        if self.imageRect.bottom >= SCREEN_HEIGHT:
            self.imageRect.bottom = SCREEN_HEIGHT
        
    def animation(self):
        ANIMATION_COOLDOWN = 120
        # checks if enough time has passed since the last update
        self.image = self.animationList[self.animationIndex][self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime > ANIMATION_COOLDOWN:
            self.updateTime = pygame.time.get_ticks()
            self.frameIndex += 1
        if self.frameIndex >= len(self.animationList[self.animationIndex]):
            self.frameIndex = 0
        
    def override_currentAction(self, new_action):
        if new_action != self.animationIndex:
            self.animationIndex = new_action
            self.frameIndex = 0
            self.update_time = pygame.time.get_ticks()        
    def move(self):
        
        self.imageRect.x += 4
        
    def draw(self, screen1):
        screen1.blit(self.image,self.imageRect)