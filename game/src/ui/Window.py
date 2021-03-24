import pygame

class Window:
    def __init__(self):
        self.__height = 720
        self.__width = 1080
        pygame.init()
        self.screen = pygame.display.set_mode((self.__width, self.__height))

    """ Returns window size in pixel """
    def getSize(self):
        return (self.__width, self.__height)
    

    
