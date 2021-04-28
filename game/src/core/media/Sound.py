import pygame
from random import choice
from numpy import inf

from src.core.utils.Coordinates import Coordinates
from src.core.enums.Tiles import Tiles
from src.ui.Window import Window

class Sound:
    def __init__(self):
        self.__PATH = "resources/sounds/"
        self.__sounds = []
        self.__load()
        self.__tick = 0

    def __load(self):
        self.__sounds.append(pygame.mixer.Sound(self.__PATH + "sea1.flac"))
        #self.__sounds.append(pygame.mixer.Sound(self.__PATH + "sea2.flac"))
        #self.__sounds.append(pygame.mixer.Sound(self.__PATH + "sea3.flac"))
        self.__sounds.append(pygame.mixer.Sound(self.__PATH + "sea4.flac"))

    def play(self):
        if Window.getTicks() > self.__tick:
            sound = choice(self.__sounds)
            sound.set_volume(0.05)
            sound.play()
            self.__tick = Window.getTicks() + 3000

    def distanceFromSea(self, map, player):
        pass