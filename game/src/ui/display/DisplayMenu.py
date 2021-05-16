import pygame

from src.ui.display.Display import Display

class DisplayMenu(Display):
    def __init__(self, window, background):
        super().__init__(window, background)

    def updateBackground(self, flip=False):
        if flip:
            self._background.rescale(self._window)
        self._window.getScreen().blit(self._background.get(), (0,0))

    def flip(self):
        self.updateBackground(True)
        for widget in self._objectsOnScreen:
            widget.update()
            self._window.getScreen().blit(widget.get(), widget.getRect()) #text as the same rect as its button so we can get the rect of the button
        pygame.display.update()

    """def update(self):
        rectToUpdate = []
        self.updateBackground()
        for widget in self._objectsToUpdate:
            rectToUpdate.append(widget.getRect().copy())
            widget.update()
            rectToUpdate.append(widget.getRect())
            self._window.getScreen().blit(widget.get(), widget.getRect())
        pygame.display.update(rectToUpdate)
        self._objectsToUpdate = []"""
