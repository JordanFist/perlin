import pygame

from game.src.core.utils.Dimensions import Dimensions
from game.src.core.enums.States import States

class Window:
    def __init__(self):
        self.__INITIAL_WIDTH = 1080
        self.__INITIAL_HEIGHT = 720
        self.__MINIMUM_WIDTH = 600
        self.__MINIMUM_HEIGHT = 400
        self.__FPS = 244
        
        pygame.init()
        pygame.display.set_caption("Perlin")

        self.__screen = pygame.display.set_mode((self.__INITIAL_WIDTH, self.__INITIAL_HEIGHT), pygame.RESIZABLE)
        self.__clock = pygame.time.Clock()

    """ Returns window size """
    @staticmethod
    def getSize():
        return Dimensions(*pygame.display.get_surface().get_size())

    def getScreen(self):
        return self.__screen

    """ This clock ensures to have __FPS Frames Per Second """
    def clock(self):
        self.__clock.tick(self.__FPS)

    def isClosed(self, event):
        if event.type == pygame.QUIT:
            return States.QUIT
        return States.CONTINUE

    def close(self):
        pygame.quit()
        quit()

    def isResized(self, event):
        if event.type == pygame.VIDEORESIZE:
            return True
        return False

    def resize(self, width, height):
        if (width < self.__MINIMUM_WIDTH):
            width = self.__MINIMUM_WIDTH
        if (height < self.__MINIMUM_HEIGHT):
            height = self.__MINIMUM_HEIGHT
        self.__screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    

    
