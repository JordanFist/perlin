import pygame

class Sprite:
    GROUND_TILE_SIZE = 64

    DEEP_WATER = 0
    SHALLOW_WATER = 1
    SAND = 2
    GRASS = 3

    def __init__(self, path):
        self.__image = pygame.image.load(path).convert_alpha()
        #self.__image = pygame.transform.scale(self.__image, (self.GROUND_TILE_SIZE, self.GROUND_TILE_SIZE)) TODO Gérer les sizes pour "zoomer"
    
    def get(self):
        return self.__image
    

