import pygame
from game.src.core.TilesEnum import TilesEnum
from game.src.core.Converter import Converter

class Background:
    def __init__(self, map, spriteStore):
        self.__map = map
        self.__spriteStore = spriteStore
        self.__background = pygame.Surface(self.__map.getSize().toTuple())
        self.__load()

    def get(self):
        return self.__background

    def __load(self):
        map = self.__map.get()

        for row in range(len(map)):
            for col in range(len(map[0])):
                value = map[row][col]

                tile = self.__spriteStore.get("grounds", TilesEnum.getID(value))
                tilePosition = (Converter.indexToPixel(col), Converter.indexToPixel(row))
                self.__background.blit(tile.get(), tilePosition)