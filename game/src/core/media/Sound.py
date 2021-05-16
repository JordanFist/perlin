import pygame
import glob, os
from math import sqrt
from random import choice, randint
from numpy import inf

from src.core.utils.PathManager import PathManager
from src.core.utils.Coordinates import Coordinates
from src.core.utils.Indexes import Indexes
from src.core.enums.Tiles import Tiles
from src.ui.Window import Window

class Sound:
    # Volume
    FOOTSTEP_VOLUME = 0.03
    SEA_VOLUME = 0.7
    SEAGULL_VOLUME = 0.3
    BIRDS_VOLUME = 0.5

    # Waiting time before the next sound is played (in ms)
    NORMAL_FOOTSTEP = 240
    RUNNING_FOOTSTEP = 200
    NEXT_FOOTSTEP = NORMAL_FOOTSTEP
    NEXT_AMBIENT_UPDATE = 200
    MINIMUM_NEXT_SEAGULL = 7000
    MAXIMUM_NEXT_SEAGULL = 15000

    # Audible Radius
    AUDIBLE_SEA_RADIUS = 20
    AUDIBLE_BIRDS_RADIUS = 10

    def __init__(self):
        self.__PATH = "resources/sounds/"
        self.__sounds = {}
        self.__load()
        self.__setVolume()

        self.__distanceFromSea = inf

        self.__nextFootStep = 0
        self.__nextAmbientUpdate = 0
        self.__nextSeagull = 0

        self.__playingSeagull = None
        self.__isBeachPlaying = False
        self.__isBirdsPlaying = False

    def __load(self):
        folders = [os.path.basename(folder) for folder in glob.glob(PathManager.addPath((self.__PATH + "*")))] 
        for folder in folders:
            self.__sounds[folder] = []
            fileNames = [os.path.splitext(os.path.basename(fileName))[0] for fileName in glob.glob(PathManager.addPath(self.__PATH + folder + "/" + "*"))]
            for name in fileNames:
                sound = pygame.mixer.Sound(PathManager.addPath(self.__PATH + folder + "/" + name + ".mp3"))
                self.__sounds[folder].append(sound)

    def __setVolume(self):
        for key in self.__sounds.keys():
            if key == str(Tiles.GRASS) or key == str(Tiles.SAND):
                for sound in self.__sounds[key]:
                    sound.set_volume(self.FOOTSTEP_VOLUME)

    def walk(self):
        self.NEXT_FOOTSTEP = self.NORMAL_FOOTSTEP

    def run(self):
        self.NEXT_FOOTSTEP = self.RUNNING_FOOTSTEP

    def pause(self):
        pygame.mixer.pause()

    def unpause(self):
        pygame.mixer.unpause()

    def footstep(self, tile):
        if Window.getTicks() > self.__nextFootStep:
            try:
                sound = choice(self.__sounds[str(tile)])
                sound.play()
            except: 
                print("error can't play a sound for this tile")
            self.__nextFootStep = Window.getTicks() + self.NEXT_FOOTSTEP

    def beachVolumeSetter(self, maxVolume, distance):
        return maxVolume - maxVolume / self.AUDIBLE_SEA_RADIUS * distance

    def birdsVolumeSetter(self, maxVolume, distance):
        return (maxVolume / self.AUDIBLE_BIRDS_RADIUS) * (distance - self.AUDIBLE_BIRDS_RADIUS)

    def canHearBeach(self):
        if self.__distanceFromSea <= self.AUDIBLE_SEA_RADIUS:
            return True
        return False

    def ambientManager(self, map, player):
        if Window.getTicks() > self.__nextAmbientUpdate:
            self.__distanceFromSea = self.__updateDistanceFromBeach(map, player)
            self.birds()
            self.beach()
            self.seagull()
            self.__nextAmbientUpdate = Window.getTicks() + self.NEXT_AMBIENT_UPDATE

    def birds(self):
        if self.__isBirdsPlaying:
            if self.AUDIBLE_BIRDS_RADIUS < self.__distanceFromSea:
                self.__sounds["birds"][0].set_volume(self.birdsVolumeSetter(self.BIRDS_VOLUME, min(self.__distanceFromSea, self.AUDIBLE_SEA_RADIUS)))
            else:
                self.__sounds["birds"][0].stop()
                self.__isBirdsPlaying = False
        else:
            if self.AUDIBLE_BIRDS_RADIUS < self.__distanceFromSea:
                self.__sounds["birds"][0].play(-1)
                self.__sounds["birds"][0].set_volume(self.birdsVolumeSetter(self.BIRDS_VOLUME, min(self.__distanceFromSea, self.AUDIBLE_SEA_RADIUS)))
                self.__isBirdsPlaying = True

    def seagull(self):
        if self.canHearBeach():
            if Window.getTicks() > self.__nextSeagull:
                self.__playingSeagull = choice(self.__sounds["seagull"])
                self.__playingSeagull.set_volume(self.beachVolumeSetter(self.SEAGULL_VOLUME, self.__distanceFromSea))
                self.__playingSeagull.play()
                self.__nextSeagull = Window.getTicks() + randint(self.MINIMUM_NEXT_SEAGULL, self.MAXIMUM_NEXT_SEAGULL)
            self.__playingSeagull.set_volume(self.beachVolumeSetter(self.SEAGULL_VOLUME, self.__distanceFromSea))

    def beach(self):
        if self.__isBeachPlaying:
            if self.canHearBeach():
                self.__sounds["beach"][0].set_volume(self.beachVolumeSetter(self.SEA_VOLUME, self.__distanceFromSea))
            else:
                self.__sounds["beach"][0].stop()
                self.__isBeachPlaying = False
        else:
            if self.canHearBeach():
                self.__sounds["beach"][0].play(-1)
                self.__sounds["beach"][0].set_volume(self.beachVolumeSetter(self.SEA_VOLUME, self.__distanceFromSea))
                self.__isBeachPlaying = True

    def __updateDistanceFromBeach(self, map, player):
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