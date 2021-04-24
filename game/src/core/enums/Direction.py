import pygame

class Direction:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @classmethod
    def keyToDir(cls, key):
        if (key == pygame.K_z):
            return cls.UP
        if (key == pygame.K_s):
            return cls.DOWN
        if (key == pygame.K_q):
            return cls.LEFT
        if (key == pygame.K_d):
            return cls.RIGHT