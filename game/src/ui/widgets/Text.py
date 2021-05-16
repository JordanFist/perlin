import pygame.freetype

from src.core.utils.Dimensions import Dimensions
from src.core.utils.PathManager import PathManager

from src.ui.utils.Position import Position

class Text:
    ZOOM = 1.2
    DEFAULT_FONT_SIZE = 45
    HIGHLIGHTED_FONT_SIZE = int(DEFAULT_FONT_SIZE * ZOOM)
    PATH = "resources/fonts/"
    DEFAULT_COLOR = "white"

    def __init__(self, message, position=None, margin=None):
        self.__message = message
        self.__position = position
        self.__margin = margin
        self.__rect = None
        self.__text = None
        self.__createSurface(self.DEFAULT_FONT_SIZE)
        if position:
            self.__rect = Position.getRect(position, self.getSize(), margin).topleft

    def get(self):
        return self.__text
    
    def getRect(self):
        return self.__rect

    def getSize(self):
        return Dimensions(*self.__rect.size)

    def setPosition(self, position):
        self.__rect.topleft = position.toTuple()

    def highlight(self):
        self.__createSurface(self.HIGHLIGHTED_FONT_SIZE)

    def default(self):
        self.__createSurface(self.DEFAULT_FONT_SIZE)

    def __createSurface(self, size): 
        font = pygame.font.Font(PathManager.addPath(self.PATH + "bringBackJustice.otf"), size)
        surface = font.render(self.__message, True, self.DEFAULT_COLOR)
        self.__text = surface.convert_alpha()
        self.__rect = self.__text.get_rect()

    def update(self, position=None):
        if position:
            self.setPosition(position)