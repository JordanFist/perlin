import pygame

class Sprite:
    GROUND_TILE_SIZE = 32

    def __init__(self, path):
        self.__image = pygame.image.load(path).convert_alpha()
        #self.__image = pygame.transform.scale(self.__image, (self.GROUND_TILE_SIZE, self.GROUND_TILE_SIZE)) TODO Gérer les sizes pour "zoomer"
    
    def get(self):
        return self.__image

    def getWidth(self):
        return self.__image.get_width()

    def getHeight(self):
        return self.__image.get_height()
    

