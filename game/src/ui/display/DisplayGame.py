import pygame

from game.src.ui.display.Display import Display

class DisplayGame(Display):
    def __init__(self, window, background, camera):
        super().__init__(window, background)
        self.__camera = camera
        #self.__characterInGame = []

    def updateBackground(self, cameraPosition):
        topLeft = self._window.getScreen().get_rect(topleft = cameraPosition.toTuple())
        self._window.getScreen().blit(self._background.get(), (0, 0), topLeft)

    def flip(self):
        cameraPosition = self.__camera.get()
        self.updateBackground(cameraPosition)
        for character in self._objectsOnScreen:
            character.update(character.getPosition() - cameraPosition)
            self._window.getScreen().blit(character.getSprite().get(), character.getSprite().getRect())
        pygame.display.update()

    def update(self):
        rectToUpdate = []
        cameraPosition = self.__camera.get()
        if self.__camera.hasMoved():
            self.flip()
        else:
            self.updateBackground(cameraPosition)
            for character in self._objectsToUpdate:
                rectToUpdate.append(character.getSprite().getRect().copy())
                character.update(character.getPosition() - cameraPosition)
                rectToUpdate.append(character.getSprite().getRect())
                self._window.getScreen().blit(character.getSprite().get(), character.getSprite().getRect())
            pygame.display.update(rectToUpdate)
        self._objectsToUpdate = []