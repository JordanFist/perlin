import pygame
import sys

from src.core.utils.Dimensions import Dimensions
from src.core.enums.Direction import Direction
from src.core.enums.States import States

class Window:
    ONE_FRAME_DURATION = 120

    def __init__(self):
        self.__INITIAL_WIDTH = 1080
        self.__INITIAL_HEIGHT = 720
        self.__MINIMUM_WIDTH = 600
        self.__MINIMUM_HEIGHT = 400
        self.__ICON_PATH = "resources/icon/icon.png"
        self.__FPS = 300
        
        pygame.init()
        pygame.display.set_caption("Perlin")
        pygame.display.set_icon(pygame.image.load(self.__ICON_PATH))

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

    def getTicks(self):
        return pygame.time.get_ticks()

    def getFPS(self):
        return self.__clock.get_fps()

    """ Returns the elapsed time in second between 2 calls """
    def getTime(self):
        return self.__clock.get_time() / 1000

    def isClosed(self, event):
        if event.type == pygame.QUIT:
            return True
        return False

    def close(self):
        pygame.quit()
        sys.exit()

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