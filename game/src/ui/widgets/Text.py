import pygame.freetype
from game.src.core.utils.Dimensions import Dimensions
from game.src.ui.utils.Position import Position

class Text:
    ZOOM = 1.2
    DEFAULT_FONT_SIZE = 30
    HIGHLIGHTED_FONT_SIZE = DEFAULT_FONT_SIZE * ZOOM
    FONT = "georgia"
    DEFAULT_COLOR = "gold"

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
        font = pygame.freetype.SysFont(self.FONT, size, bold=True)
        surface, _ = font.render(self.__message, fgcolor=self.DEFAULT_COLOR)
        self.__text = surface.convert_alpha()
        self.__rect = self.__text.get_rect()

    def update(self, position=None):
        if position:
            self.setPosition(position)