import pygame
import pygame.freetype
from game.src.core.pair.Dimensions import Dimensions
class Text:
    def __init__(self, text, buttonPosition, buttonSize):
        self.__ZOOM = 1.2
        self.__DEFAULT_FONT_SIZE = 30
        self.__HIGHLIGHTED_FONT_SIZE = self.__DEFAULT_FONT_SIZE * self.__ZOOM

        self.__text = text

        self.__buttonPosition = buttonPosition
        self.__buttonSize = buttonSize

        self.__surface = self.createSurface(self.__DEFAULT_FONT_SIZE)

        self.__rect = self.__surface.get_rect()
        self.__position = (buttonPosition + buttonSize // 2) - self.getSize() // 2

    def get(self):
        return self.__surface
    
    def getSize(self):
        return Dimensions(self.__rect.width , self.__rect.height)

    def getPosition(self):
        return self.__position
    
    def createSurface(self, size):
        font = pygame.freetype.SysFont("Consolas", size, bold=True)
        surface, _ = font.render(self.__text, fgcolor=(225,225,20))
        return surface.convert_alpha()

    def setPosition(self):
        self.__rect = self.__surface.get_rect()
        self.__position = (self.__buttonPosition + self.__buttonSize // 2) - self.getSize() // 2

    def highlight(self):
        self.__surface = self.createSurface(self.__HIGHLIGHTED_FONT_SIZE)
        self.setPosition()
              

    def default(self):
        self.__surface = self.createSurface(self.__DEFAULT_FONT_SIZE)
        self.setPosition()
    
