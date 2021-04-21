import pygame

from src.core.enums.Tiles import Tiles
from src.core.utils.Converter import Converter

from src.ui.background.Background import Background

class BackgroundGame(Background):
    def __init__(self, map, spriteStore):
        super().__init__(pygame.Surface(map.getSize().toTuple(), depth=24))
        self.__map = map
        self.__spriteStore = spriteStore
        self.__load()

    def __load(self):
        map = self.__map.get()

        for row in range(len(map)):
            for col in range(len(map[0])):
                value = map[row][col]
                tile = self.__spriteStore.get("tiles", Tiles.getID(value))
                tilePosition = (Converter.indexToPixel(col), Converter.indexToPixel(row))
                self._background.blit(tile.get(), tilePosition)
                
        self._background = self._background.convert_alpha()