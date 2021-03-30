import pygame

class Window:
    def __init__(self):
        self.__INITIAL_WIDTH = 1080
        self.__INITIAL_HEIGHT = 720
        self.__FPS = 244
        
        pygame.init()
        pygame.display.set_caption("Perlin")
        #pygame.mouse.set_visible(False)

        self.__screen = pygame.display.set_mode((self.__INITIAL_WIDTH, self.__INITIAL_HEIGHT), pygame.RESIZABLE)
        self.__clock = pygame.time.Clock()

    """ Returns window size in pixel """
    @staticmethod
    def getSize():
        return pygame.display.get_surface().get_size()

    @staticmethod
    def getWidth():
        return pygame.display.get_surface().get_width()

    @staticmethod
    def getHeight():
        return pygame.display.get_surface().get_height()

    """ This clock ensures to have __FPS Frame Per Second """
    def clock(self):
        self.__clock.tick(self.__FPS)

    def getScreen(self):
        return self.__screen

    def resizeScreen(self, width, height):
        self.__screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    

    
