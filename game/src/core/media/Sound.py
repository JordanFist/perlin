import pygame
import glob, os
from math import sqrt
from random import choice
from numpy import inf

from src.core.utils.Coordinates import Coordinates
from src.core.utils.Indexes import Indexes
from src.core.enums.Tiles import Tiles
from src.ui.Window import Window

class Sound:
    # Volume
    FOOTSTEP_VOLUME = 0.03
    SEA_VOLUME = 0.7
    ENVIRONMENT_VOLUME = 1

    # Waiting time before the next sound is played (in ms)
    NORMAL_FOOTSTEP = 240
    RUNNING_FOOTSTEP = 200
    NEXT_FOOTSTEP = NORMAL_FOOTSTEP
    NEXT_SEA_CHECK = 200

    # Radius where the sea is audible
    AUDIBLE_SEA_RADIUS = 20

    def __init__(self):
        self.__PATH = "resources/sounds/"
        self.__sounds = {}
        self.__load()
        self.__setVolume()

        self.__nextFootStep = 0
        self.__nextSeaCheck = 0

        self.__canHearSea = False

    def __load(self):
        folders = [os.path.basename(folder) for folder in glob.glob(self.__PATH + "*")]
        for folder in folders:
            self.__sounds[folder] = []
            fileNames = [os.path.splitext(os.path.basename(fileName))[0] for fileName in glob.glob(self.__PATH + folder + "/" + "*")]
            for name in fileNames:
                sound = pygame.mixer.Sound(self.__PATH + folder + "/" + name + ".mp3")
                self.__sounds[folder].append(sound)

    def walk(self):
        self.NEXT_FOOTSTEP = self.NORMAL_FOOTSTEP

    def run(self):
        self.NEXT_FOOTSTEP = self.RUNNING_FOOTSTEP

    def __setVolume(self):
        for key in self.__sounds.keys():
            if key == str(Tiles.GRASS) or key == str(Tiles.SAND):
                for sound in self.__sounds[key]:
                    sound.set_volume(self.FOOTSTEP_VOLUME)

    def footstep(self, tile):
        if Window.getTicks() > self.__nextFootStep:
            try:
                sound = choice(self.__sounds[str(tile)])
                sound.play()
            except: 
                print("error can't play a sound for this tile")
            self.__nextFootStep = Window.getTicks() + self.NEXT_FOOTSTEP

    def sea(self, map, player):
        if Window.getTicks() > self.__nextSeaCheck:
            distance = self.__distanceFromSea(map, player)
            if self.__canHearSea:
                if distance > self.AUDIBLE_SEA_RADIUS:
                    self.__canHearSea = False
                    self.__sounds["sea"][0].stop()
                else:
                    self.__sounds["sea"][0].set_volume(self.SEA_VOLUME - self.SEA_VOLUME/self.AUDIBLE_SEA_RADIUS * distance)
            else:
                if distance <= self.AUDIBLE_SEA_RADIUS:
                    self.__canHearSea = True
                    self.__sounds["sea"][0].play()
                    self.__sounds["sea"][0].set_volume(self.SEA_VOLUME - self.SEA_VOLUME/self.AUDIBLE_SEA_RADIUS * distance)
            self.__nextSeaCheck = Window.getTicks() + self.NEXT_SEA_CHECK

    def __distanceFromSea(self, map, player):
        pos = map.getIndex(Coordinates(*player.getCorners().midbottom))
        radius = 0
        visited = set()
        currentLayer = set()
        nextLayer = set()
        nextLayer.add((pos.row, pos.col))
        while (radius < self.AUDIBLE_SEA_RADIUS and len(nextLayer) != 0):
            currentLayer = nextLayer.copy()
            nextLayer.clear()
            for current in currentLayer:
                visited.add(current)
                if map.get()[current[0]][current[1]].getTileID() == Tiles.SHALLOW_WATER:
                    return sqrt((current[0] - pos.row) ** 2 + (current[1] - pos.col) ** 2)
                for neighbor in [(current[0] - 1, current[1] - 1), (current[0] - 1, current[1]), (current[0] - 1, current[1] + 1),  (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0] + 1, current[1] - 1), (current[0] + 1, current[1]), (current[0] + 1, current[1] + 1)]: 
                    if neighbor not in visited and neighbor not in nextLayer and (current[0] - pos.row) ** 2 + (current[1] - pos.col) ** 2 <= radius ** 2 and map.isInMap(Indexes(neighbor[0], neighbor[1])):
                        nextLayer.add((neighbor[0], neighbor[1]))
            radius += 1
        return inf