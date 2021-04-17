import pygame
from game.src.ui.background.Background import Background

class BackgroundImage(Background):
    def __init__(self, path):
        super().__init__(pygame.image.load(path).convert_alpha())
    
    def get(self):
        return self._background

    def rescale(self, window):
        self._background = pygame.transform.scale(self._background, window.getSize().toTuple())