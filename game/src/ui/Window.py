import pygame

class Window:
    FPS = 244

    def __init__(self):
        self.__height = 720
        self.__width = 1080
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__clock = pygame.time.Clock()

    """ Returns window size in pixel """
    def getSize(self):
        return (self.__width, self.__height)

    """ This clock ensures to have FPS Frame Per Second"""
    def clock(self):
        self.__clock.tick(self.FPS)

    def getScreen(self):
        return self.__screen
    

    
