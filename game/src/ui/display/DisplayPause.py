import pygame

from src.ui.display.Display import Display

class DisplayPause(Display):
    def __init__(self, window, background, displayGame):
        super().__init__(window, background)
        self.__displayGame = displayGame

    def updateBackground(self, flip=False):
        if flip:
            self._background.rescale(self._window)
        self._window.getScreen().blit(self._background.get(), (0,0))

    def flip(self):
        self.__displayGame.flip(True)
        self.updateBackground(True)
        for widget in self._objectsOnScreen:
            widget.update()
            self._window.getScreen().blit(widget.get(), widget.getRect()) 
        pygame.display.update()
