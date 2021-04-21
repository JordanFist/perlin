import pygame

from src.core.utils.Dimensions import Dimensions

class Sprite:
    GROUND_TILE_SIZE = 64

    def __init__(self, path):
        self.__image = pygame.image.load(path).convert_alpha()
        self.__rect = self.__image.get_rect() # Sprite top left corner coordinates

    def get(self):
        return self.__image

    def getRect(self):
        return self.__rect

    def getSize(self):
        return Dimensions(*self.__image.get_size())
        
    def setPosition(self, position):
        self.__rect.topleft = position.toTuple()

    

