import pygame


class Window:
    def __init__(self):
        self.__height = 720
        self.__width = 1080

        pygame.init()
        self.screen = pygame.display.set_mode((self.__width, self.__height))

    def getHeight(self):
        return self.__height
    
    def getWidth(self):
        return self.__width
    

    
