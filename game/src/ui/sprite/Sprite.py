import pygame

from src.core.utils.Dimensions import Dimensions

class Sprite:
    GROUND_TILE_SIZE = 64
    COLLISION_MARGIN = 10

    def __init__(self, path):
        self.__image = pygame.image.load(path).convert_alpha()
        self.__rect = self.__image.get_rect() # Sprite top left corner coordinates
        self.__collision = pygame.Rect(self.__rect.topleft, (self.__rect.w - 2 * self.COLLISION_MARGIN, self.__rect.h - 2 * self.COLLISION_MARGIN))

    def get(self):
        return self.__image

    def getRect(self):
        return self.__rect

    def getSize(self):
        return Dimensions(*self.__image.get_size())

    def getCollision(self):
        return self.__collision
        
    def setPosition(self, position):
        self.__rect.topleft = position.toTuple()
        position += self.COLLISION_MARGIN
        self.__collision.topleft = position.toTuple()
