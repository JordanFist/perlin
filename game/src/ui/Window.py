import pygame

class Window:
    FPS = 244
    WIDTH = 1080
    HEIGHT = 720

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Perlin")
        pygame.mouse.set_visible(False)
        
        self.__screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.__clock = pygame.time.Clock()

    #""" Returns window size in pixel """
    #def getSize(self):
    #    return (self.__width, self.__height)

    """ This clock ensures to have FPS Frame Per Second"""
    def clock(self):
        self.__clock.tick(self.FPS)

    def getScreen(self):
        return self.__screen
    

    
