import pygame

from game.src.core.pair.Dimensions import Dimensions

class Sprite:
    GROUND_TILE_SIZE = 32

    def __init__(self, path):
        self.__image = pygame.image.load(path).convert_alpha()
        self.__rect = self.__image.get_rect() # Sprite top left corner coordinates
        #self.__image = pygame.transform.scale(self.__image, (self.GROUND_TILE_SIZE, self.GROUND_TILE_SIZE))

    def get(self):
        return self.__image

    def setPosition(self, position):
        self.__rect.topleft = position.toTuple()

    def getRect(self):
        return self.__rect

    def getSize(self):
        return Dimensions(*self.__image.get_size())
    

