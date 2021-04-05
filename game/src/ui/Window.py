import pygame

from game.src.core.pair.Dimensions import Dimensions

class Window:
    def __init__(self):
        self.__INITIAL_WIDTH = 1080
        self.__INITIAL_HEIGHT = 720
        self.__MINIMUM_WIDTH = 600
        self.__MINIMUM_HEIGHT = 400
        self.__FPS = 244
        
        pygame.init()
        pygame.display.set_caption("Perlin")
        #pygame.mouse.set_visible(False)

        self.__screen = pygame.display.set_mode((self.__INITIAL_WIDTH, self.__INITIAL_HEIGHT), pygame.RESIZABLE)
        self.__clock = pygame.time.Clock()

    """ Returns window size """
    @staticmethod
    def getSize():
        return Dimensions(*pygame.display.get_surface().get_size())

    """ This clock ensures to have __FPS Frames Per Second """
    def clock(self):
        self.__clock.tick(self.__FPS)

    def getScreen(self):
        return self.__screen

    def resizeScreen(self, width, height):
        if (width < self.__MINIMUM_WIDTH):
            width = self.__MINIMUM_WIDTH
        if (height < self.__MINIMUM_HEIGHT):
            height = self.__MINIMUM_HEIGHT
        self.__screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    

    
