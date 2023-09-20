import os, pygame , csv
from settings import *


class Tiles(pygame.sprite.Sprite):
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)                   
        self.offsetX = 0
        
        self.sky = pygame.image.load("greedIslandV2Assets/Background.png")
        self.sky = pygame.transform.scale(self.sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.skyRect = self.sky.get_rect()
        self.platforms = []
        self.dirt_bg = pygame.image.load("greedIslandV2Assets/raw\mapAssets/blockybottom.png").convert_alpha()
        
        
        tile_image_paths = {
                    '483':"assetsbox/tile_483.png",
                    '482':"assetsbox/tile_482.png",
                    '481':"assetsbox/tile_481.png",
                    '476':"assetsbox/tile_476.png",
                    '475':"assetsbox/tile_475.png",
                    '474':"assetsbox/tile_474.png",
                    '473':"assetsbox/tile_473.png",
                    '472':"assetsbox/tile_472.png",
                    '471':"assetsbox/tile_471.png",
                    '470':"assetsbox/tile_470.png",
                    '469':"assetsbox/tile_469.png",
                    '468':"assetsbox/tile_468.png",
                    '467':"assetsbox/tile_467.png",
                    '466':"assetsbox/tile_466.png",
                    '465':"assetsbox/tile_465.png",
                    '464':"assetsbox/tile_464.png",
                    '440':"assetsbox/tile_440.png",
                    '439':"assetsbox/tile_439.png",
                    '415':"assetsbox/tile_415.png",
                    '414':"assetsbox/tile_414.png",
                    '361':"assetsbox/tile_361.png",
                    '336':"assetsbox/tile_336.png",
                    '260':"assetsbox/tile_260.png",
                    '257':"assetsbox/tile_257.png",
                    '240':"assetsbox/tile_240.png",
                    '188':"assetsbox/tile_188.png",
                    '187':"assetsbox/tile_187.png",
                    '186':"assetsbox/tile_186.png",
                    '176':"assetsbox/tile_176.png",
                    '26':"assetsbox/tile_26.png",
                }
        y_position = 0
        # this for loop reads each value in the level_map list and appends an image at the location of the value 'X' in the list
        with open(os.path.join("greedIslandV2Assets/raw/mainMap.csv")) as data:
            data = csv.reader(data,delimiter=',')
            for row in data:
                x_position = 0
                for tile in row:
                    image_path = tile_image_paths.get(tile)
                    if image_path:
                        self.Ndirt_bg = pygame.image.load(image_path).convert_alpha()
                        self.Ndirt_bg = pygame.transform.scale(self.Ndirt_bg, (16, 16))
                        self.Ndirt_bg_rect = self.Ndirt_bg.get_rect()
                        self.Ndirt_bg_rect.x = x_position * 16
                        self.Ndirt_bg_rect.y = y_position * 16
                        block = (self.Ndirt_bg, self.Ndirt_bg_rect)
                        self.platforms.append(block)
                    x_position += 1
                y_position += 1        

    def draw_tile(self,screen):
        screen.blit(self.sky,self.skyRect)
        for tile_1 in self.platforms:
            screen.blit(tile_1[0], tile_1[1])
            #tile_1[1] represents the rect of the tile and we increment the x position of the tile by a number
               