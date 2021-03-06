import pygame

from src.ui.background.Background import Background

class BackgroundImage(Background):
    def __init__(self, path):
        super().__init__(pygame.image.load(path).convert_alpha())

    def rescale(self, window):
        self._background = pygame.transform.scale(self._background, window.getSize().toTuple())