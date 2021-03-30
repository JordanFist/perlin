import pygame
from game.src.ui.Sprite import Sprite
from game.src.core.TilesEnum import TilesEnum

class Display:
    BUFFER = 2

    """ Returns player offset (xOff, yOff) """
    def __getOffSet(self, player):
        return (int(player.getPosition()[0] % Sprite.GROUND_TILE_SIZE), int(player.getPosition()[1] % Sprite.GROUND_TILE_SIZE))

    def update(self, view, window, player, spriteStore):
        xOff, yOff = self.__getOffSet(player)
        height = len(view.get())
        width = len(view.get()[0])

        for row in range(height):
            for col in range(width):
                value = view.get()[row][col]

                groundSprite = spriteStore.get("grounds", TilesEnum.getID(value))
                window.getScreen().blit(groundSprite.get(), ((col - self.BUFFER) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.BUFFER) * Sprite.GROUND_TILE_SIZE - yOff))

                playerSprite = spriteStore.getPlayer()
                playerSprite.setPosition((Sprite.GROUND_TILE_SIZE * ((view.getViewSize()[0] - 2 * self.BUFFER) // 2), Sprite.GROUND_TILE_SIZE * ((view.getViewSize()[1] - 2 * self.BUFFER) // 2)))
                window.getScreen().blit(playerSprite.get(), playerSprite.getRect())


    
