import pygame
from game.src.ui.Sprite import Sprite
from game.src.core.TilesEnum import TilesEnum

class Display:
    BUFFER = 2

    def update(self, view, window, player, spriteStore):
        xOff = player.getOffSet()[0]
        yOff = player.getOffSet()[1]
        height = len(view.get())
        width = len(view.get()[0])

        for row in range(height):
            for col in range(width):
                value = view.get()[row][col]

                groundSprite = spriteStore.get("grounds", TilesEnum.getID(value))
                window.getScreen().blit(groundSprite.get(), ((col - self.BUFFER) * Sprite.GROUND_TILE_SIZE - xOff, (row - self.BUFFER) * Sprite.GROUND_TILE_SIZE - yOff))

                playerSprite = spriteStore.get("players", 0)
                window.getScreen().blit(playerSprite.get(), (Sprite.GROUND_TILE_SIZE * ((view.getViewSize()[0] - 2 * self.BUFFER) // 2), Sprite.GROUND_TILE_SIZE * ((view.getViewSize()[1] - 2 * self.BUFFER) // 2) - playerSprite.getHeight()))


    
